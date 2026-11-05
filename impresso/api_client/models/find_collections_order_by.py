from enum import Enum
from typing import Literal


class FindCollectionsOrderBy(str, Enum):
    CREATIONDATE = "creationDate"
    DATE = "date"
    VALUE_0 = "-date"
    VALUE_2 = "-creationDate"

    def __str__(self) -> str:
        return str(self.value)


FindCollectionsOrderByLiteral = Literal[
    "creationDate",
    "date",
    "-date",
    "-creationDate",
]
