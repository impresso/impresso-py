from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentItemNamedEntity")


@_attrs_define
class ContentItemNamedEntity:
    """Content item named entity

    Attributes:
        id (Union[Unset, str]): Unique identifier of the named entity
        count (Union[Unset, int]): Number of times this entity is mentioned in the content item
        label (Union[Unset, str]): The label of the named entity, e.g., a person's name or an organization
    """

    id: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    label: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        count = self.count

        label = self.label

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if count is not UNSET:
            field_dict["count"] = count
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        count = d.pop("count", UNSET)

        label = d.pop("label", UNSET)

        content_item_named_entity = cls(
            id=id,
            count=count,
            label=label,
        )

        return content_item_named_entity
