from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection import Collection
    from ..models.entity import Entity
    from ..models.facet_with_label import FacetWithLabel
    from ..models.media_source import MediaSource
    from ..models.partner import Partner
    from ..models.topic import Topic
    from ..models.year import Year


T = TypeVar("T", bound="SearchFacetBucket")


@_attrs_define
class SearchFacetBucket:
    """Facet bucket

    Attributes:
        count (int): Number of items in the bucket
        value (Union[float, int, str]): Value that represents the bucket.
        label (Union[Unset, str]): Label of the value, if relevant.
        item (Union['Collection', 'Entity', 'FacetWithLabel', 'MediaSource', 'Partner', 'Topic', 'Year', Unset]): The
            item in the bucket. Particular object schema depends on the facet type
    """

    count: int
    value: Union[float, int, str]
    label: Union[Unset, str] = UNSET
    item: Union["Collection", "Entity", "FacetWithLabel", "MediaSource", "Partner", "Topic", "Year", Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.collection import Collection
        from ..models.entity import Entity
        from ..models.media_source import MediaSource
        from ..models.partner import Partner
        from ..models.topic import Topic
        from ..models.year import Year

        count = self.count

        value: Union[float, int, str]
        value = self.value

        label = self.label

        item: Union[Dict[str, Any], Unset]
        if isinstance(self.item, Unset):
            item = UNSET
        elif isinstance(self.item, MediaSource):
            item = self.item.to_dict()
        elif isinstance(self.item, Collection):
            item = self.item.to_dict()
        elif isinstance(self.item, Entity):
            item = self.item.to_dict()
        elif isinstance(self.item, Topic):
            item = self.item.to_dict()
        elif isinstance(self.item, Year):
            item = self.item.to_dict()
        elif isinstance(self.item, Partner):
            item = self.item.to_dict()
        else:
            item = self.item.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "count": count,
                "value": value,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if item is not UNSET:
            field_dict["item"] = item

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.collection import Collection
        from ..models.entity import Entity
        from ..models.facet_with_label import FacetWithLabel
        from ..models.media_source import MediaSource
        from ..models.partner import Partner
        from ..models.topic import Topic
        from ..models.year import Year

        d = src_dict.copy()
        count = d.pop("count")

        def _parse_value(data: object) -> Union[float, int, str]:
            return cast(Union[float, int, str], data)

        value = _parse_value(d.pop("value"))

        label = d.pop("label", UNSET)

        def _parse_item(
            data: object,
        ) -> Union["Collection", "Entity", "FacetWithLabel", "MediaSource", "Partner", "Topic", "Year", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                item_type_0 = MediaSource.from_dict(data)

                return item_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                item_type_1 = Collection.from_dict(data)

                return item_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                item_type_2 = Entity.from_dict(data)

                return item_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                item_type_3 = Topic.from_dict(data)

                return item_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                item_type_4 = Year.from_dict(data)

                return item_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                item_type_5 = Partner.from_dict(data)

                return item_type_5
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            item_type_6 = FacetWithLabel.from_dict(data)

            return item_type_6

        item = _parse_item(d.pop("item", UNSET))

        search_facet_bucket = cls(
            count=count,
            value=value,
            label=label,
            item=item,
        )

        return search_facet_bucket
