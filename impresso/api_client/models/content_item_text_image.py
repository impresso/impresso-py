from enum import Enum
from typing import Literal


class ContentItemTextImage(str, Enum):
    IMAGE = "image"
    IMG = "img"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextImageLiteral = Literal[
    "image",
    "img",
]
