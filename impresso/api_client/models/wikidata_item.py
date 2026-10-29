from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.wikidata_item_type import WikidataItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wikidata_item_descriptions import WikidataItemDescriptions
    from ..models.wikidata_item_labels import WikidataItemLabels


T = TypeVar("T", bound="WikidataItem")


@_attrs_define
class WikidataItem:
    """Wikidata item schema. Based on https://schema.org/Place

    Attributes:
        id (str): The Q Wikidata ID of the item (https://www.wikidata.org/wiki/Wikidata:Identifiers)
        type (WikidataItemType): The type of the entity
        labels (Union[Unset, WikidataItemLabels]): Labels of the item in different languages
        descriptions (Union[Unset, WikidataItemDescriptions]): Descriptions of the item in different languages
    """

    id: str
    type: WikidataItemType
    labels: Union[Unset, "WikidataItemLabels"] = UNSET
    descriptions: Union[Unset, "WikidataItemDescriptions"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        labels: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        descriptions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.descriptions, Unset):
            descriptions = self.descriptions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "type": type,
            }
        )
        if labels is not UNSET:
            field_dict["labels"] = labels
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wikidata_item_descriptions import WikidataItemDescriptions
        from ..models.wikidata_item_labels import WikidataItemLabels

        d = src_dict.copy()
        id = d.pop("id")

        type = WikidataItemType(d.pop("type"))

        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, WikidataItemLabels]
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = WikidataItemLabels.from_dict(_labels)

        _descriptions = d.pop("descriptions", UNSET)
        descriptions: Union[Unset, WikidataItemDescriptions]
        if isinstance(_descriptions, Unset):
            descriptions = UNSET
        else:
            descriptions = WikidataItemDescriptions.from_dict(_descriptions)

        wikidata_item = cls(
            id=id,
            type=type,
            labels=labels,
            descriptions=descriptions,
        )

        return wikidata_item
