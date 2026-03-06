from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.content_item_text_document_type import ContentItemTextDocumentType
from ..models.content_item_text_item_type import ContentItemTextItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_item_text_match import ContentItemTextMatch


T = TypeVar("T", bound="ContentItemText")


@_attrs_define
class ContentItemText:
    """Textual content details

    Attributes:
        document_type (Union[Unset, ContentItemTextDocumentType]): Type of document, e.g., page (p) or content item
            (ci).
        item_type (Union[Unset, ContentItemTextItemType]): Type of content item, e.g., article, section.
        item_type_label (Union[Unset, str]): Human-readable label for the itemType code.
        original_lang_code (Union[Unset, str]): Original language of the content item.
        lang_code (Union[Unset, str]): Computed language of the content item.
        content_length (Union[Unset, int]): Token count of the content item (space split).
        snippet (Union[Unset, str]): Snippet of the content item (first 150 characters).
        title (Union[Unset, str]): Title of the content item
        content (Union[Unset, str]): Full text content
        matches (Union[Unset, List['ContentItemTextMatch']]):
    """

    document_type: Union[Unset, ContentItemTextDocumentType] = UNSET
    item_type: Union[Unset, ContentItemTextItemType] = UNSET
    item_type_label: Union[Unset, str] = UNSET
    original_lang_code: Union[Unset, str] = UNSET
    lang_code: Union[Unset, str] = UNSET
    content_length: Union[Unset, int] = UNSET
    snippet: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    matches: Union[Unset, List["ContentItemTextMatch"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        document_type: Union[Unset, str] = UNSET
        if not isinstance(self.document_type, Unset):
            document_type = self.document_type.value

        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        item_type_label = self.item_type_label

        original_lang_code = self.original_lang_code

        lang_code = self.lang_code

        content_length = self.content_length

        snippet = self.snippet

        title = self.title

        content = self.content

        matches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.matches, Unset):
            matches = []
            for matches_item_data in self.matches:
                matches_item = matches_item_data.to_dict()
                matches.append(matches_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if item_type_label is not UNSET:
            field_dict["itemTypeLabel"] = item_type_label
        if original_lang_code is not UNSET:
            field_dict["originalLangCode"] = original_lang_code
        if lang_code is not UNSET:
            field_dict["langCode"] = lang_code
        if content_length is not UNSET:
            field_dict["contentLength"] = content_length
        if snippet is not UNSET:
            field_dict["snippet"] = snippet
        if title is not UNSET:
            field_dict["title"] = title
        if content is not UNSET:
            field_dict["content"] = content
        if matches is not UNSET:
            field_dict["matches"] = matches

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_item_text_match import ContentItemTextMatch

        d = src_dict.copy()
        _document_type = d.pop("documentType", UNSET)
        document_type: Union[Unset, ContentItemTextDocumentType]
        if isinstance(_document_type, Unset):
            document_type = UNSET
        else:
            document_type = ContentItemTextDocumentType(_document_type)

        _item_type = d.pop("itemType", UNSET)
        item_type: Union[Unset, ContentItemTextItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = ContentItemTextItemType(_item_type)

        item_type_label = d.pop("itemTypeLabel", UNSET)

        original_lang_code = d.pop("originalLangCode", UNSET)

        lang_code = d.pop("langCode", UNSET)

        content_length = d.pop("contentLength", UNSET)

        snippet = d.pop("snippet", UNSET)

        title = d.pop("title", UNSET)

        content = d.pop("content", UNSET)

        matches = []
        _matches = d.pop("matches", UNSET)
        for matches_item_data in _matches or []:
            matches_item = ContentItemTextMatch.from_dict(matches_item_data)

            matches.append(matches_item)

        content_item_text = cls(
            document_type=document_type,
            item_type=item_type,
            item_type_label=item_type_label,
            original_lang_code=original_lang_code,
            lang_code=lang_code,
            content_length=content_length,
            snippet=snippet,
            title=title,
            content=content,
            matches=matches,
        )

        return content_item_text
