from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_get_response_cache_counts import AdminGETResponseCacheCounts
    from ..models.admin_get_response_content_items_permissions_details import (
        AdminGETResponseContentItemsPermissionsDetails,
    )
    from ..models.admin_get_response_images_permissions_details import AdminGETResponseImagesPermissionsDetails
    from ..models.admin_get_response_patch_result import AdminGETResponsePatchResult
    from ..models.admin_get_response_user_accounts_item import AdminGETResponseUserAccountsItem
    from ..models.admin_get_response_well_known_computed_at import AdminGETResponseWellKnownComputedAt


T = TypeVar("T", bound="AdminGETResponse")


@_attrs_define
class AdminGETResponse:
    """Admin service GET response.

    Attributes:
        content_items_permissions_details (Union[Unset, AdminGETResponseContentItemsPermissionsDetails]):
        images_permissions_details (Union[Unset, AdminGETResponseImagesPermissionsDetails]):
        user_accounts (Union[Unset, List['AdminGETResponseUserAccountsItem']]):
        cache_counts (Union[Unset, AdminGETResponseCacheCounts]):
        well_known_computed_at (Union[Unset, AdminGETResponseWellKnownComputedAt]):
        patch_result (Union[Unset, AdminGETResponsePatchResult]):
    """

    content_items_permissions_details: Union[Unset, "AdminGETResponseContentItemsPermissionsDetails"] = UNSET
    images_permissions_details: Union[Unset, "AdminGETResponseImagesPermissionsDetails"] = UNSET
    user_accounts: Union[Unset, List["AdminGETResponseUserAccountsItem"]] = UNSET
    cache_counts: Union[Unset, "AdminGETResponseCacheCounts"] = UNSET
    well_known_computed_at: Union[Unset, "AdminGETResponseWellKnownComputedAt"] = UNSET
    patch_result: Union[Unset, "AdminGETResponsePatchResult"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_items_permissions_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.content_items_permissions_details, Unset):
            content_items_permissions_details = self.content_items_permissions_details.to_dict()

        images_permissions_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images_permissions_details, Unset):
            images_permissions_details = self.images_permissions_details.to_dict()

        user_accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user_accounts, Unset):
            user_accounts = []
            for user_accounts_item_data in self.user_accounts:
                user_accounts_item = user_accounts_item_data.to_dict()
                user_accounts.append(user_accounts_item)

        cache_counts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cache_counts, Unset):
            cache_counts = self.cache_counts.to_dict()

        well_known_computed_at: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.well_known_computed_at, Unset):
            well_known_computed_at = self.well_known_computed_at.to_dict()

        patch_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.patch_result, Unset):
            patch_result = self.patch_result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_items_permissions_details is not UNSET:
            field_dict["contentItemsPermissionsDetails"] = content_items_permissions_details
        if images_permissions_details is not UNSET:
            field_dict["imagesPermissionsDetails"] = images_permissions_details
        if user_accounts is not UNSET:
            field_dict["userAccounts"] = user_accounts
        if cache_counts is not UNSET:
            field_dict["cacheCounts"] = cache_counts
        if well_known_computed_at is not UNSET:
            field_dict["wellKnownComputedAt"] = well_known_computed_at
        if patch_result is not UNSET:
            field_dict["patchResult"] = patch_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.admin_get_response_cache_counts import AdminGETResponseCacheCounts
        from ..models.admin_get_response_content_items_permissions_details import (
            AdminGETResponseContentItemsPermissionsDetails,
        )
        from ..models.admin_get_response_images_permissions_details import AdminGETResponseImagesPermissionsDetails
        from ..models.admin_get_response_patch_result import AdminGETResponsePatchResult
        from ..models.admin_get_response_user_accounts_item import AdminGETResponseUserAccountsItem
        from ..models.admin_get_response_well_known_computed_at import AdminGETResponseWellKnownComputedAt

        d = src_dict.copy()
        _content_items_permissions_details = d.pop("contentItemsPermissionsDetails", UNSET)
        content_items_permissions_details: Union[Unset, AdminGETResponseContentItemsPermissionsDetails]
        if isinstance(_content_items_permissions_details, Unset):
            content_items_permissions_details = UNSET
        else:
            content_items_permissions_details = AdminGETResponseContentItemsPermissionsDetails.from_dict(
                _content_items_permissions_details
            )

        _images_permissions_details = d.pop("imagesPermissionsDetails", UNSET)
        images_permissions_details: Union[Unset, AdminGETResponseImagesPermissionsDetails]
        if isinstance(_images_permissions_details, Unset):
            images_permissions_details = UNSET
        else:
            images_permissions_details = AdminGETResponseImagesPermissionsDetails.from_dict(_images_permissions_details)

        user_accounts = []
        _user_accounts = d.pop("userAccounts", UNSET)
        for user_accounts_item_data in _user_accounts or []:
            user_accounts_item = AdminGETResponseUserAccountsItem.from_dict(user_accounts_item_data)

            user_accounts.append(user_accounts_item)

        _cache_counts = d.pop("cacheCounts", UNSET)
        cache_counts: Union[Unset, AdminGETResponseCacheCounts]
        if isinstance(_cache_counts, Unset):
            cache_counts = UNSET
        else:
            cache_counts = AdminGETResponseCacheCounts.from_dict(_cache_counts)

        _well_known_computed_at = d.pop("wellKnownComputedAt", UNSET)
        well_known_computed_at: Union[Unset, AdminGETResponseWellKnownComputedAt]
        if isinstance(_well_known_computed_at, Unset):
            well_known_computed_at = UNSET
        else:
            well_known_computed_at = AdminGETResponseWellKnownComputedAt.from_dict(_well_known_computed_at)

        _patch_result = d.pop("patchResult", UNSET)
        patch_result: Union[Unset, AdminGETResponsePatchResult]
        if isinstance(_patch_result, Unset):
            patch_result = UNSET
        else:
            patch_result = AdminGETResponsePatchResult.from_dict(_patch_result)

        admin_get_response = cls(
            content_items_permissions_details=content_items_permissions_details,
            images_permissions_details=images_permissions_details,
            user_accounts=user_accounts,
            cache_counts=cache_counts,
            well_known_computed_at=well_known_computed_at,
            patch_result=patch_result,
        )

        admin_get_response.additional_properties = d
        return admin_get_response

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
