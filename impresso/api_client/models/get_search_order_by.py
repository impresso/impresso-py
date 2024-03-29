from enum import Enum
from typing import Literal


class GetSearchOrderBy(str, Enum):
    DATE = "date"
    ID = "id"
    NAME = "name"
    RELEVANCE = "relevance"
    VALUE_0 = "-date"
    VALUE_2 = "-relevance"
    VALUE_4 = "-name"
    VALUE_7 = "-id"

    def __str__(self) -> str:
        return str(self.value)


GetSearchOrderByLiteral = Literal[
    "date",
    "id",
    "name",
    "relevance",
    "-date",
    "-relevance",
    "-name",
    "-id",
]
