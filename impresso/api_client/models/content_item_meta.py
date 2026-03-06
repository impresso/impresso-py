import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.content_item_meta_source_medium import ContentItemMetaSourceMedium
from ..models.content_item_meta_source_type import ContentItemMetaSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentItemMeta")


@_attrs_define
class ContentItemMeta:
    """Content Item metadata

    Attributes:
        source_type (ContentItemMetaSourceType): Type of the media source.
        source_medium (ContentItemMetaSourceMedium): Medium of the source (audio for audio radio broadcasts, print for
            newspapers, typescript for digitised radio bulletin typescripts).
        date (datetime.datetime): Full date and time in ISO 8601 format
        media_id (Union[Unset, str]): Media title alias. Usually a 3 letter code of the media title (newspaper, radio
            station, etc.).
        media_title (Union[Unset, str]): Human-readable title of the media source identified by mediaId.
        partner_id (Union[Unset, str]): Identifier of the partner providing the content item.
        partner_title (Union[Unset, str]): Human-readable title of the partner identified by partnerId.
        country_code (Union[Unset, str]): Country code of the content item.
        province_code (Union[Unset, str]): Province code of the content item.
    """

    source_type: ContentItemMetaSourceType
    source_medium: ContentItemMetaSourceMedium
    date: datetime.datetime
    media_id: Union[Unset, str] = UNSET
    media_title: Union[Unset, str] = UNSET
    partner_id: Union[Unset, str] = UNSET
    partner_title: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    province_code: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        source_type = self.source_type.value

        source_medium = self.source_medium.value

        date = self.date.isoformat()

        media_id = self.media_id

        media_title = self.media_title

        partner_id = self.partner_id

        partner_title = self.partner_title

        country_code = self.country_code

        province_code = self.province_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "sourceType": source_type,
                "sourceMedium": source_medium,
                "date": date,
            }
        )
        if media_id is not UNSET:
            field_dict["mediaId"] = media_id
        if media_title is not UNSET:
            field_dict["mediaTitle"] = media_title
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if partner_title is not UNSET:
            field_dict["partnerTitle"] = partner_title
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if province_code is not UNSET:
            field_dict["provinceCode"] = province_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_type = ContentItemMetaSourceType(d.pop("sourceType"))

        source_medium = ContentItemMetaSourceMedium(d.pop("sourceMedium"))

        date = isoparse(d.pop("date"))

        media_id = d.pop("mediaId", UNSET)

        media_title = d.pop("mediaTitle", UNSET)

        partner_id = d.pop("partnerId", UNSET)

        partner_title = d.pop("partnerTitle", UNSET)

        country_code = d.pop("countryCode", UNSET)

        province_code = d.pop("provinceCode", UNSET)

        content_item_meta = cls(
            source_type=source_type,
            source_medium=source_medium,
            date=date,
            media_id=media_id,
            media_title=media_title,
            partner_id=partner_id,
            partner_title=partner_title,
            country_code=country_code,
            province_code=province_code,
        )

        return content_item_meta
