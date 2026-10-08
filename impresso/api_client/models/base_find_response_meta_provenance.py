from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BaseFindResponseMetaProvenance")


@_attrs_define
class BaseFindResponseMetaProvenance:
    """
    Attributes:
        token (str):
        kid (str):
    """

    token: str
    kid: str

    def to_dict(self) -> Dict[str, Any]:
        token = self.token

        kid = self.kid

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "token": token,
                "kid": kid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token")

        kid = d.pop("kid")

        base_find_response_meta_provenance = cls(
            token=token,
            kid=kid,
        )

        return base_find_response_meta_provenance
