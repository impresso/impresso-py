from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.find_experiments_base_find_response_meta_provenance import (
        FindExperimentsBaseFindResponseMetaProvenance,
    )


T = TypeVar("T", bound="FindExperimentsBaseFindResponseMeta")


@_attrs_define
class FindExperimentsBaseFindResponseMeta:
    """
    Attributes:
        provenance (Union[Unset, FindExperimentsBaseFindResponseMetaProvenance]):
    """

    provenance: Union[Unset, "FindExperimentsBaseFindResponseMetaProvenance"] = UNSET

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
        from ..models.find_experiments_base_find_response_meta_provenance import (
            FindExperimentsBaseFindResponseMetaProvenance,
        )

        d = src_dict.copy()
        _provenance = d.pop("provenance", UNSET)
        provenance: Union[Unset, FindExperimentsBaseFindResponseMetaProvenance]
        if isinstance(_provenance, Unset):
            provenance = UNSET
        else:
            provenance = FindExperimentsBaseFindResponseMetaProvenance.from_dict(_provenance)

        find_experiments_base_find_response_meta = cls(
            provenance=provenance,
        )

        return find_experiments_base_find_response_meta
