from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.find_text_reuse_clusters_response_text_reuse_cluster_compound_text_reuse_cluster_details_resolution import (
    FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsResolution,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.find_text_reuse_clusters_response_text_reuse_cluster_compound_text_reuse_cluster_details_facets_item import (
        FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsFacetsItem,
    )


T = TypeVar("T", bound="FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetails")


@_attrs_define
class FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetails:
    """Extra details of the cluster

    Attributes:
        facets (List['FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsFacetsItem']):
        resolution (Union[Unset,
            FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsResolution]): Resolution for the
            'date' facet
    """

    facets: List["FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsFacetsItem"]
    resolution: Union[Unset, FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsResolution] = (
        UNSET
    )

    def to_dict(self) -> Dict[str, Any]:
        facets = []
        for facets_item_data in self.facets:
            facets_item = facets_item_data.to_dict()
            facets.append(facets_item)

        resolution: Union[Unset, str] = UNSET
        if not isinstance(self.resolution, Unset):
            resolution = self.resolution.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "facets": facets,
            }
        )
        if resolution is not UNSET:
            field_dict["resolution"] = resolution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.find_text_reuse_clusters_response_text_reuse_cluster_compound_text_reuse_cluster_details_facets_item import (
            FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsFacetsItem,
        )

        d = src_dict.copy()
        facets = []
        _facets = d.pop("facets")
        for facets_item_data in _facets:
            facets_item = (
                FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsFacetsItem.from_dict(
                    facets_item_data
                )
            )

            facets.append(facets_item)

        _resolution = d.pop("resolution", UNSET)
        resolution: Union[Unset, FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsResolution]
        if isinstance(_resolution, Unset):
            resolution = UNSET
        else:
            resolution = FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsResolution(
                _resolution
            )

        find_text_reuse_clusters_response_text_reuse_cluster_compound_text_reuse_cluster_details = cls(
            facets=facets,
            resolution=resolution,
        )

        return find_text_reuse_clusters_response_text_reuse_cluster_compound_text_reuse_cluster_details
