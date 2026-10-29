from enum import Enum
from typing import Literal


class ContentItemTextChapter(str, Enum):
    CHAPTER = "chapter"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextChapterLiteral = Literal["chapter",]
