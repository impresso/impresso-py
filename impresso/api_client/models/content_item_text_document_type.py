from enum import Enum
from typing import Literal


class ContentItemTextDocumentType(str, Enum):
    CI = "ci"
    P = "p"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextDocumentTypeLiteral = Literal[
    "ci",
    "p",
]
