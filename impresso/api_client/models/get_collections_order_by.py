from enum import Enum
from typing import Literal


class GetCollectionsOrderBy(str, Enum):
    DATE = "date"
    SIZE = "size"
    VALUE_0 = "-date"
    VALUE_2 = "-size"

    def __str__(self) -> str:
        return str(self.value)


GetCollectionsOrderByLiteral = Literal[
    "date",
    "size",
    "-date",
    "-size",
]
