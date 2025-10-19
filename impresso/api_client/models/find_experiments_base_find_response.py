from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.experiment_info import ExperimentInfo
    from ..models.find_experiments_base_find_response_pagination import FindExperimentsBaseFindResponsePagination


T = TypeVar("T", bound="FindExperimentsBaseFindResponse")


@_attrs_define
class FindExperimentsBaseFindResponse:
    """
    Attributes:
        data (List['ExperimentInfo']):
        pagination (FindExperimentsBaseFindResponsePagination):
    """

    data: List["ExperimentInfo"]
    pagination: "FindExperimentsBaseFindResponsePagination"

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
        from ..models.experiment_info import ExperimentInfo
        from ..models.find_experiments_base_find_response_pagination import FindExperimentsBaseFindResponsePagination

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ExperimentInfo.from_dict(data_item_data)

            data.append(data_item)

        pagination = FindExperimentsBaseFindResponsePagination.from_dict(d.pop("pagination"))

        find_experiments_base_find_response = cls(
            data=data,
            pagination=pagination,
        )

        return find_experiments_base_find_response
