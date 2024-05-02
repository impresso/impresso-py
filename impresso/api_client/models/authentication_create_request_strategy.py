from enum import Enum
from typing import Literal


class AuthenticationCreateRequestStrategy(str, Enum):
    LOCAL = "local"

    def __str__(self) -> str:
        return str(self.value)


AuthenticationCreateRequestStrategyLiteral = Literal["local",]
