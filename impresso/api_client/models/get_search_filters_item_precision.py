from enum import Enum


class GetSearchFiltersItemPrecision(str, Enum):
    EXACT = "exact"
    FUZZY = "fuzzy"
    PARTIAL = "partial"
    SOFT = "soft"

    def __str__(self) -> str:
        return str(self.value)
