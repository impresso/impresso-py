from enum import Enum


class GetArticlesResolve(str, Enum):
    COLLECTION = "collection"
    TAGS = "tags"

    def __str__(self) -> str:
        return str(self.value)
