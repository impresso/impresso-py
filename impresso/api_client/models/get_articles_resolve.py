from enum import Enum
from typing import Literal


class GetArticlesResolve(str, Enum):
    COLLECTION = "collection"
    TAGS = "tags"

    def __str__(self) -> str:
        return str(self.value)


GetArticlesResolveLiteral = Literal[
    "collection",
    "tags",
]
