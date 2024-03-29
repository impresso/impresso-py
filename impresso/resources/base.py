from impresso.api_client.client import AuthenticatedClient


class Resource:
    """Base for all API backed resources."""

    name: str

    def __init__(self, api_client: AuthenticatedClient):
        self._api_client = api_client
