from enum import Enum
from typing import Literal


class FindTrPassagesFacetsOrderBy(str, Enum):
    COUNT = "count"
    VALUE_0 = "-count"

    def __str__(self) -> str:
        return str(self.value)


FindTrPassagesFacetsOrderByLiteral = Literal[
    "count",
    "-count",
]
