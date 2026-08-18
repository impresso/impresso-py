from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.filter_ import Filter


T = TypeVar("T", bound="FilterSerializationRequest")


@_attrs_define
class FilterSerializationRequest:
    """Request payload for POST /tools/filters/serialize

    Attributes:
        filters (List['Filter']): A list of Impresso search filters.
    """

    filters: List["Filter"]

    def to_dict(self) -> Dict[str, Any]:
        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "filters": filters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_ import Filter

        d = src_dict.copy()
        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = Filter.from_dict(filters_item_data)

            filters.append(filters_item)

        filter_serialization_request = cls(
            filters=filters,
        )

        return filter_serialization_request
