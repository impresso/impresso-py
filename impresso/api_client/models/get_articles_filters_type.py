from enum import Enum


class GetArticlesFiltersType(str, Enum):
    HASTEXTCONTENTS = "hasTextContents"
    ISSUE = "issue"
    NEWSPAPER = "newspaper"
    PAGE = "page"
    UID = "uid"

    def __str__(self) -> str:
        return str(self.value)
