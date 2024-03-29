from enum import Enum
from typing import Literal


class GetSearchFiltersItemOp(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)


GetSearchFiltersItemOpLiteral = Literal[
    "AND",
    "OR",
]
