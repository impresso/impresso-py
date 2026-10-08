from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_find_response_meta import BaseFindResponseMeta
    from ..models.base_find_response_pagination import BaseFindResponsePagination


T = TypeVar("T", bound="BaseFindResponse")


@_attrs_define
class BaseFindResponse:
    """
    Attributes:
        data (List[Any]):
        pagination (BaseFindResponsePagination):
        meta (Union[Unset, BaseFindResponseMeta]):
    """

    data: List[Any]
    pagination: "BaseFindResponsePagination"
    meta: Union[Unset, "BaseFindResponseMeta"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        data = self.data

        pagination = self.pagination.to_dict()

        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "data": data,
                "pagination": pagination,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_find_response_meta import BaseFindResponseMeta
        from ..models.base_find_response_pagination import BaseFindResponsePagination

        d = src_dict.copy()
        data = cast(List[Any], d.pop("data"))

        pagination = BaseFindResponsePagination.from_dict(d.pop("pagination"))

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, BaseFindResponseMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = BaseFindResponseMeta.from_dict(_meta)

        base_find_response = cls(
            data=data,
            pagination=pagination,
            meta=meta,
        )

        return base_find_response
