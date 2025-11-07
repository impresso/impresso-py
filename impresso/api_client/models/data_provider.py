from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.data_provider_names_item import DataProviderNamesItem


T = TypeVar("T", bound="DataProvider")


@_attrs_define
class DataProvider:
    """A data provider is a partner institution that provides content to Impresso (e.g., libraries, archives, media
    organizations).

        Attributes:
            id (str): The unique identifier of the data provider.
            names (List['DataProviderNamesItem']): Names of the data provider in different languages.
    """

    id: str
    names: List["DataProviderNamesItem"]

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        names = []
        for names_item_data in self.names:
            names_item = names_item_data.to_dict()
            names.append(names_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "names": names,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_provider_names_item import DataProviderNamesItem

        d = src_dict.copy()
        id = d.pop("id")

        names = []
        _names = d.pop("names")
        for names_item_data in _names:
            names_item = DataProviderNamesItem.from_dict(names_item_data)

            names.append(names_item)

        data_provider = cls(
            id=id,
            names=names,
        )

        return data_provider
