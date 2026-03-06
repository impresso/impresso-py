from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection import Collection
    from ..models.content_item_semantic_enrichments_mentions import ContentItemSemanticEnrichmentsMentions
    from ..models.content_item_semantic_enrichments_named_entities import ContentItemSemanticEnrichmentsNamedEntities
    from ..models.content_item_topic import ContentItemTopic


T = TypeVar("T", bound="ContentItemSemanticEnrichments")


@_attrs_define
class ContentItemSemanticEnrichments:
    """Semantic enrichments information

    Attributes:
        ocr_quality (Union[Unset, float]): OCR quality assessment score between 0,00 and 1,00.
        named_entities (Union[Unset, ContentItemSemanticEnrichmentsNamedEntities]): Lists of named entities in the
            content item by type.
        mentions (Union[Unset, ContentItemSemanticEnrichmentsMentions]): List of mentions in the content item per type.
        topics (Union[Unset, List['ContentItemTopic']]): List of topics assigned to the content item.
        collections (Union[Unset, List['Collection']]): List of user collections the content item belongs to.
        embeddings (Union[Unset, List[str]]): Precomputed embeddings for the content item in the format:
            <model_type>:<base64_embedding_vector>.
    """

    ocr_quality: Union[Unset, float] = UNSET
    named_entities: Union[Unset, "ContentItemSemanticEnrichmentsNamedEntities"] = UNSET
    mentions: Union[Unset, "ContentItemSemanticEnrichmentsMentions"] = UNSET
    topics: Union[Unset, List["ContentItemTopic"]] = UNSET
    collections: Union[Unset, List["Collection"]] = UNSET
    embeddings: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        ocr_quality = self.ocr_quality

        named_entities: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.named_entities, Unset):
            named_entities = self.named_entities.to_dict()

        mentions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mentions, Unset):
            mentions = self.mentions.to_dict()

        topics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.topics, Unset):
            topics = []
            for topics_item_data in self.topics:
                topics_item = topics_item_data.to_dict()
                topics.append(topics_item)

        collections: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.collections, Unset):
            collections = []
            for collections_item_data in self.collections:
                collections_item = collections_item_data.to_dict()
                collections.append(collections_item)

        embeddings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.embeddings, Unset):
            embeddings = self.embeddings

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if ocr_quality is not UNSET:
            field_dict["ocrQuality"] = ocr_quality
        if named_entities is not UNSET:
            field_dict["namedEntities"] = named_entities
        if mentions is not UNSET:
            field_dict["mentions"] = mentions
        if topics is not UNSET:
            field_dict["topics"] = topics
        if collections is not UNSET:
            field_dict["collections"] = collections
        if embeddings is not UNSET:
            field_dict["embeddings"] = embeddings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.collection import Collection
        from ..models.content_item_semantic_enrichments_mentions import ContentItemSemanticEnrichmentsMentions
        from ..models.content_item_semantic_enrichments_named_entities import (
            ContentItemSemanticEnrichmentsNamedEntities,
        )
        from ..models.content_item_topic import ContentItemTopic

        d = src_dict.copy()
        ocr_quality = d.pop("ocrQuality", UNSET)

        _named_entities = d.pop("namedEntities", UNSET)
        named_entities: Union[Unset, ContentItemSemanticEnrichmentsNamedEntities]
        if isinstance(_named_entities, Unset):
            named_entities = UNSET
        else:
            named_entities = ContentItemSemanticEnrichmentsNamedEntities.from_dict(_named_entities)

        _mentions = d.pop("mentions", UNSET)
        mentions: Union[Unset, ContentItemSemanticEnrichmentsMentions]
        if isinstance(_mentions, Unset):
            mentions = UNSET
        else:
            mentions = ContentItemSemanticEnrichmentsMentions.from_dict(_mentions)

        topics = []
        _topics = d.pop("topics", UNSET)
        for topics_item_data in _topics or []:
            topics_item = ContentItemTopic.from_dict(topics_item_data)

            topics.append(topics_item)

        collections = []
        _collections = d.pop("collections", UNSET)
        for collections_item_data in _collections or []:
            collections_item = Collection.from_dict(collections_item_data)

            collections.append(collections_item)

        embeddings = cast(List[str], d.pop("embeddings", UNSET))

        content_item_semantic_enrichments = cls(
            ocr_quality=ocr_quality,
            named_entities=named_entities,
            mentions=mentions,
            topics=topics,
            collections=collections,
            embeddings=embeddings,
        )

        return content_item_semantic_enrichments
