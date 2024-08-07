from typing import Literal

from pandas import DataFrame, json_normalize

from impresso.api_client.api.entities import find_entities, get_entity
from impresso.api_client.models.find_entities_order_by import (
    FindEntitiesOrderBy,
    FindEntitiesOrderByLiteral,
)
from impresso.api_client.types import UNSET
from impresso.api_models import BaseFind, EntityDetails, Filter
from impresso.data_container import DataContainer
from impresso.resources.base import Resource
from impresso.structures import AND, OR
from impresso.util.error import raise_for_error
from impresso.util.filters import and_or_filter, filters_as_protobuf
from impresso.util.py import get_enum_from_literal


class FindEntitiesSchema(BaseFind):
    """Schema for the find entities response."""

    data: list[EntityDetails]


class FindEntitiesContainer(DataContainer):
    """Response of a find call."""

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        data = self._data.to_dict()["data"]
        if len(data):
            return json_normalize(self._data.to_dict()["data"]).set_index("uid")
        return DataFrame()


class GetEntityContainer(DataContainer):
    """Response of a get call."""

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        data = self._data.to_dict()
        if len(data):
            return json_normalize([self._data.to_dict()]).set_index("uid")
        return DataFrame()


EntityType = Literal["person", "location"]


class EntitiesResource(Resource):
    """Work with entities"""

    name = "entities"

    def find(
        self,
        q: str | None = None,
        entity_type: EntityType | AND[EntityType] | OR[EntityType] | None = None,
        order_by: FindEntitiesOrderByLiteral | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> FindEntitiesContainer:
        """Find entities."""

        filters: list[Filter] = []
        if entity_type is not None:
            filters.extend(and_or_filter(entity_type, "type"))

        filters_pb = filters_as_protobuf(filters or [])

        result = find_entities.sync(
            client=self._api_client,
            q=q if q is not None else UNSET,
            order_by=(
                get_enum_from_literal(order_by, FindEntitiesOrderBy)
                if order_by is not None
                else UNSET
            ),
            limit=limit if limit is not None else UNSET,
            offset=offset if offset is not None else UNSET,
            filters=filters_pb if filters_pb else UNSET,
        )
        raise_for_error(result)
        return FindEntitiesContainer(result, FindEntitiesSchema)

    def get(self, id: str) -> GetEntityContainer:
        """Get entity by ID."""

        result = get_entity.sync(
            client=self._api_client,
            id=id,
        )
        raise_for_error(result)
        return GetEntityContainer(result, FindEntitiesSchema)
