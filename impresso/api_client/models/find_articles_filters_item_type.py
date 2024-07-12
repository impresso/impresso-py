from enum import Enum
from typing import Literal


class FindArticlesFiltersItemType(str, Enum):
    HASTEXTCONTENTS = "hasTextContents"
    ISSUE = "issue"
    NEWSPAPER = "newspaper"
    PAGE = "page"
    UID = "uid"

    def __str__(self) -> str:
        return str(self.value)


FindArticlesFiltersItemTypeLiteral = Literal[
    "hasTextContents",
    "issue",
    "newspaper",
    "page",
    "uid",
]
