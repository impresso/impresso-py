from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.content_item_access_rights_copyright import ContentItemAccessRightsCopyright
from ..models.content_item_access_rights_data_domain import ContentItemAccessRightsDataDomain
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_item_access_bitmaps import ContentItemAccessBitmaps


T = TypeVar("T", bound="ContentItemAccessRights")


@_attrs_define
class ContentItemAccessRights:
    """Access rights information

    Attributes:
        data_domain (ContentItemAccessRightsDataDomain): Rights data domain. (e.g., 'pbl' for public, 'prt' for private)
        copyright_ (ContentItemAccessRightsCopyright): Copyright status.
        data_domain_label (Union[Unset, str]): Human-readable label for the dataDomain code.
        copyright_label (Union[Unset, str]): Human-readable label for the copyright code.
        access_bitmaps (Union[Unset, ContentItemAccessBitmaps]): Content item access bitmaps
    """

    data_domain: ContentItemAccessRightsDataDomain
    copyright_: ContentItemAccessRightsCopyright
    data_domain_label: Union[Unset, str] = UNSET
    copyright_label: Union[Unset, str] = UNSET
    access_bitmaps: Union[Unset, "ContentItemAccessBitmaps"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_domain = self.data_domain.value

        copyright_ = self.copyright_.value

        data_domain_label = self.data_domain_label

        copyright_label = self.copyright_label

        access_bitmaps: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.access_bitmaps, Unset):
            access_bitmaps = self.access_bitmaps.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataDomain": data_domain,
                "copyright": copyright_,
            }
        )
        if data_domain_label is not UNSET:
            field_dict["dataDomainLabel"] = data_domain_label
        if copyright_label is not UNSET:
            field_dict["copyrightLabel"] = copyright_label
        if access_bitmaps is not UNSET:
            field_dict["accessBitmaps"] = access_bitmaps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_item_access_bitmaps import ContentItemAccessBitmaps

        d = src_dict.copy()
        data_domain = ContentItemAccessRightsDataDomain(d.pop("dataDomain"))

        copyright_ = ContentItemAccessRightsCopyright(d.pop("copyright"))

        data_domain_label = d.pop("dataDomainLabel", UNSET)

        copyright_label = d.pop("copyrightLabel", UNSET)

        _access_bitmaps = d.pop("accessBitmaps", UNSET)
        access_bitmaps: Union[Unset, ContentItemAccessBitmaps]
        if isinstance(_access_bitmaps, Unset):
            access_bitmaps = UNSET
        else:
            access_bitmaps = ContentItemAccessBitmaps.from_dict(_access_bitmaps)

        content_item_access_rights = cls(
            data_domain=data_domain,
            copyright_=copyright_,
            data_domain_label=data_domain_label,
            copyright_label=copyright_label,
            access_bitmaps=access_bitmaps,
        )

        content_item_access_rights.additional_properties = d
        return content_item_access_rights

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
