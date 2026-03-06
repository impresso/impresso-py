from enum import Enum
from typing import Literal


class AuthenticationCreateRequestStrategy(str, Enum):
    JWT = "jwt"
    JWT_APP = "jwt-app"
    LOCAL = "local"
    MAGIC_LINK = "magic-link"

    def __str__(self) -> str:
        return str(self.value)


AuthenticationCreateRequestStrategyLiteral = Literal[
    "jwt",
    "jwt-app",
    "local",
    "magic-link",
]
