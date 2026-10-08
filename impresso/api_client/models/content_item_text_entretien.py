from enum import Enum
from typing import Literal


class ContentItemTextEntretien(str, Enum):
    ENT = "ent"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextEntretienLiteral = Literal["ent",]
