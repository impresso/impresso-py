from enum import Enum
from typing import Literal


class ContentItemTextItemType(str, Enum):
    AD = "ad"
    ADVERTISEMENT = "advertisement"
    AR = "ar"
    ARTICLE = "article"
    CH = "ch"
    CHAPTER = "chapter"
    CHRONICLE = "chronicle"
    DEATH_NOTICE = "death_notice"
    DISCUSSION = "discussion"
    DSC = "dsc"
    ENT = "ent"
    ENTERTAINMENT = "entertainment"
    NO_TYPE = "no-type"
    OB = "ob"
    PAGE = "page"
    RADIO_BROADCAST_EPISODE = "radio_broadcast_episode"
    RADIO_BULLETIN = "radio_bulletin"
    RB = "rb"
    RBE = "rbe"
    TB = "tb"
    UNSEGMENTED = "unsegmented"
    W = "w"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextItemTypeLiteral = Literal[
    "ad",
    "advertisement",
    "ar",
    "article",
    "ch",
    "chapter",
    "chronicle",
    "death_notice",
    "discussion",
    "dsc",
    "ent",
    "entertainment",
    "no-type",
    "ob",
    "page",
    "radio_broadcast_episode",
    "radio_bulletin",
    "rb",
    "rbe",
    "tb",
    "unsegmented",
    "w",
]
