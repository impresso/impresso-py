from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="FilterSerializationResponse")


@_attrs_define
class FilterSerializationResponse:
    """Response for POST /tools/filters/serialize

    Attributes:
        filters (str): The protobuf base64 serialized filters string.
    """

    filters: str

    def to_dict(self) -> Dict[str, Any]:
        filters = self.filters

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "filters": filters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        filters = d.pop("filters")

        filter_serialization_response = cls(
            filters=filters,
        )

        return filter_serialization_response
