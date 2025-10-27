from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="FacetWithLabel")


@_attrs_define
class FacetWithLabel:
    """An facet that has a value and a label

    Attributes:
        id (str): Unique identifier of the facet
        label (str): Label of the facet
    """

    id: str
    label: str

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        label = self.label

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        label = d.pop("label")

        facet_with_label = cls(
            id=id,
            label=label,
        )

        return facet_with_label
