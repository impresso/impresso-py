from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.find_text_reuse_clusters_response_text_reuse_cluster_compound_text_reuse_cluster import (
        FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseCluster,
    )
    from ..models.find_text_reuse_clusters_response_text_reuse_cluster_compound_text_reuse_cluster_details import (
        FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetails,
    )


T = TypeVar("T", bound="FindTextReuseClustersResponseTextReuseClusterCompound")


@_attrs_define
class FindTextReuseClustersResponseTextReuseClusterCompound:
    """Text reuse cluster with details and a sample

    Attributes:
        text_sample (str):
        cluster (Union[Unset, FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseCluster]): Represents a
            cluster of text reuse passages
        details (Union[Unset, FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetails]): Extra
            details of the cluster
        bitmap_explore (Union[Unset, int]): Access rights bitmap for the UI
        bitmap_get_transcript (Union[Unset, int]): Access rights bitmap for downloading the transcript
    """

    text_sample: str
    cluster: Union[Unset, "FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseCluster"] = UNSET
    details: Union[Unset, "FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetails"] = UNSET
    bitmap_explore: Union[Unset, int] = UNSET
    bitmap_get_transcript: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        text_sample = self.text_sample

        cluster: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cluster, Unset):
            cluster = self.cluster.to_dict()

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        bitmap_explore = self.bitmap_explore

        bitmap_get_transcript = self.bitmap_get_transcript

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "textSample": text_sample,
            }
        )
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if details is not UNSET:
            field_dict["details"] = details
        if bitmap_explore is not UNSET:
            field_dict["bitmapExplore"] = bitmap_explore
        if bitmap_get_transcript is not UNSET:
            field_dict["bitmapGetTranscript"] = bitmap_get_transcript

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.find_text_reuse_clusters_response_text_reuse_cluster_compound_text_reuse_cluster import (
            FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseCluster,
        )
        from ..models.find_text_reuse_clusters_response_text_reuse_cluster_compound_text_reuse_cluster_details import (
            FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetails,
        )

        d = src_dict.copy()
        text_sample = d.pop("textSample")

        _cluster = d.pop("cluster", UNSET)
        cluster: Union[Unset, FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseCluster]
        if isinstance(_cluster, Unset):
            cluster = UNSET
        else:
            cluster = FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseCluster.from_dict(_cluster)

        _details = d.pop("details", UNSET)
        details: Union[Unset, FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetails.from_dict(_details)

        bitmap_explore = d.pop("bitmapExplore", UNSET)

        bitmap_get_transcript = d.pop("bitmapGetTranscript", UNSET)

        find_text_reuse_clusters_response_text_reuse_cluster_compound = cls(
            text_sample=text_sample,
            cluster=cluster,
            details=details,
            bitmap_explore=bitmap_explore,
            bitmap_get_transcript=bitmap_get_transcript,
        )

        return find_text_reuse_clusters_response_text_reuse_cluster_compound
