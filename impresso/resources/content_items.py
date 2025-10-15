from typing import Any, Callable, Iterator

from pandas import DataFrame, json_normalize
from pydantic import BaseModel

from impresso.api_client.api.content_items import get_content_item
from impresso.api_models import ContentItem, BaseFind
from impresso.data_container import DataContainer, iterate_pages
from impresso.resources.base import Resource
from impresso.util.error import raise_for_error


class ContentItemsResponseSchema(BaseFind):
    """Schema for the content items response."""

    data: list[ContentItem]


class ContentItemsDataContainer(DataContainer):
    """Response of a find content items call, supports pagination."""

    def __init__(
        self,
        data: BaseModel,
        pydantic_model: type[ContentItemsResponseSchema],
        fetch_method: Callable[..., "ContentItemsDataContainer"],
        fetch_method_args: dict[str, Any],
        web_app_search_result_url: str | None = None,
    ):
        super().__init__(data, pydantic_model, web_app_search_result_url)
        self._fetch_method = fetch_method
        self._fetch_method_args = fetch_method_args

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        return json_normalize(self._data.to_dict()["data"]).set_index("uid")

    def pages(self) -> Iterator["ContentItemsDataContainer"]:
        """Iterate over all pages of results."""
        yield self
        yield from iterate_pages(
            self._fetch_method,
            self._fetch_method_args,
            self.offset,
            self.limit,
            self.total,
        )


class ContentItemDataContainer(DataContainer):
    """Response of a get content item call."""

    @property
    def raw(self) -> dict[str, Any]:
        """Return the data as a python dictionary."""
        return self._data.to_dict()

    @property
    def pydantic(self) -> ContentItem:
        """Return the data as a pydantic model."""
        return self._pydantic_model.model_validate(self.raw)

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        return json_normalize([self.raw])

    @property
    def size(self) -> int:
        """Current page size."""
        data = self._data.to_dict()
        if len(data):
            return 1
        return 0

    @property
    def total(self) -> int:
        """Total number of results."""
        return self.size


class ContentItemsResource(Resource):
    """Get content items from the impresso database."""

    name = "content_items"

    def get(
        self, id: str, include_embeddings: bool = False
    ) -> ContentItemDataContainer:
        """
        Get a content item by its id.

        Args:
            id (str): The id of the content item.
            include_embeddings (bool): Whether to include embeddings in the response.

        Returns:
            ContentItemDataContainer: The content item data container.
        """
        result = get_content_item.sync(
            client=self._api_client,
            id=id,
            include_embeddings=include_embeddings,
        )
        raise_for_error(result)

        id_parts = id.split("-")
        issue_id = "-".join(id_parts[:-1])
        article_id = id_parts[-1]

        return ContentItemDataContainer(
            result,
            ContentItem,
            f"{self._get_web_app_base_url()}/issue/{issue_id}/view?articleId={article_id}",
        )

    def get_embeddings(self, id: str) -> list[str]:
        """
        Get the embeddings of a content item by its id.
        Args:
            id (str): The id of the content item.
        Returns:
            list[str]: The embeddings of the content item if present (every embedding is returned
            in the canonical form: <model>:<base64_embedding>).
        """
        item = self.get(id, include_embeddings=True)
        return item.raw.get("embeddings", []) if item else []
