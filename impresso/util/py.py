from enum import Enum
from typing import TypeVar

from impresso.api_client.types import Unset

V = TypeVar("V", bound=str | int)
E = TypeVar("E", bound=Enum)


def get_enum_from_literal(value: V, enum: type[E]) -> E | Unset:
    if isinstance(value, Unset):
        return value

    for member in enum:
        if member.value == value:
            return member
    raise ValueError(f"{value} is not a valid member of {enum}")
