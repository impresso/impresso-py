from enum import Enum
from typing import Literal


class ContentItemTextNoTypeProvided(str, Enum):
    NO_TYPE = "no-type"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextNoTypeProvidedLiteral = Literal["no-type",]
