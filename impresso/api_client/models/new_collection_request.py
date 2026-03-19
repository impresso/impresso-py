from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.new_collection_request_access_level import NewCollectionRequestAccessLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewCollectionRequest")


@_attrs_define
class NewCollectionRequest:
    """Create new collection request

    Attributes:
        title (str):
        description (Union[Unset, str]):
        access_level (Union[Unset, NewCollectionRequestAccessLevel]): Access level of the collection.
    """

    title: str
    description: Union[Unset, str] = UNSET
    access_level: Union[Unset, NewCollectionRequestAccessLevel] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        description = self.description

        access_level: Union[Unset, str] = UNSET
        if not isinstance(self.access_level, Unset):
            access_level = self.access_level.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if access_level is not UNSET:
            field_dict["accessLevel"] = access_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        description = d.pop("description", UNSET)

        _access_level = d.pop("accessLevel", UNSET)
        access_level: Union[Unset, NewCollectionRequestAccessLevel]
        if isinstance(_access_level, Unset):
            access_level = UNSET
        else:
            access_level = NewCollectionRequestAccessLevel(_access_level)

        new_collection_request = cls(
            title=title,
            description=description,
            access_level=access_level,
        )

        return new_collection_request
