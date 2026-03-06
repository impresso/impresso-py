from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentItemTopic")


@_attrs_define
class ContentItemTopic:
    """Topic associated with a content item.

    Attributes:
        relevance (float): Relevance score of the topic in the content item, typically between 0 and 1, where 1
            indicates high relevance.
        id (str): Unique identifier of the topic.
        label (Union[Unset, str]): Human-readable label of the topic.
        language_code (Union[Unset, str]): Language code of the topic, following ISO 639-1 standards.
    """

    relevance: float
    id: str
    label: Union[Unset, str] = UNSET
    language_code: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        relevance = self.relevance

        id = self.id

        label = self.label

        language_code = self.language_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "relevance": relevance,
                "id": id,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        relevance = d.pop("relevance")

        id = d.pop("id")

        label = d.pop("label", UNSET)

        language_code = d.pop("languageCode", UNSET)

        content_item_topic = cls(
            relevance=relevance,
            id=id,
            label=label,
            language_code=language_code,
        )

        return content_item_topic
