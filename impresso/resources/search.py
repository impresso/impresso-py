from pandas import DataFrame, json_normalize

from impresso.api_client.api.search import search
from impresso.api_client.models.article_access_right import ArticleAccessRightLiteral
from impresso.api_client.models.search_group_by import SearchGroupBy
from impresso.api_client.models.search_order_by import (
    SearchOrderBy,
    SearchOrderByLiteral,
)
from impresso.api_client.types import UNSET
from impresso.api_models import Q, Article, BaseFind, Filter
from impresso.data_container import DataContainer
from impresso.resources.base import Resource
from impresso.structures import AND, OR, DateRange, NumericRange
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
        newspaper_id: str | OR[str] | None = None,
        date_range: DateRange | None = None,
        language: str | OR[str] | None = None,
        mention: str | AND[str] | OR[str] | None = None,
        topic_id: str | AND[str] | OR[str] | None = None,
        collection_id: str | OR[str] | None = None,
        country: str | OR[str] | None = None,
        access_rights: (
            ArticleAccessRightLiteral | OR[ArticleAccessRightLiteral] | None
        ) = None,
        partner_id: str | OR[str] | None = None,
        text_reuse_cluster_id: str | OR[str] | None = None,
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
            language: Return only articles that are in this language or all/any of the languages.
            mention: Return only articles that mention an entity with this term or all/any of entities with the terms.
            topic_id: Return only articles that are about this topic or all/any of the topics.
            collection_id: Return only articles that are in this collection or all/any of the collections.
            country: Return only articles that are from this country or all/any of the countries.
            access_rights: Return only articles with this access right or all/any of the access rights.
            partner_id: Return only articles that are from this partner or all/any of the partners.
            text_reuse_cluster_id: Return only articles that are in this text reuse cluster or all/any of the clusters.

        Returns:
            _type_: _description_
        """
        filters: list[Filter] = []
        if with_text_contents:
            filters.append(Filter(type="has_text_contents", daterange=None))
        if title is not None:
            filters.extend(and_or_filter(title, "title"))
        if front_page:
            filters.append(Filter(type="is_front", daterange=None))
        if entity_id is not None:
            filters.extend(and_or_filter(entity_id, "entity"))
        if newspaper_id is not None:
            filters.extend(and_or_filter(newspaper_id, "newspaper"))
        if date_range is not None:
            filters.append(
                Filter(
                    type="daterange",
                    q=Q(DateRange._as_filter_value(date_range)),
                    context="exclude" if date_range.inverted else "include",
                    daterange=None,
                )
            )
        if language is not None:
            filters.extend(and_or_filter(language, "language"))
        if mention is not None:
            filters.extend(and_or_filter(mention, "mention"))
        if topic_id is not None:
            filters.extend(and_or_filter(topic_id, "topic"))
        if collection_id is not None:
            filters.extend(and_or_filter(collection_id, "collection"))
        if country is not None:
            filters.extend(and_or_filter(country, "country"))
        if access_rights is not None:
            filters.extend(and_or_filter(access_rights, "access_right"))
        if partner_id is not None:
            filters.extend(and_or_filter(partner_id, "partner"))
        if text_reuse_cluster_id is not None:
            filters.extend(and_or_filter(text_reuse_cluster_id, "text_reuse_cluster"))

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
            filters=filters_pb if filters_pb else UNSET,
            limit=limit if limit is not None else UNSET,
            offset=offset if offset is not None else UNSET,
        )
        raise_for_error(result)
        return SearchDataContainer(result, SearchResponseSchema)
