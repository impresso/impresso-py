from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Entity")


@_attrs_define
class Entity:
    """An entity like location, person, etc

    Attributes:
        id (str): Unique identifier of the entity
        relevance (int): Relevance of the entity in the document
        name (Union[Unset, str]): Name of the entity
    """

    id: str
    relevance: int
    name: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        relevance = self.relevance

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "relevance": relevance,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        relevance = d.pop("relevance")

        name = d.pop("name", UNSET)

        entity = cls(
            id=id,
            relevance=relevance,
            name=name,
        )

        return entity
