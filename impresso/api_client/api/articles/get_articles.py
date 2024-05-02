from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_articles_filters import GetArticlesFilters
from ...models.get_articles_order_by import GetArticlesOrderBy
from ...models.get_articles_resolve import GetArticlesResolve
from ...models.get_articles_response_200 import GetArticlesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    resolve: Union[Unset, GetArticlesResolve] = UNSET,
    order_by: Union[Unset, GetArticlesOrderBy] = UNSET,
    filters: Union[Unset, "GetArticlesFilters"] = UNSET,
    limit: Union[Unset, int] = UNSET,
    skip: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_resolve: Union[Unset, str] = UNSET
    if not isinstance(resolve, Unset):
        json_resolve = resolve.value

    params["resolve"] = json_resolve

    json_order_by: Union[Unset, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    json_filters: Union[Unset, Dict[str, Any]] = UNSET
    if not isinstance(filters, Unset):
        json_filters = filters.to_dict()
    if not isinstance(json_filters, Unset):
        params.update(json_filters)

    params["limit"] = limit

    params["skip"] = skip

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/articles",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Error, GetArticlesResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetArticlesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = Error.from_dict(response.json())

        return response_422
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Error, GetArticlesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    resolve: Union[Unset, GetArticlesResolve] = UNSET,
    order_by: Union[Unset, GetArticlesOrderBy] = UNSET,
    filters: Union[Unset, "GetArticlesFilters"] = UNSET,
    limit: Union[Unset, int] = UNSET,
    skip: Union[Unset, int] = UNSET,
) -> Response[Union[Any, Error, GetArticlesResponse200]]:
    """Find articles that match the given query

    Args:
        resolve (Union[Unset, GetArticlesResolve]):
        order_by (Union[Unset, GetArticlesOrderBy]):
        filters (Union[Unset, GetArticlesFilters]):
        limit (Union[Unset, int]):
        skip (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, GetArticlesResponse200]]
    """

    kwargs = _get_kwargs(
        resolve=resolve,
        order_by=order_by,
        filters=filters,
        limit=limit,
        skip=skip,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    resolve: Union[Unset, GetArticlesResolve] = UNSET,
    order_by: Union[Unset, GetArticlesOrderBy] = UNSET,
    filters: Union[Unset, "GetArticlesFilters"] = UNSET,
    limit: Union[Unset, int] = UNSET,
    skip: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, Error, GetArticlesResponse200]]:
    """Find articles that match the given query

    Args:
        resolve (Union[Unset, GetArticlesResolve]):
        order_by (Union[Unset, GetArticlesOrderBy]):
        filters (Union[Unset, GetArticlesFilters]):
        limit (Union[Unset, int]):
        skip (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, GetArticlesResponse200]
    """

    return sync_detailed(
        client=client,
        resolve=resolve,
        order_by=order_by,
        filters=filters,
        limit=limit,
        skip=skip,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    resolve: Union[Unset, GetArticlesResolve] = UNSET,
    order_by: Union[Unset, GetArticlesOrderBy] = UNSET,
    filters: Union[Unset, "GetArticlesFilters"] = UNSET,
    limit: Union[Unset, int] = UNSET,
    skip: Union[Unset, int] = UNSET,
) -> Response[Union[Any, Error, GetArticlesResponse200]]:
    """Find articles that match the given query

    Args:
        resolve (Union[Unset, GetArticlesResolve]):
        order_by (Union[Unset, GetArticlesOrderBy]):
        filters (Union[Unset, GetArticlesFilters]):
        limit (Union[Unset, int]):
        skip (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, GetArticlesResponse200]]
    """

    kwargs = _get_kwargs(
        resolve=resolve,
        order_by=order_by,
        filters=filters,
        limit=limit,
        skip=skip,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    resolve: Union[Unset, GetArticlesResolve] = UNSET,
    order_by: Union[Unset, GetArticlesOrderBy] = UNSET,
    filters: Union[Unset, "GetArticlesFilters"] = UNSET,
    limit: Union[Unset, int] = UNSET,
    skip: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, Error, GetArticlesResponse200]]:
    """Find articles that match the given query

    Args:
        resolve (Union[Unset, GetArticlesResolve]):
        order_by (Union[Unset, GetArticlesOrderBy]):
        filters (Union[Unset, GetArticlesFilters]):
        limit (Union[Unset, int]):
        skip (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, GetArticlesResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            resolve=resolve,
            order_by=order_by,
            filters=filters,
            limit=limit,
            skip=skip,
        )
    ).parsed
