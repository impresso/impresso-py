from enum import Enum
from typing import Literal


class ContentItemTextTable(str, Enum):
    TB = "tb"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextTableLiteral = Literal["tb",]
