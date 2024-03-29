from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.article import Article
    from ..models.article_search_response_info import ArticleSearchResponseInfo


T = TypeVar("T", bound="ArticleSearchResponse")


@_attrs_define
class ArticleSearchResponse:
    """Article search response

    Attributes:
        data (List['Article']):
        limit (int): The number of articles returned in this response
        skip (int): The number of articles skipped in this response
        total (int): The total number of articles matching the query
        info (ArticleSearchResponseInfo): Additional information about the search response.
    """

    data: List["Article"]
    limit: int
    skip: int
    total: int
    info: "ArticleSearchResponseInfo"

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        limit = self.limit

        skip = self.skip

        total = self.total

        info = self.info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "data": data,
                "limit": limit,
                "skip": skip,
                "total": total,
                "info": info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.article import Article
        from ..models.article_search_response_info import ArticleSearchResponseInfo

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Article.from_dict(data_item_data)

            data.append(data_item)

        limit = d.pop("limit")

        skip = d.pop("skip")

        total = d.pop("total")

        info = ArticleSearchResponseInfo.from_dict(d.pop("info"))

        article_search_response = cls(
            data=data,
            limit=limit,
            skip=skip,
            total=total,
            info=info,
        )

        return article_search_response
