from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.find_media_sources_base_find_response_meta_provenance import (
        FindMediaSourcesBaseFindResponseMetaProvenance,
    )


T = TypeVar("T", bound="FindMediaSourcesBaseFindResponseMeta")


@_attrs_define
class FindMediaSourcesBaseFindResponseMeta:
    """
    Attributes:
        provenance (Union[Unset, FindMediaSourcesBaseFindResponseMetaProvenance]):
    """

    provenance: Union[Unset, "FindMediaSourcesBaseFindResponseMetaProvenance"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        provenance: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.provenance, Unset):
            provenance = self.provenance.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if provenance is not UNSET:
            field_dict["provenance"] = provenance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.find_media_sources_base_find_response_meta_provenance import (
            FindMediaSourcesBaseFindResponseMetaProvenance,
        )

        d = src_dict.copy()
        _provenance = d.pop("provenance", UNSET)
        provenance: Union[Unset, FindMediaSourcesBaseFindResponseMetaProvenance]
        if isinstance(_provenance, Unset):
            provenance = UNSET
        else:
            provenance = FindMediaSourcesBaseFindResponseMetaProvenance.from_dict(_provenance)

        find_media_sources_base_find_response_meta = cls(
            provenance=provenance,
        )

        return find_media_sources_base_find_response_meta
