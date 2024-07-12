from enum import Enum
from typing import Literal


class GetTrClustersFacetOrderBy(str, Enum):
    COUNT = "count"
    VALUE_0 = "-count"

    def __str__(self) -> str:
        return str(self.value)


GetTrClustersFacetOrderByLiteral = Literal[
    "count",
    "-count",
]
