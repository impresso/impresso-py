from typing import List, Union

from pandas import DataFrame, json_normalize

from impresso.api_client.api.search import get_search
from impresso.api_client.models.get_search_facets import (
    GetSearchFacets,
    GetSearchFacetsLiteral,
)
from impresso.api_client.models.get_search_group_by import (
    GetSearchGroupBy,
    GetSearchGroupByLiteral,
)
from impresso.api_client.models.get_search_order_by import (
    GetSearchOrderBy,
    GetSearchOrderByLiteral,
)
from impresso.api_client.types import UNSET, Unset
from impresso.api_models import BaseFind, Article, Filter
from impresso.data_container import DataContainer
from impresso.resources.base import Resource
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
        group_by: GetSearchGroupByLiteral = "articles",
        order_by: Union[Unset, GetSearchOrderByLiteral] = UNSET,
        facets: Union[Unset, GetSearchFacetsLiteral] = UNSET,
        filters: Union[Unset, List[Filter]] = UNSET,
        limit: Union[Unset, int] = UNSET,
        skip: Union[Unset, int] = UNSET,
    ):
        result = get_search.sync(
            client=self._api_client,
            q=q,
            group_by=get_enum_from_literal(group_by, GetSearchGroupBy),
            order_by=get_enum_from_literal(order_by, GetSearchOrderBy),
            facets=get_enum_from_literal(facets, GetSearchFacets),
            filters=filters,
            limit=limit,
            skip=skip,
        )
        return SearchDataContainer(result, SearchResponseSchema)
