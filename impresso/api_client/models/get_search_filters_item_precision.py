from enum import Enum
from typing import Literal


class GetSearchFiltersItemPrecision(str, Enum):
    EXACT = "exact"
    FUZZY = "fuzzy"
    PARTIAL = "partial"
    SOFT = "soft"

    def __str__(self) -> str:
        return str(self.value)


GetSearchFiltersItemPrecisionLiteral = Literal[
    "exact",
    "fuzzy",
    "partial",
    "soft",
]
