from enum import Enum
from typing import Literal


class AddCollectableItemsFromFiltersNamespace(str, Enum):
    SEARCH = "search"
    TR_PASSAGES = "tr_passages"

    def __str__(self) -> str:
        return str(self.value)


AddCollectableItemsFromFiltersNamespaceLiteral = Literal[
    "search",
    "tr_passages",
]
