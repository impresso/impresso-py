from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provenance_verification_response_json_type_0_claims_type_1_kind import (
    ProvenanceVerificationResponseJsonType0ClaimsType1Kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProvenanceVerificationResponseJsonType0ClaimsType1")


@_attrs_define
class ProvenanceVerificationResponseJsonType0ClaimsType1:
    """
    Attributes:
        kind (Union[Unset, ProvenanceVerificationResponseJsonType0ClaimsType1Kind]):
    """

    kind: Union[Unset, ProvenanceVerificationResponseJsonType0ClaimsType1Kind] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, ProvenanceVerificationResponseJsonType0ClaimsType1Kind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = ProvenanceVerificationResponseJsonType0ClaimsType1Kind(_kind)

        provenance_verification_response_json_type_0_claims_type_1 = cls(
            kind=kind,
        )

        provenance_verification_response_json_type_0_claims_type_1.additional_properties = d
        return provenance_verification_response_json_type_0_claims_type_1

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
