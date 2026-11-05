from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provenance_verification_response_provenance_verification_api_claims import (
        ProvenanceVerificationResponseProvenanceVerificationApiClaims,
    )
    from ..models.provenance_verification_response_provenance_verification_export_claims import (
        ProvenanceVerificationResponseProvenanceVerificationExportClaims,
    )


T = TypeVar("T", bound="ProvenanceVerificationResponse")


@_attrs_define
class ProvenanceVerificationResponse:
    """Signed delivery receipts identify receiving accounts and ordered item IDs only. They do not attest item content or
    identify a publisher.

        Attributes:
            valid (bool):
            claims (Union['ProvenanceVerificationResponseProvenanceVerificationApiClaims',
                'ProvenanceVerificationResponseProvenanceVerificationExportClaims', Unset]):
            ids_match (Union[Unset, bool]):
            reason (Union[Unset, str]):
    """

    valid: bool
    claims: Union[
        "ProvenanceVerificationResponseProvenanceVerificationApiClaims",
        "ProvenanceVerificationResponseProvenanceVerificationExportClaims",
        Unset,
    ] = UNSET
    ids_match: Union[Unset, bool] = UNSET
    reason: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.provenance_verification_response_provenance_verification_api_claims import (
            ProvenanceVerificationResponseProvenanceVerificationApiClaims,
        )

        valid = self.valid

        claims: Union[Dict[str, Any], Unset]
        if isinstance(self.claims, Unset):
            claims = UNSET
        elif isinstance(self.claims, ProvenanceVerificationResponseProvenanceVerificationApiClaims):
            claims = self.claims.to_dict()
        else:
            claims = self.claims.to_dict()

        ids_match = self.ids_match

        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "valid": valid,
            }
        )
        if claims is not UNSET:
            field_dict["claims"] = claims
        if ids_match is not UNSET:
            field_dict["idsMatch"] = ids_match
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.provenance_verification_response_provenance_verification_api_claims import (
            ProvenanceVerificationResponseProvenanceVerificationApiClaims,
        )
        from ..models.provenance_verification_response_provenance_verification_export_claims import (
            ProvenanceVerificationResponseProvenanceVerificationExportClaims,
        )

        d = src_dict.copy()
        valid = d.pop("valid")

        def _parse_claims(
            data: object,
        ) -> Union[
            "ProvenanceVerificationResponseProvenanceVerificationApiClaims",
            "ProvenanceVerificationResponseProvenanceVerificationExportClaims",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                claims_type_0 = ProvenanceVerificationResponseProvenanceVerificationApiClaims.from_dict(data)

                return claims_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            claims_type_1 = ProvenanceVerificationResponseProvenanceVerificationExportClaims.from_dict(data)

            return claims_type_1

        claims = _parse_claims(d.pop("claims", UNSET))

        ids_match = d.pop("idsMatch", UNSET)

        reason = d.pop("reason", UNSET)

        provenance_verification_response = cls(
            valid=valid,
            claims=claims,
            ids_match=ids_match,
            reason=reason,
        )

        return provenance_verification_response
