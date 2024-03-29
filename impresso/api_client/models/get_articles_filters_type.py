from enum import Enum
from typing import Literal


class GetArticlesFiltersType(str, Enum):
    HASTEXTCONTENTS = "hasTextContents"
    ISSUE = "issue"
    NEWSPAPER = "newspaper"
    PAGE = "page"
    UID = "uid"

    def __str__(self) -> str:
        return str(self.value)


GetArticlesFiltersTypeLiteral = Literal[
    "hasTextContents",
    "issue",
    "newspaper",
    "page",
    "uid",
]
