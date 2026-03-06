from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.full_version_details_partner_institutions_item_names_item import (
        FullVersionDetailsPartnerInstitutionsItemNamesItem,
    )


T = TypeVar("T", bound="FullVersionDetailsPartnerInstitutionsItem")


@_attrs_define
class FullVersionDetailsPartnerInstitutionsItem:
    """
    Attributes:
        id (str):
        names (List['FullVersionDetailsPartnerInstitutionsItemNamesItem']):
        bitmap_index (int):
    """

    id: str
    names: List["FullVersionDetailsPartnerInstitutionsItemNamesItem"]
    bitmap_index: int

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        names = []
        for names_item_data in self.names:
            names_item = names_item_data.to_dict()
            names.append(names_item)

        bitmap_index = self.bitmap_index

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "names": names,
                "bitmapIndex": bitmap_index,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.full_version_details_partner_institutions_item_names_item import (
            FullVersionDetailsPartnerInstitutionsItemNamesItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        names = []
        _names = d.pop("names")
        for names_item_data in _names:
            names_item = FullVersionDetailsPartnerInstitutionsItemNamesItem.from_dict(names_item_data)

            names.append(names_item)

        bitmap_index = d.pop("bitmapIndex")

        full_version_details_partner_institutions_item = cls(
            id=id,
            names=names,
            bitmap_index=bitmap_index,
        )

        return full_version_details_partner_institutions_item
