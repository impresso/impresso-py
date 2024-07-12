from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchFacet")


@_attrs_define
class SearchFacet:
    """An object containing search results for a facet

    Attributes:
        type (str): The type of facet
        num_buckets (int): The number of buckets in the facet
        buckets (Any):
        min_ (Union[Unset, Any]): TODO
        max_ (Union[Unset, Any]): TODO
        gap (Union[Unset, Any]): TODO
    """

    type: str
    num_buckets: int
    buckets: Any
    min_: Union[Unset, Any] = UNSET
    max_: Union[Unset, Any] = UNSET
    gap: Union[Unset, Any] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        num_buckets = self.num_buckets

        buckets = self.buckets

        min_ = self.min_

        max_ = self.max_

        gap = self.gap

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "numBuckets": num_buckets,
                "buckets": buckets,
            }
        )
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if gap is not UNSET:
            field_dict["gap"] = gap

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        num_buckets = d.pop("numBuckets")

        buckets = d.pop("buckets")

        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        gap = d.pop("gap", UNSET)

        search_facet = cls(
            type=type,
            num_buckets=num_buckets,
            buckets=buckets,
            min_=min_,
            max_=max_,
            gap=gap,
        )

        return search_facet
