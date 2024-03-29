from enum import Enum
from typing import Literal


class AuthenticationRequestStrategy(str, Enum):
    LOCAL = "local"

    def __str__(self) -> str:
        return str(self.value)


AuthenticationRequestStrategyLiteral = Literal["local",]
