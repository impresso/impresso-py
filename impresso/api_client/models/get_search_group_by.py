from enum import Enum


class GetSearchGroupBy(str, Enum):
    ARTICLES = "articles"
    RAW = "raw"

    def __str__(self) -> str:
        return str(self.value)
