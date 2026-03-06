from enum import Enum
from typing import Literal


class ContentItemTextItemType(str, Enum):
    AD = "ad"
    AR = "ar"
    CHAPTER = "chapter"
    CHRONICLE = "chronicle"
    OB = "ob"
    PAGE = "page"
    RADIO_BROADCAST_EPISODE = "radio_broadcast_episode"
    RADIO_BULLETIN = "radio_bulletin"
    TB = "tb"
    UNSEGMENTED = "unsegmented"
    W = "w"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextItemTypeLiteral = Literal[
    "ad",
    "ar",
    "chapter",
    "chronicle",
    "ob",
    "page",
    "radio_broadcast_episode",
    "radio_bulletin",
    "tb",
    "unsegmented",
    "w",
]
