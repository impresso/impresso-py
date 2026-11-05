from enum import Enum
from typing import Literal


class ContentItemTextTable(str, Enum):
    TABLE = "table"
    TB = "tb"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextTableLiteral = Literal[
    "table",
    "tb",
]
