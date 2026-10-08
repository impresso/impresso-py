from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.find_data_providers_base_find_response_meta_provenance import (
        FindDataProvidersBaseFindResponseMetaProvenance,
    )


T = TypeVar("T", bound="FindDataProvidersBaseFindResponseMeta")


@_attrs_define
class FindDataProvidersBaseFindResponseMeta:
    """
    Attributes:
        provenance (Union[Unset, FindDataProvidersBaseFindResponseMetaProvenance]):
    """

    provenance: Union[Unset, "FindDataProvidersBaseFindResponseMetaProvenance"] = UNSET

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
        from ..models.find_data_providers_base_find_response_meta_provenance import (
            FindDataProvidersBaseFindResponseMetaProvenance,
        )

        d = src_dict.copy()
        _provenance = d.pop("provenance", UNSET)
        provenance: Union[Unset, FindDataProvidersBaseFindResponseMetaProvenance]
        if isinstance(_provenance, Unset):
            provenance = UNSET
        else:
            provenance = FindDataProvidersBaseFindResponseMetaProvenance.from_dict(_provenance)

        find_data_providers_base_find_response_meta = cls(
            provenance=provenance,
        )

        return find_data_providers_base_find_response_meta
