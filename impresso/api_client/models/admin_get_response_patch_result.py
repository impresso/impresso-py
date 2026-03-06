from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_get_response_patch_result_cleared import AdminGETResponsePatchResultCleared


T = TypeVar("T", bound="AdminGETResponsePatchResult")


@_attrs_define
class AdminGETResponsePatchResult:
    """
    Attributes:
        action (str):
        cleared (Union[Unset, AdminGETResponsePatchResultCleared]):
        job_id (Union[Unset, str]):
    """

    action: str
    cleared: Union[Unset, "AdminGETResponsePatchResultCleared"] = UNSET
    job_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action

        cleared: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cleared, Unset):
            cleared = self.cleared.to_dict()

        job_id = self.job_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )
        if cleared is not UNSET:
            field_dict["cleared"] = cleared
        if job_id is not UNSET:
            field_dict["jobId"] = job_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.admin_get_response_patch_result_cleared import AdminGETResponsePatchResultCleared

        d = src_dict.copy()
        action = d.pop("action")

        _cleared = d.pop("cleared", UNSET)
        cleared: Union[Unset, AdminGETResponsePatchResultCleared]
        if isinstance(_cleared, Unset):
            cleared = UNSET
        else:
            cleared = AdminGETResponsePatchResultCleared.from_dict(_cleared)

        job_id = d.pop("jobId", UNSET)

        admin_get_response_patch_result = cls(
            action=action,
            cleared=cleared,
            job_id=job_id,
        )

        admin_get_response_patch_result.additional_properties = d
        return admin_get_response_patch_result

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
