from impresso.api_client.client import AuthenticatedClient
from impresso.resources.articles import ArticlesResource
from impresso.resources.search import SearchResource
from impresso.resources.search_facets import SearchFacetsResource
from impresso.resources.text_reuse import TextReuseDomain


class ImpressoApiResourcesBase:
    """Base class for the Impresso client that contains resources."""

    def __init__(self, api_client: AuthenticatedClient) -> None:
        self._api_client = api_client

    @property
    def search(self) -> SearchResource:
        return SearchResource(self._api_client)

    @property
    def articles(self) -> ArticlesResource:
        return ArticlesResource(self._api_client)

    @property
    def facets(self) -> SearchFacetsResource:
        return SearchFacetsResource(self._api_client)

    @property
    def text_reuse(self) -> TextReuseDomain:
        return TextReuseDomain(self._api_client)
