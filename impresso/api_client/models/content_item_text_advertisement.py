from enum import Enum
from typing import Literal


class ContentItemTextAdvertisement(str, Enum):
    AD = "ad"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextAdvertisementLiteral = Literal["ad",]
