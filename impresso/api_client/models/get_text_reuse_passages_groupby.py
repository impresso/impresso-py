from enum import Enum
from typing import Literal


class GetTextReusePassagesGroupby(str, Enum):
    TEXTREUSECLUSTERID = "textReuseClusterId"

    def __str__(self) -> str:
        return str(self.value)


GetTextReusePassagesGroupbyLiteral = Literal["textReuseClusterId",]
