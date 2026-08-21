from enum import Enum
from typing import Literal


class MediaSourceMedium(str, Enum):
    AUDIO = "audio"
    PRINT = "print"
    TYPESCRIPT = "typescript"

    def __str__(self) -> str:
        return str(self.value)


MediaSourceMediumLiteral = Literal[
    "audio",
    "print",
    "typescript",
]
