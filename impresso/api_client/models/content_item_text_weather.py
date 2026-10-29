from enum import Enum
from typing import Literal


class ContentItemTextWeather(str, Enum):
    W = "w"
    WEATHER = "weather"

    def __str__(self) -> str:
        return str(self.value)


ContentItemTextWeatherLiteral = Literal[
    "w",
    "weather",
]
