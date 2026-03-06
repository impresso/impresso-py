from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_item_audio_record import ContentItemAudioRecord


T = TypeVar("T", bound="ContentItemAudio")


@_attrs_define
class ContentItemAudio:
    """Audio-related information for broadcast content

    Attributes:
        start_time (Union[Unset, str]): Start time of media in HH:MM:SS format (relative to the day of broadcast).
        duration (Union[Unset, str]): Duration of the radio broadcast in HH:MM:SS format (relative to the start of the
            broadcast on the given broadcast day).
        records (Union[Unset, List['ContentItemAudioRecord']]): Array of records
        records_count (Union[Unset, int]): Total number of records/segments in the radio broadcast
    """

    start_time: Union[Unset, str] = UNSET
    duration: Union[Unset, str] = UNSET
    records: Union[Unset, List["ContentItemAudioRecord"]] = UNSET
    records_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_time = self.start_time

        duration = self.duration

        records: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item = records_item_data.to_dict()
                records.append(records_item)

        records_count = self.records_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if duration is not UNSET:
            field_dict["duration"] = duration
        if records is not UNSET:
            field_dict["records"] = records
        if records_count is not UNSET:
            field_dict["recordsCount"] = records_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_item_audio_record import ContentItemAudioRecord

        d = src_dict.copy()
        start_time = d.pop("startTime", UNSET)

        duration = d.pop("duration", UNSET)

        records = []
        _records = d.pop("records", UNSET)
        for records_item_data in _records or []:
            records_item = ContentItemAudioRecord.from_dict(records_item_data)

            records.append(records_item)

        records_count = d.pop("recordsCount", UNSET)

        content_item_audio = cls(
            start_time=start_time,
            duration=duration,
            records=records,
            records_count=records_count,
        )

        content_item_audio.additional_properties = d
        return content_item_audio

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
