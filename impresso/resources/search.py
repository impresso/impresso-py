from pandas import DataFrame, json_normalize

from impresso.api_client.api.search import search
from impresso.api_client.models.search_group_by import SearchGroupBy
from impresso.api_client.models.search_order_by import (
    SearchOrderBy,
    SearchOrderByLiteral,
)
from impresso.api_client.types import UNSET
from impresso.api_models import Article, BaseFind, Filter
from impresso.data_container import DataContainer
from impresso.resources.base import Resource
from impresso.structures import AND, OR, DateRange
from impresso.util.error import raise_for_error
from impresso.util.filters import and_or_filter, filters_as_protobuf
from impresso.util.py import get_enum_from_literal, get_enum_from_literal_required


class SearchResponseSchema(BaseFind):
    """Schema for the articles response."""

    data: list[Article]


class SearchDataContainer(DataContainer):
    """Response of a search call."""

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        data = self._data.to_dict()["data"]
        if len(data):
            return json_normalize(self._data.to_dict()["data"]).set_index("uid")
        return DataFrame()


class SearchResource(Resource):
    """Search articles in the impresso database."""

    name = "search"

    def find(
        self,
        q: str | None = None,
        order_by: SearchOrderByLiteral | None = None,
        limit: int | None = None,
        offset: int | None = None,
        with_text_contents: bool | None = False,
        title: str | AND[str] | OR[str] | None = None,
        front_page: bool | None = None,
        entity_id: str | AND[str] | OR[str] | None = None,
        newspaper_id: str | AND[str] | OR[str] | None = None,
        date_range: DateRange | None = None,
    ) -> SearchDataContainer:
        """
        Search for articles in Impresso.

        Args:
            q: Search term.
            order_by: Order by aspect.
            limit: Number of results to return.
            offset: Number of results to skip.

            with_text_contents: Return only articles with text contents.
            title: Return only articles that have this term or all/any of the terms in the title.
            front_page: Return only articles that were on the front page.
            entity_id: Return only articles that mention this entity or all/any of the entities.
            date_range: Return only articles that were published in this date range.

        Returns:
            _type_: _description_
        """
        filters: list[Filter] = []
        if with_text_contents:
            filters.append(Filter(type="has_text_contents"))
        if title is not None:
            filters.append(and_or_filter(title, "title"))
        if front_page:
            filters.append(Filter(type="is_front"))
        if entity_id is not None:
            filters.append(and_or_filter(entity_id, "entity"))
        if newspaper_id is not None:
            filters.append(and_or_filter(newspaper_id, "newspaper"))
        if date_range is not None:
            filters.append(
                Filter(type="daterange", q=DateRange._as_filter_value(date_range))
            )

        filters_pb = filters_as_protobuf(filters or [])

        result = search.sync(
            client=self._api_client,
            q=q if q is not None else UNSET,
            order_by=(
                get_enum_from_literal(order_by, SearchOrderBy)
                if order_by is not None
                else UNSET
            ),
            group_by=get_enum_from_literal_required("articles", SearchGroupBy),
            filters=filters_pb,
            limit=limit if limit is not None else UNSET,
            offset=offset if offset is not None else UNSET,
        )
        raise_for_error(result)
        return SearchDataContainer(result, SearchResponseSchema)
