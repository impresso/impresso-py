from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_item_access_rights import ContentItemAccessRights
    from ..models.content_item_audio import ContentItemAudio
    from ..models.content_item_image import ContentItemImage
    from ..models.content_item_meta import ContentItemMeta
    from ..models.content_item_semantic_enrichments import ContentItemSemanticEnrichments
    from ..models.content_item_text import ContentItemText


T = TypeVar("T", bound="ContentItem")


@_attrs_define
class ContentItem:
    """Unified schema for media content items in the Impresso project, with modular field groups.

    Attributes:
        id (str): Unique identifier for the content item
        issue_id (Union[Unset, str]): Unique issue identifier
        relevance_score (Union[Unset, float]): Relevance score for this content item relative to the search query
        meta (Union[Unset, ContentItemMeta]): Content Item metadata
        text (Union[Unset, ContentItemText]): Textual content details
        semantic_enrichments (Union[Unset, ContentItemSemanticEnrichments]): Semantic enrichments information
        image (Union[Unset, ContentItemImage]): Image-related information for digitized content
        audio (Union[Unset, ContentItemAudio]): Audio-related information for broadcast content
        access (Union[Unset, ContentItemAccessRights]): Access rights information
    """

    id: str
    issue_id: Union[Unset, str] = UNSET
    relevance_score: Union[Unset, float] = UNSET
    meta: Union[Unset, "ContentItemMeta"] = UNSET
    text: Union[Unset, "ContentItemText"] = UNSET
    semantic_enrichments: Union[Unset, "ContentItemSemanticEnrichments"] = UNSET
    image: Union[Unset, "ContentItemImage"] = UNSET
    audio: Union[Unset, "ContentItemAudio"] = UNSET
    access: Union[Unset, "ContentItemAccessRights"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        issue_id = self.issue_id

        relevance_score = self.relevance_score

        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.text, Unset):
            text = self.text.to_dict()

        semantic_enrichments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.semantic_enrichments, Unset):
            semantic_enrichments = self.semantic_enrichments.to_dict()

        image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        audio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.audio, Unset):
            audio = self.audio.to_dict()

        access: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )
        if issue_id is not UNSET:
            field_dict["issueId"] = issue_id
        if relevance_score is not UNSET:
            field_dict["relevanceScore"] = relevance_score
        if meta is not UNSET:
            field_dict["meta"] = meta
        if text is not UNSET:
            field_dict["text"] = text
        if semantic_enrichments is not UNSET:
            field_dict["semanticEnrichments"] = semantic_enrichments
        if image is not UNSET:
            field_dict["image"] = image
        if audio is not UNSET:
            field_dict["audio"] = audio
        if access is not UNSET:
            field_dict["access"] = access

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_item_access_rights import ContentItemAccessRights
        from ..models.content_item_audio import ContentItemAudio
        from ..models.content_item_image import ContentItemImage
        from ..models.content_item_meta import ContentItemMeta
        from ..models.content_item_semantic_enrichments import ContentItemSemanticEnrichments
        from ..models.content_item_text import ContentItemText

        d = src_dict.copy()
        id = d.pop("id")

        issue_id = d.pop("issueId", UNSET)

        relevance_score = d.pop("relevanceScore", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, ContentItemMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ContentItemMeta.from_dict(_meta)

        _text = d.pop("text", UNSET)
        text: Union[Unset, ContentItemText]
        if isinstance(_text, Unset):
            text = UNSET
        else:
            text = ContentItemText.from_dict(_text)

        _semantic_enrichments = d.pop("semanticEnrichments", UNSET)
        semantic_enrichments: Union[Unset, ContentItemSemanticEnrichments]
        if isinstance(_semantic_enrichments, Unset):
            semantic_enrichments = UNSET
        else:
            semantic_enrichments = ContentItemSemanticEnrichments.from_dict(_semantic_enrichments)

        _image = d.pop("image", UNSET)
        image: Union[Unset, ContentItemImage]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = ContentItemImage.from_dict(_image)

        _audio = d.pop("audio", UNSET)
        audio: Union[Unset, ContentItemAudio]
        if isinstance(_audio, Unset):
            audio = UNSET
        else:
            audio = ContentItemAudio.from_dict(_audio)

        _access = d.pop("access", UNSET)
        access: Union[Unset, ContentItemAccessRights]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = ContentItemAccessRights.from_dict(_access)

        content_item = cls(
            id=id,
            issue_id=issue_id,
            relevance_score=relevance_score,
            meta=meta,
            text=text,
            semantic_enrichments=semantic_enrichments,
            image=image,
            audio=audio,
            access=access,
        )

        return content_item
