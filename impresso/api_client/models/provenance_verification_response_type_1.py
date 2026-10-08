from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProvenanceVerificationResponseType1")


@_attrs_define
class ProvenanceVerificationResponseType1:
    """
    Attributes:
        valid (bool):
        reason (str):
    """

    valid: bool
    reason: str

    def to_dict(self) -> Dict[str, Any]:
        valid = self.valid

        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "valid": valid,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        valid = d.pop("valid")

        reason = d.pop("reason")

        provenance_verification_response_type_1 = cls(
            valid=valid,
            reason=reason,
        )

        return provenance_verification_response_type_1
