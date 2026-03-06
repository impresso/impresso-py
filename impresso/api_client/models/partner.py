from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Partner")


@_attrs_define
class Partner:
    """
    Attributes:
        id (str): Partner ID
        title (str): Partner Title
        url (Union[Unset, str]): URL of the partner's website
    """

    id: str
    title: str
    url: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        title = self.title

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "title": title,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        title = d.pop("title")

        url = d.pop("url", UNSET)

        partner = cls(
            id=id,
            title=title,
            url=url,
        )

        return partner
