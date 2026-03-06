from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="FullVersionDetailsPartnerInstitutionsItemNamesItem")


@_attrs_define
class FullVersionDetailsPartnerInstitutionsItemNamesItem:
    """
    Attributes:
        lang_code (str):
        name (str):
    """

    lang_code: str
    name: str

    def to_dict(self) -> Dict[str, Any]:
        lang_code = self.lang_code

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "langCode": lang_code,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lang_code = d.pop("langCode")

        name = d.pop("name")

        full_version_details_partner_institutions_item_names_item = cls(
            lang_code=lang_code,
            name=name,
        )

        return full_version_details_partner_institutions_item_names_item
