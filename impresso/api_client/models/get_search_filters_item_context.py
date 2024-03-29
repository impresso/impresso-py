from enum import Enum
from typing import Literal


class GetSearchFiltersItemContext(str, Enum):
    EXCLUDE = "exclude"
    INCLUDE = "include"

    def __str__(self) -> str:
        return str(self.value)


GetSearchFiltersItemContextLiteral = Literal[
    "exclude",
    "include",
]
