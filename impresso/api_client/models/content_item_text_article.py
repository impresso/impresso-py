from enum import Enum
from typing import Literal


class ContentItemTextArticle(str, Enum):
    AR = "ar"
    ARTICLE = "article"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextArticleLiteral = Literal[
    "ar",
    "article",
]
