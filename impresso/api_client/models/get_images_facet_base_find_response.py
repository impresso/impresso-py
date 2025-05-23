from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_images_facet_base_find_response_pagination import GetImagesFacetBaseFindResponsePagination
    from ..models.search_facet_bucket import SearchFacetBucket


T = TypeVar("T", bound="GetImagesFacetBaseFindResponse")


@_attrs_define
class GetImagesFacetBaseFindResponse:
    """
    Attributes:
        data (List['SearchFacetBucket']):
        pagination (GetImagesFacetBaseFindResponsePagination):
    """

    data: List["SearchFacetBucket"]
    pagination: "GetImagesFacetBaseFindResponsePagination"

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        pagination = self.pagination.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "data": data,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_images_facet_base_find_response_pagination import GetImagesFacetBaseFindResponsePagination
        from ..models.search_facet_bucket import SearchFacetBucket

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = SearchFacetBucket.from_dict(data_item_data)

            data.append(data_item)

        pagination = GetImagesFacetBaseFindResponsePagination.from_dict(d.pop("pagination"))

        get_images_facet_base_find_response = cls(
            data=data,
            pagination=pagination,
        )

        return get_images_facet_base_find_response
