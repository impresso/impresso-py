from enum import Enum
from typing import Literal


class FindTopicsOrderBy(str, Enum):
    MODEL = "model"
    NAME = "name"
    VALUE_1 = "-name"
    VALUE_3 = "-model"

    def __str__(self) -> str:
        return str(self.value)


FindTopicsOrderByLiteral = Literal[
    "model",
    "name",
    "-name",
    "-model",
]
