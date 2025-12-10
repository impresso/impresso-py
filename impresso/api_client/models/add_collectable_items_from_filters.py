from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

from ..models.add_collectable_items_from_filters_namespace import AddCollectableItemsFromFiltersNamespace

if TYPE_CHECKING:
    from ..models.filter_ import Filter


T = TypeVar("T", bound="AddCollectableItemsFromFilters")


@_attrs_define
class AddCollectableItemsFromFilters:
    """Request to add content items to a collection from content items that match given filters

    Attributes:
        filters (List['Filter']): Filters to apply when selecting items to add to the collection
        namespace (AddCollectableItemsFromFiltersNamespace): Namespace to use when selecting items to add to the
            collection
    """

    filters: List["Filter"]
    namespace: AddCollectableItemsFromFiltersNamespace

    def to_dict(self) -> Dict[str, Any]:
        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        namespace = self.namespace.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "filters": filters,
                "namespace": namespace,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_ import Filter

        d = src_dict.copy()
        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = Filter.from_dict(filters_item_data)

            filters.append(filters_item)

        namespace = AddCollectableItemsFromFiltersNamespace(d.pop("namespace"))

        add_collectable_items_from_filters = cls(
            filters=filters,
            namespace=namespace,
        )

        return add_collectable_items_from_filters
