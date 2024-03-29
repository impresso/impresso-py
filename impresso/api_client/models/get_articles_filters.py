from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.get_articles_filters_type import GetArticlesFiltersType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetArticlesFilters")


@_attrs_define
class GetArticlesFilters:
    """
    Attributes:
        type (GetArticlesFiltersType):
        q (Union[Unset, str]):
    """

    type: GetArticlesFiltersType
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
        type = GetArticlesFiltersType(d.pop("type"))

        q = d.pop("q", UNSET)

        get_articles_filters = cls(
            type=type,
            q=q,
        )

        return get_articles_filters
