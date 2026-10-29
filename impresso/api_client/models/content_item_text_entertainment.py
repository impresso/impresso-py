from enum import Enum
from typing import Literal


class ContentItemTextEntertainment(str, Enum):
    ENT = "ent"
    ENTERTAINMENT = "entertainment"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextEntertainmentLiteral = Literal[
    "ent",
    "entertainment",
]
