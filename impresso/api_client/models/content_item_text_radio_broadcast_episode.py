from enum import Enum
from typing import Literal


class ContentItemTextRadioBroadcastEpisode(str, Enum):
    RADIO_BROADCAST_EPISODE = "radio_broadcast_episode"
    RBE = "rbe"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextRadioBroadcastEpisodeLiteral = Literal[
    "radio_broadcast_episode",
    "rbe",
]
