from enum import Enum
from typing import Literal


class ContentItemTextObituary(str, Enum):
    OB = "ob"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextObituaryLiteral = Literal["ob",]
