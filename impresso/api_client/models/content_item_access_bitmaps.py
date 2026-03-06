from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentItemAccessBitmaps")


@_attrs_define
class ContentItemAccessBitmaps:
    """Content item access bitmaps

    Attributes:
        explore (Union[Unset, str]): Bitmap for explore access. As bytes.
        get_transcript (Union[Unset, str]): Bitmap for get transcript access. As bytes.
        get_images (Union[Unset, str]): Bitmap for get images access. As bytes.
        get_audio (Union[Unset, str]): Bitmap for get audio access. As bytes.
    """

    explore: Union[Unset, str] = UNSET
    get_transcript: Union[Unset, str] = UNSET
    get_images: Union[Unset, str] = UNSET
    get_audio: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        explore = self.explore

        get_transcript = self.get_transcript

        get_images = self.get_images

        get_audio = self.get_audio

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if explore is not UNSET:
            field_dict["explore"] = explore
        if get_transcript is not UNSET:
            field_dict["getTranscript"] = get_transcript
        if get_images is not UNSET:
            field_dict["getImages"] = get_images
        if get_audio is not UNSET:
            field_dict["getAudio"] = get_audio

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        explore = d.pop("explore", UNSET)

        get_transcript = d.pop("getTranscript", UNSET)

        get_images = d.pop("getImages", UNSET)

        get_audio = d.pop("getAudio", UNSET)

        content_item_access_bitmaps = cls(
            explore=explore,
            get_transcript=get_transcript,
            get_images=get_images,
            get_audio=get_audio,
        )

        return content_item_access_bitmaps
