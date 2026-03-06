from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.admin_patch_request_action import AdminPatchRequestAction

T = TypeVar("T", bound="AdminPatchRequest")


@_attrs_define
class AdminPatchRequest:
    """Admin maintenance action request.

    Attributes:
        action (AdminPatchRequestAction):
    """

    action: AdminPatchRequestAction

    def to_dict(self) -> Dict[str, Any]:
        action = self.action.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action = AdminPatchRequestAction(d.pop("action"))

        admin_patch_request = cls(
            action=action,
        )

        return admin_patch_request
