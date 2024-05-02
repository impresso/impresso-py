from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_newspapers_response_200_info import GetNewspapersResponse200Info
    from ..models.newspaper import Newspaper


T = TypeVar("T", bound="GetNewspapersResponse200")


@_attrs_define
class GetNewspapersResponse200:
    """
    Attributes:
        limit (int): The number of items returned in this response
        skip (int): The number of items skipped in this response
        total (int): The total number of items matching the query
        info (GetNewspapersResponse200Info): Additional information about the response.
        data (List['Newspaper']):
    """

    limit: int
    skip: int
    total: int
    info: "GetNewspapersResponse200Info"
    data: List["Newspaper"]

    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit

        skip = self.skip

        total = self.total

        info = self.info.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "limit": limit,
                "skip": skip,
                "total": total,
                "info": info,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_newspapers_response_200_info import GetNewspapersResponse200Info
        from ..models.newspaper import Newspaper

        d = src_dict.copy()
        limit = d.pop("limit")

        skip = d.pop("skip")

        total = d.pop("total")

        info = GetNewspapersResponse200Info.from_dict(d.pop("info"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Newspaper.from_dict(data_item_data)

            data.append(data_item)

        get_newspapers_response_200 = cls(
            limit=limit,
            skip=skip,
            total=total,
            info=info,
            data=data,
        )

        return get_newspapers_response_200
