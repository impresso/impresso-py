from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentItemTextMatch")


@_attrs_define
class ContentItemTextMatch:
    """TODO

    Attributes:
        fragment (str): TODO
        coords (Union[Unset, List[float]]): TODO
        page_id (Union[Unset, str]): TODO
        iiif (Union[Unset, str]): TODO
    """

    fragment: str
    coords: Union[Unset, List[float]] = UNSET
    page_id: Union[Unset, str] = UNSET
    iiif: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        fragment = self.fragment

        coords: Union[Unset, List[float]] = UNSET
        if not isinstance(self.coords, Unset):
            coords = self.coords

        page_id = self.page_id

        iiif = self.iiif

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "fragment": fragment,
            }
        )
        if coords is not UNSET:
            field_dict["coords"] = coords
        if page_id is not UNSET:
            field_dict["pageId"] = page_id
        if iiif is not UNSET:
            field_dict["iiif"] = iiif

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fragment = d.pop("fragment")

        coords = cast(List[float], d.pop("coords", UNSET))

        page_id = d.pop("pageId", UNSET)

        iiif = d.pop("iiif", UNSET)

        content_item_text_match = cls(
            fragment=fragment,
            coords=coords,
            page_id=page_id,
            iiif=iiif,
        )

        return content_item_text_match
