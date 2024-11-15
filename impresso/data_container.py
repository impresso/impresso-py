from typing import Any, Callable, Generic, Iterator, TypeVar
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
        data_provider: tuple[Callable[..., Any], dict[Any, Any]],
        web_app_search_result_url: str | None = None,
    ):
        if data is None or getattr(data, "to_dict") is None:
            raise ValueError(f"Unexpected data object: {data}")
        self._data = data
        self._pydantic_model = pydantic_model
        self._data_provider = data_provider
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
        return self.raw.get("pagination", {}).get("total", 0)

    @property
    def limit(self) -> int:
        """Page size."""
        return self.raw.get("pagination", {}).get("limit", 0)

    @property
    def offset(self) -> int:
        """Page offset."""
        return self.raw.get("pagination", {}).get("offset", 0)

    @property
    def size(self) -> int:
        """Current page size."""
        return len(self.raw.get("data", []))

    @property
    def url(self) -> str | None:
        """A URL of the result set in the Impresso web app."""
        return self._web_app_search_result_url

    @property
    def query_parameters(self) -> dict[str, Any]:
        """Query parameters used to fetch this result container."""
        return self._data_provider[1]

    def _get_next_page_kwargs(self) -> dict[str, Any] | None:
        """Get the next page kwargs."""
        if self._data_provider is None:
            return {}
        offset = self.offset + self.limit
        if offset >= self.total:
            return None
        return {
            **self._data_provider[1],
            "offset": self.offset + self.limit,
        }

    def next_page(self) -> Iterator["DataContainer[IT, T]"]:
        """Get the next page of results."""
        if self._data_provider is None:
            raise StopIteration()

        current_result = self
        while (current_result.offset + current_result.limit) < current_result.total:
            kwargs = current_result._get_next_page_kwargs()
            if kwargs is None:
                break
            next_data_container = self._data_provider[0](**kwargs)
            current_result = next_data_container
            yield next_data_container

    def __next__(self) -> "DataContainer[IT, T]":
        """Get the next page of results."""
        return next(self.next_page())

    def __iter__(self) -> Iterator["DataContainer[IT, T]"]:
        """Get the next page of results."""
        return self.next_page()
