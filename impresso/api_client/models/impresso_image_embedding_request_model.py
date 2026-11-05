from enum import Enum
from typing import Literal


class ImpressoImageEmbeddingRequestModel(str, Enum):
    DINOV2_1024 = "dinov2-1024"
    OPENCLIP_768 = "openclip-768"
    SIGLIP2_768 = "siglip2-768"

    def __str__(self) -> str:
        return str(self.value)


ImpressoImageEmbeddingRequestModelLiteral = Literal[
    "dinov2-1024",
    "openclip-768",
    "siglip2-768",
]
