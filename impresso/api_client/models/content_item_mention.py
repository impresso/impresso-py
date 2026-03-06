from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentItemMention")


@_attrs_define
class ContentItemMention:
    """Content item mention

    Attributes:
        surface_form (Union[Unset, str]): The surface form (label) of the entity mention
        mention_confidence (Union[Unset, float]): Confidence score of the entity mention
        start_offset (Union[Unset, int]): Start offset of the entity mention in the content item
        end_offset (Union[Unset, int]): End offset of the entity mention in the content item
    """

    surface_form: Union[Unset, str] = UNSET
    mention_confidence: Union[Unset, float] = UNSET
    start_offset: Union[Unset, int] = UNSET
    end_offset: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        surface_form = self.surface_form

        mention_confidence = self.mention_confidence

        start_offset = self.start_offset

        end_offset = self.end_offset

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if surface_form is not UNSET:
            field_dict["surfaceForm"] = surface_form
        if mention_confidence is not UNSET:
            field_dict["mentionConfidence"] = mention_confidence
        if start_offset is not UNSET:
            field_dict["startOffset"] = start_offset
        if end_offset is not UNSET:
            field_dict["endOffset"] = end_offset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        surface_form = d.pop("surfaceForm", UNSET)

        mention_confidence = d.pop("mentionConfidence", UNSET)

        start_offset = d.pop("startOffset", UNSET)

        end_offset = d.pop("endOffset", UNSET)

        content_item_mention = cls(
            surface_form=surface_form,
            mention_confidence=mention_confidence,
            start_offset=start_offset,
            end_offset=end_offset,
        )

        return content_item_mention
