import datetime
from typing import Sequence, Union
from collections.abc import Sequence as _Sequence


class AND(set[str]):
    """
    Used in filters to specify that all the terms must be present in the result.

    Example:

    ```
    AND(["apple", "banana"])
    AND("apple")
    AND("apple", "banana")
    ```

    """

    def __init__(self, items: Union[Sequence[str], str], *args: str):
        if not isinstance(items, str):
            _items = items
        else:
            _items = [items] + list(args)

        super().__init__(_items)


class OR(set[str]):
    """
    Used in filters to specify that any of the terms must be present in the result.


    Example:

    ```
    OR(["apple", "banana"])
    OR("apple")
    OR("apple", "banana")
    ```

    """

    def __init__(self, items: Union[Sequence[str], str], *args: str):
        if not isinstance(items, str):
            _items = items
        else:
            _items = [items] + list(args)

        super().__init__(_items)


class DateRange(tuple[datetime.date, datetime.date]):
    """
    Date range.

    Example:

    ```
    DateRange(datetime.date(1900, 1, 1), datetime.date(2000, 12, 31))

    # Everything until 2000
    DateRange(None, datetime.date(2000, 12, 31))

    # Everything since 1900
    DateRange(datetime.date(1900, 12, 31), None)

    ```

    """

    def __new__(
        cls, start: datetime.date | str | None, end: datetime.date | str | None
    ):
        _start = datetime.date.min if start is None else DateRange._as_date(start)
        _end = datetime.date.max if end is None else DateRange._as_date(end)
        return (_start, _end)

    @staticmethod
    def _as_filter_value(v: tuple[datetime.date, datetime.date]) -> str:
        return f"{v[0].isoformat()}T00:00:00Z TO {v[1].isoformat()}T00:00:00Z"

    @staticmethod
    def _as_date(value: datetime.date | str) -> datetime.date:
        if isinstance(value, str):
            return datetime.date.fromisoformat(value)
        return value
