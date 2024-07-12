from typing import List, Union

from pandas import DataFrame, json_normalize

from impresso.api_client.api.search import search
from impresso.api_client.models.search_facets import SearchFacets, SearchFacetsLiteral
from impresso.api_client.models.search_group_by import (
    SearchGroupBy,
    SearchGroupByLiteral,
)
from impresso.api_client.models.search_order_by import (
    SearchOrderBy,
    SearchOrderByLiteral,
)
from impresso.api_client.types import UNSET, Unset
from impresso.api_models import Article, BaseFind, Filter
from impresso.data_container import DataContainer
from impresso.resources.base import Resource
from impresso.util.error import raise_for_error
from impresso.util.py import get_enum_from_literal


class SearchResponseSchema(BaseFind):
    """Schema for the articles response."""

    data: list[Article]


class SearchDataContainer(DataContainer):
    """Response of a search call."""

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        return json_normalize(self._data.to_dict()["data"]).set_index("uid")


class SearchResource(Resource):
    """Search articles in the impresso database."""

    name = "search"

    def find(
        self,
        q: Union[Unset, str] = UNSET,
        group_by: SearchGroupByLiteral = "articles",
        order_by: Union[Unset, SearchOrderByLiteral] = UNSET,
        facets: Union[Unset, SearchFacetsLiteral] = UNSET,
        filters: Union[Unset, List[Filter]] = UNSET,
        limit: Union[Unset, int] = UNSET,
        offset: Union[Unset, int] = UNSET,
    ):
        result = search.sync(
            client=self._api_client,
            q=q,
            group_by=get_enum_from_literal(group_by, SearchGroupBy),
            order_by=get_enum_from_literal(order_by, SearchOrderBy),
            facets=get_enum_from_literal(facets, SearchFacets),
            filters=filters,
            limit=limit,
            offset=offset,
        )
        raise_for_error(result)
        return SearchDataContainer(result, SearchResponseSchema)
