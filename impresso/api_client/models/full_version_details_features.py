from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.full_version_details_features_additional_property import FullVersionDetailsFeaturesAdditionalProperty


T = TypeVar("T", bound="FullVersionDetailsFeatures")


@_attrs_define
class FullVersionDetailsFeatures:
    """ """

    additional_properties: Dict[str, "FullVersionDetailsFeaturesAdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.full_version_details_features_additional_property import (
            FullVersionDetailsFeaturesAdditionalProperty,
        )

        d = src_dict.copy()
        full_version_details_features = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = FullVersionDetailsFeaturesAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        full_version_details_features.additional_properties = additional_properties
        return full_version_details_features

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "FullVersionDetailsFeaturesAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "FullVersionDetailsFeaturesAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
