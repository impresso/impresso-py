from enum import Enum
from typing import Literal


class ContentItemTextPage(str, Enum):
    PAGE = "page"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextPageLiteral = Literal["page",]
