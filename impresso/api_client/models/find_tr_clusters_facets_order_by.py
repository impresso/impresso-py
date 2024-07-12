from enum import Enum
from typing import Literal


class FindTrClustersFacetsOrderBy(str, Enum):
    COUNT = "count"
    VALUE_0 = "-count"

    def __str__(self) -> str:
        return str(self.value)


FindTrClustersFacetsOrderByLiteral = Literal[
    "count",
    "-count",
]
