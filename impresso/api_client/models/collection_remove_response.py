from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.collection_remove_response_params import CollectionRemoveResponseParams
    from ..models.collection_remove_response_task import CollectionRemoveResponseTask


T = TypeVar("T", bound="CollectionRemoveResponse")


@_attrs_define
class CollectionRemoveResponse:
    """Remove collection response

    Attributes:
        params (CollectionRemoveResponseParams):
        task (CollectionRemoveResponseTask): Deletion task details
    """

    params: "CollectionRemoveResponseParams"
    task: "CollectionRemoveResponseTask"

    def to_dict(self) -> Dict[str, Any]:
        params = self.params.to_dict()

        task = self.task.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "params": params,
                "task": task,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.collection_remove_response_params import CollectionRemoveResponseParams
        from ..models.collection_remove_response_task import CollectionRemoveResponseTask

        d = src_dict.copy()
        params = CollectionRemoveResponseParams.from_dict(d.pop("params"))

        task = CollectionRemoveResponseTask.from_dict(d.pop("task"))

        collection_remove_response = cls(
            params=params,
            task=task,
        )

        return collection_remove_response
