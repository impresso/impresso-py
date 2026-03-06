from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_item_audio_locator import ContentItemAudioLocator


T = TypeVar("T", bound="ContentItemAudioRecord")


@_attrs_define
class ContentItemAudioRecord:
    """Content item audio record

    Attributes:
        id (Union[Unset, str]): Unique identifier of the audio record.
        number (Union[Unset, int]): The number of the audio record.
        audio_segments_locators (Union[Unset, List['ContentItemAudioLocator']]): A list of audio segments locators.
        audio_file_url (Union[Unset, str]): The URL of the audio file.
    """

    id: Union[Unset, str] = UNSET
    number: Union[Unset, int] = UNSET
    audio_segments_locators: Union[Unset, List["ContentItemAudioLocator"]] = UNSET
    audio_file_url: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        number = self.number

        audio_segments_locators: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.audio_segments_locators, Unset):
            audio_segments_locators = []
            for audio_segments_locators_item_data in self.audio_segments_locators:
                audio_segments_locators_item = audio_segments_locators_item_data.to_dict()
                audio_segments_locators.append(audio_segments_locators_item)

        audio_file_url = self.audio_file_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if number is not UNSET:
            field_dict["number"] = number
        if audio_segments_locators is not UNSET:
            field_dict["audioSegmentsLocators"] = audio_segments_locators
        if audio_file_url is not UNSET:
            field_dict["audioFileUrl"] = audio_file_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_item_audio_locator import ContentItemAudioLocator

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        number = d.pop("number", UNSET)

        audio_segments_locators = []
        _audio_segments_locators = d.pop("audioSegmentsLocators", UNSET)
        for audio_segments_locators_item_data in _audio_segments_locators or []:
            audio_segments_locators_item = ContentItemAudioLocator.from_dict(audio_segments_locators_item_data)

            audio_segments_locators.append(audio_segments_locators_item)

        audio_file_url = d.pop("audioFileUrl", UNSET)

        content_item_audio_record = cls(
            id=id,
            number=number,
            audio_segments_locators=audio_segments_locators,
            audio_file_url=audio_file_url,
        )

        return content_item_audio_record
