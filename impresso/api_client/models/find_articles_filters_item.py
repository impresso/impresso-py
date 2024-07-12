from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.find_articles_filters_item_type import FindArticlesFiltersItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FindArticlesFiltersItem")


@_attrs_define
class FindArticlesFiltersItem:
    """
    Attributes:
        type (FindArticlesFiltersItemType):
        q (Union[Unset, str]):
    """

    type: FindArticlesFiltersItemType
    q: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        q = self.q

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )
        if q is not UNSET:
            field_dict["q"] = q

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = FindArticlesFiltersItemType(d.pop("type"))

        q = d.pop("q", UNSET)

        find_articles_filters_item = cls(
            type=type,
            q=q,
        )

        return find_articles_filters_item
