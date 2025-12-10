from enum import Enum
from typing import Literal


class ImpressoTextEmbeddingRequestSearchTarget(str, Enum):
    MULTIMODAL = "multimodal"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)


ImpressoTextEmbeddingRequestSearchTargetLiteral = Literal[
    "multimodal",
    "text",
]
