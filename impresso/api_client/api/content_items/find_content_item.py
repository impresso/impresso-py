from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.find_content_item_order_by import FindContentItemOrderBy
from ...models.find_content_item_resolve import FindContentItemResolve
from ...models.find_content_item_response_200 import FindContentItemResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    resolve: Union[Unset, FindContentItemResolve] = UNSET,
    order_by: Union[Unset, FindContentItemOrderBy] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
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

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/content-items",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, FindContentItemResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FindContentItemResponse200.from_dict(response.json())

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
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = Error.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, FindContentItemResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    resolve: Union[Unset, FindContentItemResolve] = UNSET,
    order_by: Union[Unset, FindContentItemOrderBy] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[Error, FindContentItemResponse200]]:
    """Find content items that match the given query

    Args:
        resolve (Union[Unset, FindContentItemResolve]):
        order_by (Union[Unset, FindContentItemOrderBy]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, FindContentItemResponse200]]
    """

    kwargs = _get_kwargs(
        resolve=resolve,
        order_by=order_by,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    resolve: Union[Unset, FindContentItemResolve] = UNSET,
    order_by: Union[Unset, FindContentItemOrderBy] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[Error, FindContentItemResponse200]]:
    """Find content items that match the given query

    Args:
        resolve (Union[Unset, FindContentItemResolve]):
        order_by (Union[Unset, FindContentItemOrderBy]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, FindContentItemResponse200]
    """

    return sync_detailed(
        client=client,
        resolve=resolve,
        order_by=order_by,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    resolve: Union[Unset, FindContentItemResolve] = UNSET,
    order_by: Union[Unset, FindContentItemOrderBy] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[Error, FindContentItemResponse200]]:
    """Find content items that match the given query

    Args:
        resolve (Union[Unset, FindContentItemResolve]):
        order_by (Union[Unset, FindContentItemOrderBy]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, FindContentItemResponse200]]
    """

    kwargs = _get_kwargs(
        resolve=resolve,
        order_by=order_by,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    resolve: Union[Unset, FindContentItemResolve] = UNSET,
    order_by: Union[Unset, FindContentItemOrderBy] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[Error, FindContentItemResponse200]]:
    """Find content items that match the given query

    Args:
        resolve (Union[Unset, FindContentItemResolve]):
        order_by (Union[Unset, FindContentItemOrderBy]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, FindContentItemResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            resolve=resolve,
            order_by=order_by,
            limit=limit,
            offset=offset,
        )
    ).parsed
