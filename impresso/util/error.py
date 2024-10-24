from json import JSONDecodeError
from typing import TypeVar

from impresso.api_client.models.error import Error as ApiError
from impresso.api_models import Error
import re

IT = TypeVar("IT")


class ImpressoError(Exception):
    """Impresso API Exception"""

    def __init__(self, error: Error):
        self.error = error
        super().__init__(str(self.error))

    def __str__(self):
        return str(self.error)


def raise_for_error(result: ApiError | IT) -> IT:
    """Raise an Impresso API Exception if the result is an error."""

    if isinstance(result, ApiError):
        error = Error.model_validate(result.to_dict())
        raise ImpressoError(error)
    else:
        return result


def handle_known_errors(status_code: int, response_text: str) -> None:
    # Known firewall errors
    match = re.search(r"Your support ID is: ([^\s<>]+)", response_text)
    if match:
        support_id = match.group(1)
        raise ValueError(
            f"Request rejected. Please contact Impresso team on info@impresso-project.ch quoting the ID: {support_id}."
        )
