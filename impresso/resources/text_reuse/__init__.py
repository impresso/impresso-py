from impresso.api_client.client import AuthenticatedClient
from impresso.resources.text_reuse.clusters import TextReuseClustersResource


class TextReuseDomain:
    """Container for text reuse resources."""

    def __init__(self, api_client: AuthenticatedClient) -> None:
        self._api_client = api_client

    @property
    def clusters(self) -> TextReuseClustersResource:
        return TextReuseClustersResource(self._api_client)
