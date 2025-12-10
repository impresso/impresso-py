import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.content_item_copyright_status import ContentItemCopyrightStatus
from ..models.content_item_media_type import ContentItemMediaType
from ..models.content_item_source_medium import ContentItemSourceMedium
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_item_entities_mentions_information import ContentItemEntitiesMentionsInformation
    from ..models.content_item_named_entities_information import ContentItemNamedEntitiesInformation
    from ..models.topic_mention import TopicMention


T = TypeVar("T", bound="ContentItem")


@_attrs_define
class ContentItem:
    """A journal/magazine content item (article, advertisement, etc.)

    Attributes:
        uid (str): The unique identifier of the content item.
        copyright_status (Union[Unset, ContentItemCopyrightStatus]): Copyright status.
        type (Union[Unset, str]): The type of the content item, as present in the OLR provided by the data provider. All
            content items are not characterised by the same set of types.
        source_medium (Union[Unset, ContentItemSourceMedium]): Medium of the source (audio for audio radio broadcasts,
            print for newspapers, typescript for digitised radio bulletin typescripts).
        title (Union[Unset, str]): The title of the content item.
        transcript (Union[Unset, str]): Transcript of the content item.
        entities (Union[Unset, ContentItemNamedEntitiesInformation]): A collection of linked named entities (location,
            person, etc.) present in text.
        mentions (Union[Unset, ContentItemEntitiesMentionsInformation]): A collection of entity mentions (location,
            person, etc.) present in text.
        topics (Union[Unset, List['TopicMention']]): Topics mentioned in the content item.
        embeddings (Union[Unset, List[str]]): Precomputed embeddings for the content item in the format:
            <model_type>:<base64_embedding_vector>.
        transcript_length (Union[Unset, float]): The length of the transcript in characters.
        total_pages (Union[Unset, float]): Total number of pages the item covers.
        language_code (Union[Unset, str]): ISO 639-1 language code of the content item.
        is_on_front_page (Union[Unset, bool]): Whether the content item is on the front page of the publication.
        publication_date (Union[Unset, datetime.datetime]): The publication date of the content item.
        issue_uid (Union[Unset, str]): Unique issue identifier
        country_code (Union[Unset, str]): ISO 3166-1 alpha-2 country code of the content item.
        provider_code (Union[Unset, str]): The code of the data provider.
        media_uid (Union[Unset, str]): Media title alias. Usually a 3 letter code of the media title (newspaper, radio
            station, etc.).
        media_type (Union[Unset, ContentItemMediaType]): The type of the media the content item belongs to.
        has_olr (Union[Unset, bool]): Whether the content item has OCR/OLR data available.
        ocr_quality_score (Union[Unset, float]): OCR quality score of the content item (0 - 1).
        relevance_score (Union[Unset, float]): Relevance score of the content item (0 - 1).
        page_numbers (Union[Unset, List[float]]): Page numbers the content item appears on.
        collection_uids (Union[Unset, List[str]]): Unique identifiers of collections the content item belongs to.
    """

    uid: str
    copyright_status: Union[Unset, ContentItemCopyrightStatus] = UNSET
    type: Union[Unset, str] = UNSET
    source_medium: Union[Unset, ContentItemSourceMedium] = UNSET
    title: Union[Unset, str] = UNSET
    transcript: Union[Unset, str] = UNSET
    entities: Union[Unset, "ContentItemNamedEntitiesInformation"] = UNSET
    mentions: Union[Unset, "ContentItemEntitiesMentionsInformation"] = UNSET
    topics: Union[Unset, List["TopicMention"]] = UNSET
    embeddings: Union[Unset, List[str]] = UNSET
    transcript_length: Union[Unset, float] = UNSET
    total_pages: Union[Unset, float] = UNSET
    language_code: Union[Unset, str] = UNSET
    is_on_front_page: Union[Unset, bool] = UNSET
    publication_date: Union[Unset, datetime.datetime] = UNSET
    issue_uid: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    provider_code: Union[Unset, str] = UNSET
    media_uid: Union[Unset, str] = UNSET
    media_type: Union[Unset, ContentItemMediaType] = UNSET
    has_olr: Union[Unset, bool] = UNSET
    ocr_quality_score: Union[Unset, float] = UNSET
    relevance_score: Union[Unset, float] = UNSET
    page_numbers: Union[Unset, List[float]] = UNSET
    collection_uids: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uid = self.uid

        copyright_status: Union[Unset, str] = UNSET
        if not isinstance(self.copyright_status, Unset):
            copyright_status = self.copyright_status.value

        type = self.type

        source_medium: Union[Unset, str] = UNSET
        if not isinstance(self.source_medium, Unset):
            source_medium = self.source_medium.value

        title = self.title

        transcript = self.transcript

        entities: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entities, Unset):
            entities = self.entities.to_dict()

        mentions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mentions, Unset):
            mentions = self.mentions.to_dict()

        topics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.topics, Unset):
            topics = []
            for topics_item_data in self.topics:
                topics_item = topics_item_data.to_dict()
                topics.append(topics_item)

        embeddings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.embeddings, Unset):
            embeddings = self.embeddings

        transcript_length = self.transcript_length

        total_pages = self.total_pages

        language_code = self.language_code

        is_on_front_page = self.is_on_front_page

        publication_date: Union[Unset, str] = UNSET
        if not isinstance(self.publication_date, Unset):
            publication_date = self.publication_date.isoformat()

        issue_uid = self.issue_uid

        country_code = self.country_code

        provider_code = self.provider_code

        media_uid = self.media_uid

        media_type: Union[Unset, str] = UNSET
        if not isinstance(self.media_type, Unset):
            media_type = self.media_type.value

        has_olr = self.has_olr

        ocr_quality_score = self.ocr_quality_score

        relevance_score = self.relevance_score

        page_numbers: Union[Unset, List[float]] = UNSET
        if not isinstance(self.page_numbers, Unset):
            page_numbers = self.page_numbers

        collection_uids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.collection_uids, Unset):
            collection_uids = self.collection_uids

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "uid": uid,
            }
        )
        if copyright_status is not UNSET:
            field_dict["copyrightStatus"] = copyright_status
        if type is not UNSET:
            field_dict["type"] = type
        if source_medium is not UNSET:
            field_dict["sourceMedium"] = source_medium
        if title is not UNSET:
            field_dict["title"] = title
        if transcript is not UNSET:
            field_dict["transcript"] = transcript
        if entities is not UNSET:
            field_dict["entities"] = entities
        if mentions is not UNSET:
            field_dict["mentions"] = mentions
        if topics is not UNSET:
            field_dict["topics"] = topics
        if embeddings is not UNSET:
            field_dict["embeddings"] = embeddings
        if transcript_length is not UNSET:
            field_dict["transcriptLength"] = transcript_length
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if is_on_front_page is not UNSET:
            field_dict["isOnFrontPage"] = is_on_front_page
        if publication_date is not UNSET:
            field_dict["publicationDate"] = publication_date
        if issue_uid is not UNSET:
            field_dict["issueUid"] = issue_uid
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if provider_code is not UNSET:
            field_dict["providerCode"] = provider_code
        if media_uid is not UNSET:
            field_dict["mediaUid"] = media_uid
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if has_olr is not UNSET:
            field_dict["hasOLR"] = has_olr
        if ocr_quality_score is not UNSET:
            field_dict["ocrQualityScore"] = ocr_quality_score
        if relevance_score is not UNSET:
            field_dict["relevanceScore"] = relevance_score
        if page_numbers is not UNSET:
            field_dict["pageNumbers"] = page_numbers
        if collection_uids is not UNSET:
            field_dict["collectionUids"] = collection_uids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_item_entities_mentions_information import ContentItemEntitiesMentionsInformation
        from ..models.content_item_named_entities_information import ContentItemNamedEntitiesInformation
        from ..models.topic_mention import TopicMention

        d = src_dict.copy()
        uid = d.pop("uid")

        _copyright_status = d.pop("copyrightStatus", UNSET)
        copyright_status: Union[Unset, ContentItemCopyrightStatus]
        if isinstance(_copyright_status, Unset):
            copyright_status = UNSET
        else:
            copyright_status = ContentItemCopyrightStatus(_copyright_status)

        type = d.pop("type", UNSET)

        _source_medium = d.pop("sourceMedium", UNSET)
        source_medium: Union[Unset, ContentItemSourceMedium]
        if isinstance(_source_medium, Unset):
            source_medium = UNSET
        else:
            source_medium = ContentItemSourceMedium(_source_medium)

        title = d.pop("title", UNSET)

        transcript = d.pop("transcript", UNSET)

        _entities = d.pop("entities", UNSET)
        entities: Union[Unset, ContentItemNamedEntitiesInformation]
        if isinstance(_entities, Unset):
            entities = UNSET
        else:
            entities = ContentItemNamedEntitiesInformation.from_dict(_entities)

        _mentions = d.pop("mentions", UNSET)
        mentions: Union[Unset, ContentItemEntitiesMentionsInformation]
        if isinstance(_mentions, Unset):
            mentions = UNSET
        else:
            mentions = ContentItemEntitiesMentionsInformation.from_dict(_mentions)

        topics = []
        _topics = d.pop("topics", UNSET)
        for topics_item_data in _topics or []:
            topics_item = TopicMention.from_dict(topics_item_data)

            topics.append(topics_item)

        embeddings = cast(List[str], d.pop("embeddings", UNSET))

        transcript_length = d.pop("transcriptLength", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        language_code = d.pop("languageCode", UNSET)

        is_on_front_page = d.pop("isOnFrontPage", UNSET)

        _publication_date = d.pop("publicationDate", UNSET)
        publication_date: Union[Unset, datetime.datetime]
        if isinstance(_publication_date, Unset):
            publication_date = UNSET
        else:
            publication_date = isoparse(_publication_date)

        issue_uid = d.pop("issueUid", UNSET)

        country_code = d.pop("countryCode", UNSET)

        provider_code = d.pop("providerCode", UNSET)

        media_uid = d.pop("mediaUid", UNSET)

        _media_type = d.pop("mediaType", UNSET)
        media_type: Union[Unset, ContentItemMediaType]
        if isinstance(_media_type, Unset):
            media_type = UNSET
        else:
            media_type = ContentItemMediaType(_media_type)

        has_olr = d.pop("hasOLR", UNSET)

        ocr_quality_score = d.pop("ocrQualityScore", UNSET)

        relevance_score = d.pop("relevanceScore", UNSET)

        page_numbers = cast(List[float], d.pop("pageNumbers", UNSET))

        collection_uids = cast(List[str], d.pop("collectionUids", UNSET))

        content_item = cls(
            uid=uid,
            copyright_status=copyright_status,
            type=type,
            source_medium=source_medium,
            title=title,
            transcript=transcript,
            entities=entities,
            mentions=mentions,
            topics=topics,
            embeddings=embeddings,
            transcript_length=transcript_length,
            total_pages=total_pages,
            language_code=language_code,
            is_on_front_page=is_on_front_page,
            publication_date=publication_date,
            issue_uid=issue_uid,
            country_code=country_code,
            provider_code=provider_code,
            media_uid=media_uid,
            media_type=media_type,
            has_olr=has_olr,
            ocr_quality_score=ocr_quality_score,
            relevance_score=relevance_score,
            page_numbers=page_numbers,
            collection_uids=collection_uids,
        )

        return content_item
