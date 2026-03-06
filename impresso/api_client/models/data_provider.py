from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_provider_names_item import DataProviderNamesItem


T = TypeVar("T", bound="DataProvider")


@_attrs_define
class DataProvider:
    """A data provider is a partner institution that provides content to Impresso (e.g., libraries, archives, media
    organizations).

        Attributes:
            id (str): The unique identifier of the data provider.
            name (str): The default name of the data provider.
            names (List['DataProviderNamesItem']): Names of the data provider in different languages.
            bitmap_index (Union[Unset, int]): Bitmap index used for efficient data provider filtering.
    """

    id: str
    name: str
    names: List["DataProviderNamesItem"]
    bitmap_index: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        names = []
        for names_item_data in self.names:
            names_item = names_item_data.to_dict()
            names.append(names_item)

        bitmap_index = self.bitmap_index

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
                "names": names,
            }
        )
        if bitmap_index is not UNSET:
            field_dict["bitmapIndex"] = bitmap_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_provider_names_item import DataProviderNamesItem

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        names = []
        _names = d.pop("names")
        for names_item_data in _names:
            names_item = DataProviderNamesItem.from_dict(names_item_data)

            names.append(names_item)

        bitmap_index = d.pop("bitmapIndex", UNSET)

        data_provider = cls(
            id=id,
            name=name,
            names=names,
            bitmap_index=bitmap_index,
        )

        return data_provider
