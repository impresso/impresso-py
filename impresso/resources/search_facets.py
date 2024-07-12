from typing import Any, Union

from pandas import DataFrame, json_normalize

from impresso.api_client.api.search_facets import get_search_facet
from impresso.api_client.models.get_search_facet_id import (
    GetSearchFacetId,
    GetSearchFacetIdLiteral,
)
from impresso.api_client.types import UNSET, Unset
from impresso.api_models import BaseFind, SearchFacet
from impresso.data_container import DataContainer
from impresso.resources.base import Resource
from impresso.util.error import raise_for_error
from impresso.util.py import get_enum_from_literal


class FacetsResponseSchema(BaseFind):
    """Schema for the search facets response."""

    data: list[SearchFacet]


class FacetsDataContainer(DataContainer):
    """Response of a search facets call."""

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        return json_normalize(self._data.to_dict()["data"]).set_index("type")


class FacetDataContainer(DataContainer):
    """Response of a get facet call."""

    @property
    def raw(self) -> dict[str, Any]:
        """Return the data as a python dictionary."""
        return self._data.to_dict()

    @property
    def pydantic(self) -> SearchFacet:
        """Return the data as a pydantic model."""
        return self._pydantic_model.model_validate(self.raw)

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        return json_normalize(self.raw["buckets"]).set_index("val")


class SearchFacetsResource(Resource):
    """Get articles from the impresso database."""

    name = "searchFacets"

    # def find(
    #     self,
    #     resolve: Union[Unset, GetArticlesResolveLiteral] = UNSET,
    #     order_by: Union[Unset, GetArticlesOrderByLiteral] = UNSET,
    #     filters: Union[Unset, GetArticlesFilters] = UNSET,
    #     limit: Union[Unset, int] = UNSET,
    #     skip: Union[Unset, int] = UNSET,
    # ):
    #     result = get_articles.sync(
    #         client=self._api_client,
    #         resolve=get_enum_from_literal(resolve, GetArticlesResolve),
    #         order_by=get_enum_from_literal(order_by, GetArticlesOrderBy),
    #         filters=filters,
    #         limit=limit,
    #         skip=skip,
    #     )

    #     return ArticlesDataContainer(result, ArticlesResponseSchema)

    def get(
        self,
        facet: GetSearchFacetIdLiteral,
        q: Union[Unset, str] = UNSET,
    ):
        result = get_search_facet.sync(
            client=self._api_client,
            id=get_enum_from_literal(facet, GetSearchFacetId),
            # q=q,
        )
        raise_for_error(result)
        return FacetDataContainer(result, SearchFacet)
