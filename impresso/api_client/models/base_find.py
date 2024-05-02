from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.base_find_info import BaseFindInfo


T = TypeVar("T", bound="BaseFind")


@_attrs_define
class BaseFind:
    """
    Attributes:
        limit (int): The number of items returned in this response
        skip (int): The number of items skipped in this response
        total (int): The total number of items matching the query
        info (BaseFindInfo): Additional information about the response.
        data (List[Any]):
    """

    limit: int
    skip: int
    total: int
    info: "BaseFindInfo"
    data: List[Any]

    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit

        skip = self.skip

        total = self.total

        info = self.info.to_dict()

        data = self.data

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
        from ..models.base_find_info import BaseFindInfo

        d = src_dict.copy()
        limit = d.pop("limit")

        skip = d.pop("skip")

        total = d.pop("total")

        info = BaseFindInfo.from_dict(d.pop("info"))

        data = cast(List[Any], d.pop("data"))

        base_find = cls(
            limit=limit,
            skip=skip,
            total=total,
            info=info,
            data=data,
        )

        return base_find
