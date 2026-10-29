from enum import Enum
from typing import Literal


class ContentItemTextObituary(str, Enum):
    DEATH_NOTICE = "death_notice"
    OB = "ob"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextObituaryLiteral = Literal[
    "death_notice",
    "ob",
]
