from enum import Enum
from typing import Literal


class ContentItemAccessRightsDataDomain(str, Enum):
    PBL = "pbl"
    PRT = "prt"

    def __str__(self) -> str:
        return str(self.value)


ContentItemAccessRightsDataDomainLiteral = Literal[
    "pbl",
    "prt",
]
