from enum import Enum
from typing import Literal


class CollectionRemoveResponseParamsStatus(str, Enum):
    DEL = "DEL"

    def __str__(self) -> str:
        return str(self.value)


CollectionRemoveResponseParamsStatusLiteral = Literal["DEL",]
