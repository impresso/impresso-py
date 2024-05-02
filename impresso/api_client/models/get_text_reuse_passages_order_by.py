from enum import Enum
from typing import Literal


class GetTextReusePassagesOrderBy(str, Enum):
    CLUSTERSIZE = "clusterSize"
    DATE = "date"
    LEXICALOVERLAP = "lexicalOverlap"
    SIZE = "size"
    TIMEDIFFERENCEDAY = "timeDifferenceDay"
    VALUE_1 = "-clusterSize"
    VALUE_3 = "-lexicalOverlap"
    VALUE_5 = "-timeDifferenceDay"
    VALUE_7 = "-size"
    VALUE_9 = "-date"

    def __str__(self) -> str:
        return str(self.value)


GetTextReusePassagesOrderByLiteral = Literal[
    "clusterSize",
    "date",
    "lexicalOverlap",
    "size",
    "timeDifferenceDay",
    "-clusterSize",
    "-lexicalOverlap",
    "-timeDifferenceDay",
    "-size",
    "-date",
]
