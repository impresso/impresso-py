from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.find_newspapers_base_find_response_pagination import FindNewspapersBaseFindResponsePagination
    from ..models.newspaper import Newspaper


T = TypeVar("T", bound="FindNewspapersBaseFindResponse")


@_attrs_define
class FindNewspapersBaseFindResponse:
    """
    Attributes:
        data (List['Newspaper']):
        pagination (FindNewspapersBaseFindResponsePagination):
    """

    data: List["Newspaper"]
    pagination: "FindNewspapersBaseFindResponsePagination"

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
        from ..models.find_newspapers_base_find_response_pagination import FindNewspapersBaseFindResponsePagination
        from ..models.newspaper import Newspaper

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Newspaper.from_dict(data_item_data)

            data.append(data_item)

        pagination = FindNewspapersBaseFindResponsePagination.from_dict(d.pop("pagination"))

        find_newspapers_base_find_response = cls(
            data=data,
            pagination=pagination,
        )

        return find_newspapers_base_find_response
