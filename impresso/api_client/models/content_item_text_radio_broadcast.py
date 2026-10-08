from enum import Enum
from typing import Literal


class ContentItemTextRadioBroadcast(str, Enum):
    RB = "rb"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextRadioBroadcastLiteral = Literal["rb",]
