from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_item_mention import ContentItemMention


T = TypeVar("T", bound="ContentItemSemanticEnrichmentsMentions")


@_attrs_define
class ContentItemSemanticEnrichmentsMentions:
    """List of mentions in the content item per type.

    Attributes:
        persons (Union[Unset, List['ContentItemMention']]):
        locations (Union[Unset, List['ContentItemMention']]):
        organisations (Union[Unset, List['ContentItemMention']]):
        newsagencies (Union[Unset, List['ContentItemMention']]):
    """

    persons: Union[Unset, List["ContentItemMention"]] = UNSET
    locations: Union[Unset, List["ContentItemMention"]] = UNSET
    organisations: Union[Unset, List["ContentItemMention"]] = UNSET
    newsagencies: Union[Unset, List["ContentItemMention"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        persons: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.persons, Unset):
            persons = []
            for persons_item_data in self.persons:
                persons_item = persons_item_data.to_dict()
                persons.append(persons_item)

        locations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

        organisations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.organisations, Unset):
            organisations = []
            for organisations_item_data in self.organisations:
                organisations_item = organisations_item_data.to_dict()
                organisations.append(organisations_item)

        newsagencies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.newsagencies, Unset):
            newsagencies = []
            for newsagencies_item_data in self.newsagencies:
                newsagencies_item = newsagencies_item_data.to_dict()
                newsagencies.append(newsagencies_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if persons is not UNSET:
            field_dict["persons"] = persons
        if locations is not UNSET:
            field_dict["locations"] = locations
        if organisations is not UNSET:
            field_dict["organisations"] = organisations
        if newsagencies is not UNSET:
            field_dict["newsagencies"] = newsagencies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_item_mention import ContentItemMention

        d = src_dict.copy()
        persons = []
        _persons = d.pop("persons", UNSET)
        for persons_item_data in _persons or []:
            persons_item = ContentItemMention.from_dict(persons_item_data)

            persons.append(persons_item)

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = ContentItemMention.from_dict(locations_item_data)

            locations.append(locations_item)

        organisations = []
        _organisations = d.pop("organisations", UNSET)
        for organisations_item_data in _organisations or []:
            organisations_item = ContentItemMention.from_dict(organisations_item_data)

            organisations.append(organisations_item)

        newsagencies = []
        _newsagencies = d.pop("newsagencies", UNSET)
        for newsagencies_item_data in _newsagencies or []:
            newsagencies_item = ContentItemMention.from_dict(newsagencies_item_data)

            newsagencies.append(newsagencies_item)

        content_item_semantic_enrichments_mentions = cls(
            persons=persons,
            locations=locations,
            organisations=organisations,
            newsagencies=newsagencies,
        )

        return content_item_semantic_enrichments_mentions
