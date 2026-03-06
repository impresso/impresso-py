from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="IIIFContentItemPageDetails")


@_attrs_define
class IIIFContentItemPageDetails:
    """IIIF details for a content item page

    Attributes:
        manifest_url (str): The URL of the IIIF manifest for the page.
        thumbnail_url (str): The URL of the thumbnail image for the page.
    """

    manifest_url: str
    thumbnail_url: str

    def to_dict(self) -> Dict[str, Any]:
        manifest_url = self.manifest_url

        thumbnail_url = self.thumbnail_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "manifestUrl": manifest_url,
                "thumbnailUrl": thumbnail_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        manifest_url = d.pop("manifestUrl")

        thumbnail_url = d.pop("thumbnailUrl")

        iiif_content_item_page_details = cls(
            manifest_url=manifest_url,
            thumbnail_url=thumbnail_url,
        )

        return iiif_content_item_page_details
