from enum import Enum
from typing import Literal


class ContentItemAccessRightsCopyright(str, Enum):
    EUO = "euo"
    IN_CPY = "in_cpy"
    NKN = "nkn"
    PBL = "pbl"
    UND = "und"
    UNK = "unk"

    def __str__(self) -> str:
        return str(self.value)


ContentItemAccessRightsCopyrightLiteral = Literal[
    "euo",
    "in_cpy",
    "nkn",
    "pbl",
    "und",
    "unk",
]
