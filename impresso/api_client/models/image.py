import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_image_types import ImageImageTypes
    from ..models.image_media_source_ref import ImageMediaSourceRef


T = TypeVar("T", bound="Image")


@_attrs_define
class Image:
    """An image from a content item

    Attributes:
        uid (str): The unique identifier of the image
        issue_uid (str): The unique identifier of the issue that the image belongs to.
        preview_url (str): The URL of the image preview
        media_source_ref (ImageMediaSourceRef): The media source of the image
        date (datetime.date): The date of the image or the date of the issue that the image belongs to.
        caption (Union[Unset, str]): Image caption
        content_item_uid (Union[Unset, str]): The unique identifier of the content item that the image belongs to.
        page_numbers (Union[Unset, List[int]]): The page numbers of the issue that the image belongs to.
        image_types (Union[Unset, ImageImageTypes]):
        embeddings (Union[Unset, List[str]]): Precomputed embeddings for the image in the format:
            <model_type>:<base64_embedding_vector>.
    """

    uid: str
    issue_uid: str
    preview_url: str
    media_source_ref: "ImageMediaSourceRef"
    date: datetime.date
    caption: Union[Unset, str] = UNSET
    content_item_uid: Union[Unset, str] = UNSET
    page_numbers: Union[Unset, List[int]] = UNSET
    image_types: Union[Unset, "ImageImageTypes"] = UNSET
    embeddings: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uid = self.uid

        issue_uid = self.issue_uid

        preview_url = self.preview_url

        media_source_ref = self.media_source_ref.to_dict()

        date = self.date.isoformat()

        caption = self.caption

        content_item_uid = self.content_item_uid

        page_numbers: Union[Unset, List[int]] = UNSET
        if not isinstance(self.page_numbers, Unset):
            page_numbers = self.page_numbers

        image_types: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image_types, Unset):
            image_types = self.image_types.to_dict()

        embeddings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.embeddings, Unset):
            embeddings = self.embeddings

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "uid": uid,
                "issueUid": issue_uid,
                "previewUrl": preview_url,
                "mediaSourceRef": media_source_ref,
                "date": date,
            }
        )
        if caption is not UNSET:
            field_dict["caption"] = caption
        if content_item_uid is not UNSET:
            field_dict["contentItemUid"] = content_item_uid
        if page_numbers is not UNSET:
            field_dict["pageNumbers"] = page_numbers
        if image_types is not UNSET:
            field_dict["imageTypes"] = image_types
        if embeddings is not UNSET:
            field_dict["embeddings"] = embeddings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_image_types import ImageImageTypes
        from ..models.image_media_source_ref import ImageMediaSourceRef

        d = src_dict.copy()
        uid = d.pop("uid")

        issue_uid = d.pop("issueUid")

        preview_url = d.pop("previewUrl")

        media_source_ref = ImageMediaSourceRef.from_dict(d.pop("mediaSourceRef"))

        date = isoparse(d.pop("date")).date()

        caption = d.pop("caption", UNSET)

        content_item_uid = d.pop("contentItemUid", UNSET)

        page_numbers = cast(List[int], d.pop("pageNumbers", UNSET))

        _image_types = d.pop("imageTypes", UNSET)
        image_types: Union[Unset, ImageImageTypes]
        if isinstance(_image_types, Unset):
            image_types = UNSET
        else:
            image_types = ImageImageTypes.from_dict(_image_types)

        embeddings = cast(List[str], d.pop("embeddings", UNSET))

        image = cls(
            uid=uid,
            issue_uid=issue_uid,
            preview_url=preview_url,
            media_source_ref=media_source_ref,
            date=date,
            caption=caption,
            content_item_uid=content_item_uid,
            page_numbers=page_numbers,
            image_types=image_types,
            embeddings=embeddings,
        )

        return image
