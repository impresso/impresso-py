from enum import Enum
from typing import Literal


class GetTextReuseClustersOrderBy(str, Enum):
    PASSAGES_COUNT = "passages-count"
    VALUE_1 = "-passages-count"

    def __str__(self) -> str:
        return str(self.value)


GetTextReuseClustersOrderByLiteral = Literal[
    "passages-count",
    "-passages-count",
]
