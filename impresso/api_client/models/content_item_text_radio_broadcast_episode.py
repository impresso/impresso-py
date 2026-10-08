from enum import Enum
from typing import Literal


class ContentItemTextRadioBroadcastEpisode(str, Enum):
    RBE = "rbe"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextRadioBroadcastEpisodeLiteral = Literal["rbe",]
