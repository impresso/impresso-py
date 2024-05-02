from typing import Any, Union

from pandas import DataFrame, json_normalize
from impresso.api_client.models.get_articles_filters import GetArticlesFilters
from impresso.api_client.models.get_articles_order_by import (
    GetArticlesOrderBy,
    GetArticlesOrderByLiteral,
)
from impresso.api_client.models.get_articles_resolve import (
    GetArticlesResolve,
    GetArticlesResolveLiteral,
)
from impresso.api_client.types import UNSET, Unset
from impresso.data_container import DataContainer
from impresso.resources.base import Resource
from impresso.api_client.api.articles import get_articles, get_articles_id
from impresso.util.py import get_enum_from_literal
from impresso.api_models import Article, BaseFind


class ArticlesResponseSchema(BaseFind):
    """Schema for the articles response."""

    data: list[Article]


class ArticlesDataContainer(DataContainer):
    """Response of an articles call."""

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        return json_normalize(self._data.to_dict()["data"]).set_index("uid")


class ArticleDataContainer(DataContainer):
    """Response of a get article call."""

    @property
    def raw(self) -> dict[str, Any]:
        """Return the data as a python dictionary."""
        return self._data.to_dict()

    @property
    def pydantic(self) -> Article:
        """Return the data as a pydantic model."""
        return self._pydantic_model.model_validate(self.raw)

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        return json_normalize([self.raw])


class ArticlesResource(Resource):
    """Get articles from the impresso database."""

    name = "articles"

    def find(
        self,
        resolve: Union[Unset, GetArticlesResolveLiteral] = UNSET,
        order_by: Union[Unset, GetArticlesOrderByLiteral] = UNSET,
        filters: Union[Unset, GetArticlesFilters] = UNSET,
        limit: Union[Unset, int] = UNSET,
        skip: Union[Unset, int] = UNSET,
    ):
        result = get_articles.sync(
            client=self._api_client,
            resolve=get_enum_from_literal(resolve, GetArticlesResolve),
            order_by=get_enum_from_literal(order_by, GetArticlesOrderBy),
            filters=filters,
            limit=limit,
            skip=skip,
        )

        return ArticlesDataContainer(result, ArticlesResponseSchema)

    def get(self, id: str):
        result = get_articles_id.sync(client=self._api_client, id=id)
        return ArticleDataContainer(result, Article)
