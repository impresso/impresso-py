from enum import Enum
from typing import Literal


class ContentItemTextDiscussion(str, Enum):
    DSC = "dsc"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextDiscussionLiteral = Literal["dsc",]
