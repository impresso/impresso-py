from enum import Enum


class GetArticlesOrderBy(str, Enum):
    DATE = "date"
    RELEVANCE = "relevance"
    VALUE_0 = "-date"
    VALUE_2 = "-relevance"

    def __str__(self) -> str:
        return str(self.value)
