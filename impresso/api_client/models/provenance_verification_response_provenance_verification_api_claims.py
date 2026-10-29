from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.provenance_verification_response_provenance_verification_api_claims_kind import (
    ProvenanceVerificationResponseProvenanceVerificationApiClaimsKind,
)

T = TypeVar("T", bound="ProvenanceVerificationResponseProvenanceVerificationApiClaims")


@_attrs_define
class ProvenanceVerificationResponseProvenanceVerificationApiClaims:
    """
    Attributes:
        iss (str):
        aud (str):
        iat (float):
        jti (str):
        user_ref (str):
        kind (ProvenanceVerificationResponseProvenanceVerificationApiClaimsKind):
        path (str):
        ids_hash (str):
        ids_count (int):
    """

    iss: str
    aud: str
    iat: float
    jti: str
    user_ref: str
    kind: ProvenanceVerificationResponseProvenanceVerificationApiClaimsKind
    path: str
    ids_hash: str
    ids_count: int

    def to_dict(self) -> Dict[str, Any]:
        iss = self.iss

        aud = self.aud

        iat = self.iat

        jti = self.jti

        user_ref = self.user_ref

        kind = self.kind.value

        path = self.path

        ids_hash = self.ids_hash

        ids_count = self.ids_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "iss": iss,
                "aud": aud,
                "iat": iat,
                "jti": jti,
                "userRef": user_ref,
                "kind": kind,
                "path": path,
                "idsHash": ids_hash,
                "idsCount": ids_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        iss = d.pop("iss")

        aud = d.pop("aud")

        iat = d.pop("iat")

        jti = d.pop("jti")

        user_ref = d.pop("userRef")

        kind = ProvenanceVerificationResponseProvenanceVerificationApiClaimsKind(d.pop("kind"))

        path = d.pop("path")

        ids_hash = d.pop("idsHash")

        ids_count = d.pop("idsCount")

        provenance_verification_response_provenance_verification_api_claims = cls(
            iss=iss,
            aud=aud,
            iat=iat,
            jti=jti,
            user_ref=user_ref,
            kind=kind,
            path=path,
            ids_hash=ids_hash,
            ids_count=ids_count,
        )

        return provenance_verification_response_provenance_verification_api_claims
