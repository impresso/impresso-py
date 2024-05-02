from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_data import ErrorData


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """Default error response. TODO: replace with https://datatracker.ietf.org/doc/html/rfc9457

    Attributes:
        message (str):
        data (Union[Unset, ErrorData]):
    """

    message: str
    data: Union[Unset, "ErrorData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_data import ErrorData

        d = src_dict.copy()
        message = d.pop("message")

        _data = d.pop("data", UNSET)
        data: Union[Unset, ErrorData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ErrorData.from_dict(_data)

        error = cls(
            message=message,
            data=data,
        )

        error.additional_properties = d
        return error

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
