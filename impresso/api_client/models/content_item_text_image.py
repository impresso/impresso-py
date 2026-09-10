from enum import Enum
from typing import Literal


class ContentItemTextImage(str, Enum):
    IMG = "img"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextImageLiteral = Literal["img",]
