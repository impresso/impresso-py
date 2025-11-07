from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_mention import EntityMention


T = TypeVar("T", bound="ContentItemEntitiesMentionsInformation")


@_attrs_define
class ContentItemEntitiesMentionsInformation:
    """A collection of entity mentions (location, person, etc.) present in text.

    Attributes:
        locations (Union[Unset, List['EntityMention']]): Locations mentioned in the content item.
        persons (Union[Unset, List['EntityMention']]): Persons mentioned in the content item.
        organisations (Union[Unset, List['EntityMention']]): Organisations mentioned in the content item.
        news_agencies (Union[Unset, List['EntityMention']]): News agencies mentioned in the content item.
    """

    locations: Union[Unset, List["EntityMention"]] = UNSET
    persons: Union[Unset, List["EntityMention"]] = UNSET
    organisations: Union[Unset, List["EntityMention"]] = UNSET
    news_agencies: Union[Unset, List["EntityMention"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        locations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

        persons: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.persons, Unset):
            persons = []
            for persons_item_data in self.persons:
                persons_item = persons_item_data.to_dict()
                persons.append(persons_item)

        organisations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.organisations, Unset):
            organisations = []
            for organisations_item_data in self.organisations:
                organisations_item = organisations_item_data.to_dict()
                organisations.append(organisations_item)

        news_agencies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.news_agencies, Unset):
            news_agencies = []
            for news_agencies_item_data in self.news_agencies:
                news_agencies_item = news_agencies_item_data.to_dict()
                news_agencies.append(news_agencies_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if locations is not UNSET:
            field_dict["locations"] = locations
        if persons is not UNSET:
            field_dict["persons"] = persons
        if organisations is not UNSET:
            field_dict["organisations"] = organisations
        if news_agencies is not UNSET:
            field_dict["newsAgencies"] = news_agencies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity_mention import EntityMention

        d = src_dict.copy()
        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = EntityMention.from_dict(locations_item_data)

            locations.append(locations_item)

        persons = []
        _persons = d.pop("persons", UNSET)
        for persons_item_data in _persons or []:
            persons_item = EntityMention.from_dict(persons_item_data)

            persons.append(persons_item)

        organisations = []
        _organisations = d.pop("organisations", UNSET)
        for organisations_item_data in _organisations or []:
            organisations_item = EntityMention.from_dict(organisations_item_data)

            organisations.append(organisations_item)

        news_agencies = []
        _news_agencies = d.pop("newsAgencies", UNSET)
        for news_agencies_item_data in _news_agencies or []:
            news_agencies_item = EntityMention.from_dict(news_agencies_item_data)

            news_agencies.append(news_agencies_item)

        content_item_entities_mentions_information = cls(
            locations=locations,
            persons=persons,
            organisations=organisations,
            news_agencies=news_agencies,
        )

        return content_item_entities_mentions_information
