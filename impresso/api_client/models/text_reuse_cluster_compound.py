from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_reuse_cluster import TextReuseCluster
    from ..models.text_reuse_cluster_details import TextReuseClusterDetails


T = TypeVar("T", bound="TextReuseClusterCompound")


@_attrs_define
class TextReuseClusterCompound:
    """Text reuse cluster with details and a sample

    Attributes:
        cluster (TextReuseCluster): Represents a cluster of text reuse passages
        text_sample (str):
        details (Union[Unset, TextReuseClusterDetails]): Extra details of the cluster
    """

    cluster: "TextReuseCluster"
    text_sample: str
    details: Union[Unset, "TextReuseClusterDetails"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        cluster = self.cluster.to_dict()

        text_sample = self.text_sample

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "cluster": cluster,
                "textSample": text_sample,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.text_reuse_cluster import TextReuseCluster
        from ..models.text_reuse_cluster_details import TextReuseClusterDetails

        d = src_dict.copy()
        cluster = TextReuseCluster.from_dict(d.pop("cluster"))

        text_sample = d.pop("textSample")

        _details = d.pop("details", UNSET)
        details: Union[Unset, TextReuseClusterDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = TextReuseClusterDetails.from_dict(_details)

        text_reuse_cluster_compound = cls(
            cluster=cluster,
            text_sample=text_sample,
            details=details,
        )

        return text_reuse_cluster_compound
