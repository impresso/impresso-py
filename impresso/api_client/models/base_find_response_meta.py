from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_find_response_meta_provenance import BaseFindResponseMetaProvenance


T = TypeVar("T", bound="BaseFindResponseMeta")


@_attrs_define
class BaseFindResponseMeta:
    """
    Attributes:
        provenance (Union[Unset, BaseFindResponseMetaProvenance]):
    """

    provenance: Union[Unset, "BaseFindResponseMetaProvenance"] = UNSET

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
        from ..models.base_find_response_meta_provenance import BaseFindResponseMetaProvenance

        d = src_dict.copy()
        _provenance = d.pop("provenance", UNSET)
        provenance: Union[Unset, BaseFindResponseMetaProvenance]
        if isinstance(_provenance, Unset):
            provenance = UNSET
        else:
            provenance = BaseFindResponseMetaProvenance.from_dict(_provenance)

        base_find_response_meta = cls(
            provenance=provenance,
        )

        return base_find_response_meta
