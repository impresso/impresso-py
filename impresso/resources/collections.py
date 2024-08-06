from pandas import DataFrame, json_normalize
from impresso.api_client.api.collections import find_collections, get_collection
from impresso.api_client.models.find_collections_order_by import (
    FindCollectionsOrderBy,
    FindCollectionsOrderByLiteral,
)
from impresso.api_client.types import UNSET
from impresso.api_models import BaseFind, Collection
from impresso.data_container import DataContainer
from impresso.resources.base import Resource
from impresso.util.error import raise_for_error
from impresso.util.py import get_enum_from_literal


class FindCollectionsSchema(BaseFind):
    """Schema for the find collections response."""

    data: list[Collection]


class FindCollectionsContainer(DataContainer):
    """Response of a find call."""

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        data = self._data.to_dict()["data"]
        if len(data):
            return json_normalize(self._data.to_dict()["data"]).set_index("uid")
        return DataFrame()


class CollectionsResource(Resource):
    """Work with collections"""

    name = "collections"

    def find(
        self,
        q: str | None = None,
        order_by: FindCollectionsOrderByLiteral | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> FindCollectionsContainer:
        """Find collections."""

        result = find_collections.sync(
            client=self._api_client,
            q=q if q is not None else UNSET,
            order_by=(
                get_enum_from_literal(order_by, FindCollectionsOrderBy)
                if order_by is not None
                else UNSET
            ),
            limit=limit if limit is not None else UNSET,
            offset=offset if offset is not None else UNSET,
        )
        raise_for_error(result)
        return FindCollectionsContainer(result, FindCollectionsSchema)

    def get(self, id: str) -> FindCollectionsContainer:
        """Get collection by ID."""

        result = get_collection.sync(
            client=self._api_client,
            id=id,
        )
        raise_for_error(result)
        return FindCollectionsContainer(result, FindCollectionsSchema)
