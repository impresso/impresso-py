from enum import Enum
from typing import Literal


class ContentItemTextRadioBulletin(str, Enum):
    RADIO_BULLETIN = "radio_bulletin"
    RB = "rb"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextRadioBulletinLiteral = Literal[
    "radio_bulletin",
    "rb",
]
