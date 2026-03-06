from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentItemAudioLocator")


@_attrs_define
class ContentItemAudioLocator:
    """Content item audio locator. Links location of a segement in text with location in audio.

    Attributes:
        time_code (Union[Unset, List[float]]): Represents the start offset and the length of the audio segment in
            seconds.
        text_location (Union[Unset, List[int]]): Represents the character offset and length of the audio segment in the
            content item text.
        utterance_index (Union[Unset, int]): Represents the index of the utterance in the audio file this audio segment
            belongs to. May not be provided if no utterance information is available.
    """

    time_code: Union[Unset, List[float]] = UNSET
    text_location: Union[Unset, List[int]] = UNSET
    utterance_index: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        time_code: Union[Unset, List[float]] = UNSET
        if not isinstance(self.time_code, Unset):
            time_code = self.time_code

        text_location: Union[Unset, List[int]] = UNSET
        if not isinstance(self.text_location, Unset):
            text_location = self.text_location

        utterance_index = self.utterance_index

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if time_code is not UNSET:
            field_dict["timeCode"] = time_code
        if text_location is not UNSET:
            field_dict["textLocation"] = text_location
        if utterance_index is not UNSET:
            field_dict["utteranceIndex"] = utterance_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time_code = cast(List[float], d.pop("timeCode", UNSET))

        text_location = cast(List[int], d.pop("textLocation", UNSET))

        utterance_index = d.pop("utteranceIndex", UNSET)

        content_item_audio_locator = cls(
            time_code=time_code,
            text_location=text_location,
            utterance_index=utterance_index,
        )

        return content_item_audio_locator
