from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.find_images_base_find_response_meta_provenance import FindImagesBaseFindResponseMetaProvenance


T = TypeVar("T", bound="FindImagesBaseFindResponseMeta")


@_attrs_define
class FindImagesBaseFindResponseMeta:
    """
    Attributes:
        provenance (Union[Unset, FindImagesBaseFindResponseMetaProvenance]):
    """

    provenance: Union[Unset, "FindImagesBaseFindResponseMetaProvenance"] = UNSET

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
        from ..models.find_images_base_find_response_meta_provenance import FindImagesBaseFindResponseMetaProvenance

        d = src_dict.copy()
        _provenance = d.pop("provenance", UNSET)
        provenance: Union[Unset, FindImagesBaseFindResponseMetaProvenance]
        if isinstance(_provenance, Unset):
            provenance = UNSET
        else:
            provenance = FindImagesBaseFindResponseMetaProvenance.from_dict(_provenance)

        find_images_base_find_response_meta = cls(
            provenance=provenance,
        )

        return find_images_base_find_response_meta
