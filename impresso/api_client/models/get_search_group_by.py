from enum import Enum
from typing import Literal


class GetSearchGroupBy(str, Enum):
    ARTICLES = "articles"
    RAW = "raw"

    def __str__(self) -> str:
        return str(self.value)


GetSearchGroupByLiteral = Literal[
    "articles",
    "raw",
]
