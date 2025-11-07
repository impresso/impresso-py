from typing import Any, Callable, Iterator, cast

from pandas import DataFrame, json_normalize

from impresso.api_client.api.data_providers import find_data_providers, get_data_provider
from impresso.api_client.models.find_data_providers_base_find_response import (
    FindDataProvidersBaseFindResponse,
)
from impresso.api_client.types import UNSET
from impresso.api_models import BaseFind, Filter
from impresso.data_container import DataContainer, iterate_pages
from impresso.resources.base import Resource
from impresso.structures import AND, OR
from impresso.util.error import raise_for_error
from impresso.util.filters import and_or_filter, filters_as_protobuf


class FindDataProvidersSchema(BaseFind):
    """Schema for the find data providers response."""

    data: list[dict]


class FindDataProvidersContainer(DataContainer):
    """Response of a find call."""

    def __init__(
        self,
        data: FindDataProvidersBaseFindResponse,
        pydantic_model: type[FindDataProvidersSchema],
        fetch_method: Callable[..., "FindDataProvidersContainer"],
        fetch_method_args: dict[str, Any],
        web_app_search_result_url: str | None = None,
    ):
        super().__init__(data, pydantic_model, web_app_search_result_url)
        self._fetch_method = fetch_method
        self._fetch_method_args = fetch_method_args

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        data = self._data.to_dict()["data"]
        if len(data):
            return json_normalize(self._data.to_dict()["data"]).set_index("id")
        return DataFrame()

    def pages(self) -> Iterator["FindDataProvidersContainer"]:
        """Iterate over all pages of results."""
        yield self
        yield from iterate_pages(
            self._fetch_method,
            self._fetch_method_args,
            self.offset,
            self.limit,
            self.total,
        )


class GetDataProviderContainer(DataContainer):
    """Response of a get call."""

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        data = self._data.to_dict()
        if len(data):
            return json_normalize([self._data.to_dict()]).set_index("id")
        return DataFrame()


class DataProvidersResource(Resource):
    """Search data providers in the Impresso database."""

    name = "data_providers"

    def find(
        self,
        term: str | None = None,
        provider_id: str | AND[str] | OR[str] | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> FindDataProvidersContainer:
        """
        Search data providers in Impresso.

        Data providers are partner institutions that provide content to Impresso,
        such as libraries, archives, and media organizations.

        Args:
            term: Search term to find data providers by their names.
            provider_id: Return only data provider with this ID.
            limit: Number of results to return.
            offset: Number of results to skip.

        Returns:
            FindDataProvidersContainer: Data container with a page of results of the search.
        """

        filters: list[Filter] = []
        if provider_id is not None:
            filters.extend(and_or_filter(provider_id, "id"))

        filters_pb = filters_as_protobuf(filters or [])

        result = find_data_providers.sync(
            client=self._api_client,
            term=term if term is not None else UNSET,
            limit=limit if limit is not None else UNSET,
            offset=offset if offset is not None else UNSET,
        )
        raise_for_error(result)
        return FindDataProvidersContainer(
            cast(FindDataProvidersBaseFindResponse, result),
            FindDataProvidersSchema,
            fetch_method=self.find,
            fetch_method_args={
                "term": term,
                "provider_id": provider_id,
            },
            web_app_search_result_url=(
                _build_web_app_find_data_providers_url(
                    base_url=self._get_web_app_base_url(),
                    term=term,
                )
                if provider_id is None
                else None
            ),
        )

    def get(self, id: str) -> GetDataProviderContainer:
        """Get data provider by ID."""

        result = get_data_provider.sync(
            client=self._api_client,
            id=id,
        )
        raise_for_error(result)
        return GetDataProviderContainer(
            result,
            FindDataProvidersSchema,
            web_app_search_result_url=_build_web_app_get_data_provider_url(
                base_url=self._get_web_app_base_url(),
                id=id,
            ),
        )


def _build_web_app_find_data_providers_url(
    base_url: str,
    term: str | None = None,
) -> str:
    query_params = {
        "q": term,
    }
    query_string = "&".join(
        f"{key}={value}" for key, value in query_params.items() if value is not None
    )
    url = f"{base_url}/data-providers"
    return f"{url}?{query_string}" if query_string else url


def _build_web_app_get_data_provider_url(
    base_url: str,
    id: str,
) -> str:
    return f"{base_url}/data-providers/{id}"
