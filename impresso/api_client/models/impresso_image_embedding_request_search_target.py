from enum import Enum
from typing import Literal


class ImpressoImageEmbeddingRequestSearchTarget(str, Enum):
    IMAGE = "image"
    MULTIMODAL = "multimodal"

    def __str__(self) -> str:
        return str(self.value)


ImpressoImageEmbeddingRequestSearchTargetLiteral = Literal[
    "image",
    "multimodal",
]
