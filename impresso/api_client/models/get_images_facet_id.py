from enum import Enum
from typing import Literal


class GetImagesFacetId(str, Enum):
    COLLECTION = "collection"
    NEWSPAPER = "newspaper"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)


GetImagesFacetIdLiteral = Literal[
    "collection",
    "newspaper",
    "year",
]
