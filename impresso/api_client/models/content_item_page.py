from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iiif_content_item_page_details import IIIFContentItemPageDetails


T = TypeVar("T", bound="ContentItemPage")


@_attrs_define
class ContentItemPage:
    """Content item page

    Attributes:
        id (Union[Unset, str]): Unique identifier of the page.
        number (Union[Unset, int]): The number of the page.
        region_coordinates (Union[Unset, List[List[int]]]): List of region coordinates.
        iiif (Union[Unset, IIIFContentItemPageDetails]): IIIF details for a content item page
    """

    id: Union[Unset, str] = UNSET
    number: Union[Unset, int] = UNSET
    region_coordinates: Union[Unset, List[List[int]]] = UNSET
    iiif: Union[Unset, "IIIFContentItemPageDetails"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        number = self.number

        region_coordinates: Union[Unset, List[List[int]]] = UNSET
        if not isinstance(self.region_coordinates, Unset):
            region_coordinates = []
            for region_coordinates_item_data in self.region_coordinates:
                region_coordinates_item = region_coordinates_item_data

                region_coordinates.append(region_coordinates_item)

        iiif: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.iiif, Unset):
            iiif = self.iiif.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if number is not UNSET:
            field_dict["number"] = number
        if region_coordinates is not UNSET:
            field_dict["regionCoordinates"] = region_coordinates
        if iiif is not UNSET:
            field_dict["iiif"] = iiif

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.iiif_content_item_page_details import IIIFContentItemPageDetails

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        number = d.pop("number", UNSET)

        region_coordinates = []
        _region_coordinates = d.pop("regionCoordinates", UNSET)
        for region_coordinates_item_data in _region_coordinates or []:
            region_coordinates_item = cast(List[int], region_coordinates_item_data)

            region_coordinates.append(region_coordinates_item)

        _iiif = d.pop("iiif", UNSET)
        iiif: Union[Unset, IIIFContentItemPageDetails]
        if isinstance(_iiif, Unset):
            iiif = UNSET
        else:
            iiif = IIIFContentItemPageDetails.from_dict(_iiif)

        content_item_page = cls(
            id=id,
            number=number,
            region_coordinates=region_coordinates,
            iiif=iiif,
        )

        return content_item_page
