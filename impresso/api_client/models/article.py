from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity import Entity
    from ..models.page import Page


T = TypeVar("T", bound="Article")


@_attrs_define
class Article:
    """A journal/magazine article

    Attributes:
        uid (str): The unique identifier of the article
        type (str): The type of the article. NOTE: may be empty.
        title (str): The title of the article
        size (int): The size of the article in characters
        nb_pages (int): The number of pages in this article
        pages (List['Page']):
        is_cc (bool): TODO
        excerpt (str): The excerpt of the article
        locations (Union[Unset, List['Entity']]):
        persons (Union[Unset, List['Entity']]):
    """

    uid: str
    type: str
    title: str
    size: int
    nb_pages: int
    pages: List["Page"]
    is_cc: bool
    excerpt: str
    locations: Union[Unset, List["Entity"]] = UNSET
    persons: Union[Unset, List["Entity"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uid = self.uid

        type = self.type

        title = self.title

        size = self.size

        nb_pages = self.nb_pages

        pages = []
        for pages_item_data in self.pages:
            pages_item = pages_item_data.to_dict()
            pages.append(pages_item)

        is_cc = self.is_cc

        excerpt = self.excerpt

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "uid": uid,
                "type": type,
                "title": title,
                "size": size,
                "nbPages": nb_pages,
                "pages": pages,
                "isCC": is_cc,
                "excerpt": excerpt,
            }
        )
        if locations is not UNSET:
            field_dict["locations"] = locations
        if persons is not UNSET:
            field_dict["persons"] = persons

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity import Entity
        from ..models.page import Page

        d = src_dict.copy()
        uid = d.pop("uid")

        type = d.pop("type")

        title = d.pop("title")

        size = d.pop("size")

        nb_pages = d.pop("nbPages")

        pages = []
        _pages = d.pop("pages")
        for pages_item_data in _pages:
            pages_item = Page.from_dict(pages_item_data)

            pages.append(pages_item)

        is_cc = d.pop("isCC")

        excerpt = d.pop("excerpt")

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = Entity.from_dict(locations_item_data)

            locations.append(locations_item)

        persons = []
        _persons = d.pop("persons", UNSET)
        for persons_item_data in _persons or []:
            persons_item = Entity.from_dict(persons_item_data)

            persons.append(persons_item)

        article = cls(
            uid=uid,
            type=type,
            title=title,
            size=size,
            nb_pages=nb_pages,
            pages=pages,
            is_cc=is_cc,
            excerpt=excerpt,
            locations=locations,
            persons=persons,
        )

        return article
