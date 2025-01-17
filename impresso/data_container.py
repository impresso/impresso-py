from typing import Any, Generic, TypeVar
from pydantic import BaseModel
from pandas import DataFrame

IT = TypeVar("IT")
T = TypeVar("T", bound=BaseModel)


class DataContainer(Generic[IT, T]):
    """
    Generic container for responses from the Impresso API
    returned by resource methods (`get`, `find`).
    Generally represents a single page of the result.
    """

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

        grid_template_style = (
            "grid-template-columns: minmax(200px, 1fr) auto;"
            if preview_img is not None
            else ""
        )

        items = [
            f'<div style="display: grid; {grid_template_style}">',
            "<div>",
            f"<h2>{response_type} result</h2>",
            f"<div>Contains <b>{self.size}</b> items "
            + (
                f"(<b>{self.offset}</b> - <b>{self.offset + self.size}</b>) "
                if self.size > 0 and self.size < self.total
                else ""
            )
            + f"of <b>{self.total}</b> total items.</div>",
            "<br/>",
            (
                f'See this result in the <a href="{self.url}">Impresso App</a>.'
                if self.url
                else None
            ),
            "</div>",
            (
                (
                    f'<div style="align-content: center;"><img src="data:image/png;base64,{preview_img}" '
                    + 'style="max-width: 800px; width: 100%;"></div>'
                )
                if preview_img
                else None
            ),
            "</div>",
            "<h3>Data preview:</h3>",
            df_repr,
        ]

        return "\n".join([item for item in items if item])

    def _get_preview_image_(self) -> str | None:
        return None

    @property
    def raw(self) -> dict[str, Any]:
        """Returns the response data as a python dictionary."""
        return getattr(self._data, "to_dict")()

    @property
    def pydantic(self) -> T:
        """Returns the response data as a pydantic model."""
        return self._pydantic_model.model_validate(self.raw)

    @property
    def df(self) -> DataFrame:
        """Returns the response data as a pandas dataframe."""
        return DataFrame.from_dict(self._data)  # type: ignore

    @property
    def total(self) -> int:
        """Total number of results."""
        return self.raw.get("pagination", {}).get("total", 0)

    @property
    def limit(self) -> int:
        """Current page size."""
        return self.raw.get("pagination", {}).get("limit", 0)

    @property
    def offset(self) -> int:
        """Current page offset."""
        return self.raw.get("pagination", {}).get("offset", 0)

    @property
    def size(self) -> int:
        """Current page size."""
        return len(self.raw.get("data", []))

    @property
    def url(self) -> str | None:
        """
        URL of an Impresso web application page
        representing the result set from this container.
        """
        return self._web_app_search_result_url
