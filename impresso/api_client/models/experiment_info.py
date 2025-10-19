from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExperimentInfo")


@_attrs_define
class ExperimentInfo:
    """Information about an available experiment including its identifier, name, and description.

    Attributes:
        id (str): The unique identifier of the experiment.
        name (str): The display name of the experiment.
        description (Union[Unset, str]): A description of what the experiment does.
    """

    id: str
    name: str
    description: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        experiment_info = cls(
            id=id,
            name=name,
            description=description,
        )

        return experiment_info
