from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AdminGETResponsePatchResultCleared")


@_attrs_define
class AdminGETResponsePatchResultCleared:
    """
    Attributes:
        count (int):
    """

    count: int

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count")

        admin_get_response_patch_result_cleared = cls(
            count=count,
        )

        return admin_get_response_patch_result_cleared
