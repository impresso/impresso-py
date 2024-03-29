from enum import Enum
from typing import TypeVar

V = TypeVar("V", bound=str | int)
E = TypeVar("E", bound=Enum)


def get_enum_from_literal(value: V, enum: type[E]) -> E:
    for member in enum:
        if member.value == value:
            return member
    raise ValueError(f"{value} is not a valid member of {enum}")
