from enum import Enum
from typing import Literal


class WikidataItemType(str, Enum):
    ITEM = "item"

    def __str__(self) -> str:
        return str(self.value)


WikidataItemTypeLiteral = Literal["item",]
