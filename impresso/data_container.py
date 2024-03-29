from typing import Any, Generic, TypeVar
from pydantic import BaseModel

IT = TypeVar("IT")
T = TypeVar("T", bound=BaseModel)


class DataContainer(Generic[IT, T]):
    """Response of a resource call"""

    def __init__(self, data: IT, pydantic_model: type[T]):
        if data is None or getattr(data, "to_dict") is None:
            raise ValueError(f"Unexpected data object: {data}")
        self._data = data
        self._pydantic_model = pydantic_model

    @property
    def raw(self) -> dict[str, Any]:
        """Return the data as a python dictionary."""
        return getattr(self._data, "to_dict")()

    @property
    def pydantic(self) -> T:
        """Return the data as a pydantic model."""
        return self._pydantic_model.model_validate(self.raw)
