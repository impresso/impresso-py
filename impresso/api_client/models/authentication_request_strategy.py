from enum import Enum


class AuthenticationRequestStrategy(str, Enum):
    LOCAL = "local"

    def __str__(self) -> str:
        return str(self.value)
