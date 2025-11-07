from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topic_word import TopicWord


T = TypeVar("T", bound="Topic")


@_attrs_define
class Topic:
    """A topic

    Attributes:
        uid (str): The unique identifier of the topic
        language (str): The language code of the topic
        content_items_count (Union[Unset, float]): Number of content items with this topic
        words (Union[Unset, List['TopicWord']]): Top N words associated with the topic
        model (Union[Unset, str]): ID of the model used to generate the topic
    """

    uid: str
    language: str
    content_items_count: Union[Unset, float] = UNSET
    words: Union[Unset, List["TopicWord"]] = UNSET
    model: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uid = self.uid

        language = self.language

        content_items_count = self.content_items_count

        words: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.words, Unset):
            words = []
            for words_item_data in self.words:
                words_item = words_item_data.to_dict()
                words.append(words_item)

        model = self.model

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "uid": uid,
                "language": language,
            }
        )
        if content_items_count is not UNSET:
            field_dict["contentItemsCount"] = content_items_count
        if words is not UNSET:
            field_dict["words"] = words
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.topic_word import TopicWord

        d = src_dict.copy()
        uid = d.pop("uid")

        language = d.pop("language")

        content_items_count = d.pop("contentItemsCount", UNSET)

        words = []
        _words = d.pop("words", UNSET)
        for words_item_data in _words or []:
            words_item = TopicWord.from_dict(words_item_data)

            words.append(words_item)

        model = d.pop("model", UNSET)

        topic = cls(
            uid=uid,
            language=language,
            content_items_count=content_items_count,
            words=words,
            model=model,
        )

        return topic
