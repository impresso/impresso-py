from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_provider import DataProvider
    from ..models.find_data_providers_base_find_response_meta import FindDataProvidersBaseFindResponseMeta
    from ..models.find_data_providers_base_find_response_pagination import FindDataProvidersBaseFindResponsePagination


T = TypeVar("T", bound="FindDataProvidersBaseFindResponse")


@_attrs_define
class FindDataProvidersBaseFindResponse:
    """
    Attributes:
        data (List['DataProvider']):
        pagination (FindDataProvidersBaseFindResponsePagination):
        meta (Union[Unset, FindDataProvidersBaseFindResponseMeta]):
    """

    data: List["DataProvider"]
    pagination: "FindDataProvidersBaseFindResponsePagination"
    meta: Union[Unset, "FindDataProvidersBaseFindResponseMeta"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

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
        from ..models.data_provider import DataProvider
        from ..models.find_data_providers_base_find_response_meta import FindDataProvidersBaseFindResponseMeta
        from ..models.find_data_providers_base_find_response_pagination import (
            FindDataProvidersBaseFindResponsePagination,
        )

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = DataProvider.from_dict(data_item_data)

            data.append(data_item)

        pagination = FindDataProvidersBaseFindResponsePagination.from_dict(d.pop("pagination"))

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, FindDataProvidersBaseFindResponseMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = FindDataProvidersBaseFindResponseMeta.from_dict(_meta)

        find_data_providers_base_find_response = cls(
            data=data,
            pagination=pagination,
            meta=meta,
        )

        return find_data_providers_base_find_response
