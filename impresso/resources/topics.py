from typing import Any, Callable, Iterator, cast

from pandas import DataFrame, json_normalize

from impresso.api_client.api.topics import find_topics, get_topic
from impresso.api_client.models.find_topics_base_find_response import (
    FindTopicsBaseFindResponse,
)
from impresso.api_client.models.find_topics_order_by import (
    FindTopicsOrderBy,
    FindTopicsOrderByLiteral,
)
from impresso.api_client.types import UNSET
from impresso.api_models import BaseFind
from impresso.data_container import DataContainer, iterate_pages
from impresso.resources.base import Resource
from impresso.util.error import raise_for_error
from impresso.util.py import get_enum_from_literal


class FindTopicsSchema(BaseFind):
    """Schema for the find topics response."""

    data: list[dict]


class FindTopicsContainer(DataContainer):
    """Response of a find call."""

    def __init__(
        self,
        data: FindTopicsBaseFindResponse,
        pydantic_model: type[FindTopicsSchema],
        fetch_method: Callable[..., "FindTopicsContainer"],
        fetch_method_args: dict[str, Any],
        web_app_search_result_url: str | None = None,
    ):
        super().__init__(data, pydantic_model, web_app_search_result_url)
        self._fetch_method = fetch_method
        self._fetch_method_args = fetch_method_args

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        data = self._data.to_dict()["data"]
        if len(data):
            return json_normalize(self._data.to_dict()["data"]).set_index("uid")
        return DataFrame()

    def pages(self) -> Iterator["FindTopicsContainer"]:
        """Iterate over all pages of results."""
        yield self
        yield from iterate_pages(
            self._fetch_method,
            self._fetch_method_args,
            self.offset,
            self.limit,
            self.total,
        )


class GetTopicContainer(DataContainer):
    """Response of a get call."""

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        data = self._data.to_dict()
        if len(data):
            return json_normalize([self._data.to_dict()]).set_index("uid")
        return DataFrame()


class TopicsResource(Resource):
    """
    Search topics in the Impresso database.

    Examples:
        Search for topics containing specific words:
        >>> results = topics.find(term="economy") # doctest: +SKIP
        >>> print(results.df) # doctest: +SKIP

        Get a specific topic by its ID:
        >>> topic_id = "some-topic-id" # Replace with a real ID
        >>> topic = topics.get(topic_id) # doctest: +SKIP
        >>> print(topic.df) # doctest: +SKIP

        Iterate through all pages of topic search results:
        >>> results = topics.find(term="war", limit=10) # doctest: +SKIP
        >>> for page in results.pages(): # doctest: +SKIP
        ...     print(page.df) # doctest: +SKIP
    """

    name = "topics"

    def find(
        self,
        term: str | None = None,
        order_by: FindTopicsOrderByLiteral | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> FindTopicsContainer:
        """
        Search topics in Impresso.

        Args:
            term: Search term to find topics by their words.
            order_by: Field to order results by.
            limit: Number of results to return.
            offset: Number of results to skip.

        Returns:
            FindTopicsContainer: Data container with a page of results of the search.
        """

        result = find_topics.sync(
            client=self._api_client,
            q=term if term is not None else UNSET,
            order_by=(
                get_enum_from_literal(order_by, FindTopicsOrderBy)
                if order_by is not None
                else UNSET
            ),
            limit=limit if limit is not None else UNSET,
            offset=offset if offset is not None else UNSET,
            filters=UNSET,
        )
        raise_for_error(result)
        return FindTopicsContainer(
            cast(FindTopicsBaseFindResponse, result),
            FindTopicsSchema,
            fetch_method=self.find,
            fetch_method_args={
                "term": term,
                "order_by": order_by,
            },
            web_app_search_result_url=(
                _build_web_app_find_topics_url(
                    base_url=self._get_web_app_base_url(),
                    term=term,
                )
            ),
        )

    def get(self, id: str) -> GetTopicContainer:
        """Get topic by ID.

        Args:
            id: The ID of the topic to retrieve.

        Returns:
            GetTopicContainer: Data container with the topic information.
        """

        result = get_topic.sync(
            client=self._api_client,
            id=id,
        )
        raise_for_error(result)
        return GetTopicContainer(
            result,
            FindTopicsSchema,
            web_app_search_result_url=_build_web_app_get_topic_url(
                base_url=self._get_web_app_base_url(),
                id=id,
            ),
        )


def _build_web_app_find_topics_url(
    base_url: str,
    term: str | None = None,
) -> str:
    query_params = {
        "q": term,
    }
    query_string = "&".join(
        f"{key}={value}" for key, value in query_params.items() if value is not None
    )
    url = f"{base_url}/topics"
    return f"{url}?{query_string}" if query_string else url


def _build_web_app_get_topic_url(
    base_url: str,
    id: str,
) -> str:
    return f"{base_url}/topics/{id}"
