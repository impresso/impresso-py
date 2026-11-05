from enum import Enum
from typing import Literal


class ImpressoTextEmbeddingRequestModel(str, Enum):
    GTE_256 = "gte-256"
    GTE_768 = "gte-768"
    OPENCLIP_768 = "openclip-768"
    SIGLIP2_768 = "siglip2-768"

    def __str__(self) -> str:
        return str(self.value)


ImpressoTextEmbeddingRequestModelLiteral = Literal[
    "gte-256",
    "gte-768",
    "openclip-768",
    "siglip2-768",
]
