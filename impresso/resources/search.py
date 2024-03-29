from typing import List, Union

from impresso.api_client.api.search import get_search
from impresso.api_client.models.get_search_facets import GetSearchFacets
from impresso.api_client.models.get_search_filters_item import GetSearchFiltersItem
from impresso.api_client.models.get_search_group_by import GetSearchGroupBy
from impresso.api_client.models.get_search_order_by import GetSearchOrderBy
from impresso.api_client.types import UNSET, Unset
from impresso.api_models import SearchResponseSchema
from impresso.data_container import DataContainer
from impresso.resources.base import Resource


class SearchResource(Resource):
    """Search articles in the impresso database."""

    name = "search"

    def find(
        self,
        q: Union[Unset, str] = UNSET,
        group_by: GetSearchGroupBy = GetSearchGroupBy.ARTICLES,
        order_by: Union[Unset, GetSearchOrderBy] = UNSET,
        facets: Union[Unset, GetSearchFacets] = UNSET,
        filters: Union[Unset, List[GetSearchFiltersItem]] = UNSET,
        limit: Union[Unset, int] = UNSET,
        skip: Union[Unset, int] = UNSET,
    ):
        result = get_search.sync(
            client=self._api_client,
            q=q,
            group_by=group_by,
            order_by=order_by,
            facets=facets,
            filters=filters,
            limit=limit,
            skip=skip,
        )
        return DataContainer(result, SearchResponseSchema)
