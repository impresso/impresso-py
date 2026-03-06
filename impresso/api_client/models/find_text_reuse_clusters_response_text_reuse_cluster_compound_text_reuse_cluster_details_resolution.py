from enum import Enum
from typing import Literal


class FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsResolution(str, Enum):
    DAY = "day"
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)


FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsResolutionLiteral = Literal[
    "day",
    "month",
    "year",
]
