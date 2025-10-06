from enum import Enum
from typing import Literal


class ImpressoTextEmbeddingRequestSearchTarget(str, Enum):
    IMAGE = "image"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)


ImpressoTextEmbeddingRequestSearchTargetLiteral = Literal[
    "image",
    "text",
]
