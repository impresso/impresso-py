from typing import Any, Generic, TypeVar
from pydantic import BaseModel
from pandas import DataFrame

IT = TypeVar("IT")
T = TypeVar("T", bound=BaseModel)


class DataContainer(Generic[IT, T]):
    """Response of a resource call"""

    def __init__(
        self,
        data: IT,
        pydantic_model: type[T],
        web_app_search_result_url: str | None = None,
    ):
        if data is None or getattr(data, "to_dict") is None:
            raise ValueError(f"Unexpected data object: {data}")
        self._data = data
        self._pydantic_model = pydantic_model
        self._web_app_search_result_url = web_app_search_result_url

    def _repr_html_(self):
        df_repr = self.df.head(3).to_html(notebook=True)
        response_type = self.__class__.__name__.replace("DataContainer", "").replace(
            "Container", ""
        )
        preview_img = self._get_preview_image_()

        items = [
            f"<h2>{response_type} result</h2>",
            f"<div>Contains <b>{self.limit}</b> items starting from item number <b>{self.offset}</b> of <b>{self.total}</b> total items.</div>",
            "<br/>",
            (
                f'See this result in the <a href="{self.url}">Impresso App</a>.'
                if self.url
                else None
            ),
            "<h3>Data preview:</h3>",
            df_repr,
            (
                f'<img src="data:image/png;base64,{preview_img}" style="width:100% !important;">'
                if preview_img
                else None
            ),
        ]

        return "\n".join([item for item in items if item])

    def _get_preview_image_(self) -> str | None:
        return None

    @property
    def raw(self) -> dict[str, Any]:
        """Return the data as a python dictionary."""
        return getattr(self._data, "to_dict")()

    @property
    def pydantic(self) -> T:
        """Return the data as a pydantic model."""
        return self._pydantic_model.model_validate(self.raw)

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        return DataFrame.from_dict(self._data)  # type: ignore

    @property
    def total(self) -> int:
        """Total number of results."""
        return self.raw.get("total", 0)

    @property
    def limit(self) -> int:
        """Page size."""
        return self.raw.get("limit", 0)

    @property
    def offset(self) -> int:
        """Page offset."""
        return self.raw.get("offset", 0)

    @property
    def url(self) -> str | None:
        """A URL of the result set in the Impresso web app."""
        return self._web_app_search_result_url
