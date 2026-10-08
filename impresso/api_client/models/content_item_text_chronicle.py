from enum import Enum
from typing import Literal


class ContentItemTextChronicle(str, Enum):
    CH = "ch"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextChronicleLiteral = Literal["ch",]
