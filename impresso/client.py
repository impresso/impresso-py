"""Impresso Python client library."""

from impresso.api_client import AuthenticatedClient
from impresso.client_base import ImpressoApiResourcesBase
from impresso.util.token import get_jwt_status


class ImpressoClient(ImpressoApiResourcesBase):
    """
    Client class for the impresso Python libary. This is the context for all
    interactions with the impresso API.
    """

    def __init__(self, api_url: str, api_bearer_token: str):
        self._api_url = api_url
        self._api_bearer_token = api_bearer_token
        super().__init__(
            AuthenticatedClient(
                base_url=self._api_url,
                token=self._api_bearer_token,
            )
        )

    @property
    def api_url(self) -> str:
        """
        Return the Impresso Public API URL currently in use.
        """
        return self._api_url


_PROMPT = """
Click on the following link to access the login page: {URL}
 - 🔤 Enter your email/password on this page.
 - 🔑 Once logged in, a secret token will be generated for you.
 - 📋 Copy this token and paste it into the input field below 👇🏼.
"""


def connect(
    public_api_url: str = "api.impresso-project.ch",
) -> ImpressoClient:
    """
    Connect to the Impresso API and return a client object.
    """

    # Show a prompt to the user with the explanations on how to get the token.
    print(_PROMPT.format(URL=f"https://{public_api_url}/login"))
    token = input("🔑 Enter your token: ")
    token_status, _ = get_jwt_status(token)

    if token_status != "valid":
        message = (
            f"The provided token is {token_status}. Have you entered it correctly? 🤔"
        )
        print(message)
        raise ValueError(message)

    print("🎉 You are now connected to the Impresso API!  🎉")

    return ImpressoClient(api_url=public_api_url, api_bearer_token=token)
