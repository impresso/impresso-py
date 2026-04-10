from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_item_page import ContentItemPage


T = TypeVar("T", bound="ContentItemFacsimile")


@_attrs_define
class ContentItemFacsimile:
    """Facsimile-related information for digitized content

    Attributes:
        pages_count (Union[Unset, int]): Total number of pages in the content item.
        is_front_page (Union[Unset, bool]): Indicates if the content item is on the front page.
        is_coordinates_converted (Union[Unset, bool]): Indicates whether coordinates were converted.
        pages (Union[Unset, List['ContentItemPage']]): List of pages this content item is on.
        line_breaks (Union[Unset, List[int]]): List of line breaks offsets in the content item (relative to textual
            content).
        paragraph_breaks (Union[Unset, List[int]]): List of paragraph breaks offsets in the content item (relative to
            textual content).
        region_breaks (Union[Unset, List[int]]): List of region breaks offsets in the content item (relative to textual
            content).
    """

    pages_count: Union[Unset, int] = UNSET
    is_front_page: Union[Unset, bool] = UNSET
    is_coordinates_converted: Union[Unset, bool] = UNSET
    pages: Union[Unset, List["ContentItemPage"]] = UNSET
    line_breaks: Union[Unset, List[int]] = UNSET
    paragraph_breaks: Union[Unset, List[int]] = UNSET
    region_breaks: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pages_count = self.pages_count

        is_front_page = self.is_front_page

        is_coordinates_converted = self.is_coordinates_converted

        pages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pages, Unset):
            pages = []
            for pages_item_data in self.pages:
                pages_item = pages_item_data.to_dict()
                pages.append(pages_item)

        line_breaks: Union[Unset, List[int]] = UNSET
        if not isinstance(self.line_breaks, Unset):
            line_breaks = self.line_breaks

        paragraph_breaks: Union[Unset, List[int]] = UNSET
        if not isinstance(self.paragraph_breaks, Unset):
            paragraph_breaks = self.paragraph_breaks

        region_breaks: Union[Unset, List[int]] = UNSET
        if not isinstance(self.region_breaks, Unset):
            region_breaks = self.region_breaks

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pages_count is not UNSET:
            field_dict["pagesCount"] = pages_count
        if is_front_page is not UNSET:
            field_dict["isFrontPage"] = is_front_page
        if is_coordinates_converted is not UNSET:
            field_dict["isCoordinatesConverted"] = is_coordinates_converted
        if pages is not UNSET:
            field_dict["pages"] = pages
        if line_breaks is not UNSET:
            field_dict["lineBreaks"] = line_breaks
        if paragraph_breaks is not UNSET:
            field_dict["paragraphBreaks"] = paragraph_breaks
        if region_breaks is not UNSET:
            field_dict["regionBreaks"] = region_breaks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_item_page import ContentItemPage

        d = src_dict.copy()
        pages_count = d.pop("pagesCount", UNSET)

        is_front_page = d.pop("isFrontPage", UNSET)

        is_coordinates_converted = d.pop("isCoordinatesConverted", UNSET)

        pages = []
        _pages = d.pop("pages", UNSET)
        for pages_item_data in _pages or []:
            pages_item = ContentItemPage.from_dict(pages_item_data)

            pages.append(pages_item)

        line_breaks = cast(List[int], d.pop("lineBreaks", UNSET))

        paragraph_breaks = cast(List[int], d.pop("paragraphBreaks", UNSET))

        region_breaks = cast(List[int], d.pop("regionBreaks", UNSET))

        content_item_facsimile = cls(
            pages_count=pages_count,
            is_front_page=is_front_page,
            is_coordinates_converted=is_coordinates_converted,
            pages=pages,
            line_breaks=line_breaks,
            paragraph_breaks=paragraph_breaks,
            region_breaks=region_breaks,
        )

        content_item_facsimile.additional_properties = d
        return content_item_facsimile

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
