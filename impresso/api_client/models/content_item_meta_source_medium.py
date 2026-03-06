from enum import Enum
from typing import Literal


class ContentItemMetaSourceMedium(str, Enum):
    AUDIO = "audio"
    PRINT = "print"
    TYPESCRIPT = "typescript"

    def __str__(self) -> str:
        return str(self.value)


ContentItemMetaSourceMediumLiteral = Literal[
    "audio",
    "print",
    "typescript",
]
