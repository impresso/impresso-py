from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.find_text_reuse_passages_base_find_response_meta_provenance import (
        FindTextReusePassagesBaseFindResponseMetaProvenance,
    )


T = TypeVar("T", bound="FindTextReusePassagesBaseFindResponseMeta")


@_attrs_define
class FindTextReusePassagesBaseFindResponseMeta:
    """
    Attributes:
        provenance (Union[Unset, FindTextReusePassagesBaseFindResponseMetaProvenance]):
    """

    provenance: Union[Unset, "FindTextReusePassagesBaseFindResponseMetaProvenance"] = UNSET

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
        from ..models.find_text_reuse_passages_base_find_response_meta_provenance import (
            FindTextReusePassagesBaseFindResponseMetaProvenance,
        )

        d = src_dict.copy()
        _provenance = d.pop("provenance", UNSET)
        provenance: Union[Unset, FindTextReusePassagesBaseFindResponseMetaProvenance]
        if isinstance(_provenance, Unset):
            provenance = UNSET
        else:
            provenance = FindTextReusePassagesBaseFindResponseMetaProvenance.from_dict(_provenance)

        find_text_reuse_passages_base_find_response_meta = cls(
            provenance=provenance,
        )

        return find_text_reuse_passages_base_find_response_meta
