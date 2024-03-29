from enum import Enum


class GetSearchOrderBy(str, Enum):
    DATE = "date"
    ID = "id"
    NAME = "name"
    RELEVANCE = "relevance"
    VALUE_0 = "-date"
    VALUE_2 = "-relevance"
    VALUE_4 = "-name"
    VALUE_7 = "-id"

    def __str__(self) -> str:
        return str(self.value)
