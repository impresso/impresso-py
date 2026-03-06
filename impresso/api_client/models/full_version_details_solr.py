from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.full_version_details_solr_endpoints import FullVersionDetailsSolrEndpoints


T = TypeVar("T", bound="FullVersionDetailsSolr")


@_attrs_define
class FullVersionDetailsSolr:
    """
    Attributes:
        endpoints (Union[Unset, FullVersionDetailsSolrEndpoints]):
    """

    endpoints: Union[Unset, "FullVersionDetailsSolrEndpoints"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endpoints: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.endpoints, Unset):
            endpoints = self.endpoints.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if endpoints is not UNSET:
            field_dict["endpoints"] = endpoints

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.full_version_details_solr_endpoints import FullVersionDetailsSolrEndpoints

        d = src_dict.copy()
        _endpoints = d.pop("endpoints", UNSET)
        endpoints: Union[Unset, FullVersionDetailsSolrEndpoints]
        if isinstance(_endpoints, Unset):
            endpoints = UNSET
        else:
            endpoints = FullVersionDetailsSolrEndpoints.from_dict(_endpoints)

        full_version_details_solr = cls(
            endpoints=endpoints,
        )

        full_version_details_solr.additional_properties = d
        return full_version_details_solr

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
