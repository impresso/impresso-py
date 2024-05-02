from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.filter_ import Filter
from ...models.get_text_reuse_clusters_order_by import GetTextReuseClustersOrderBy
from ...models.get_text_reuse_clusters_response_200 import GetTextReuseClustersResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    text: Union[Unset, str] = UNSET,
    order_by: Union[Unset, GetTextReuseClustersOrderBy] = UNSET,
    filters: Union[Unset, List["Filter"]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    skip: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["text"] = text

    json_order_by: Union[Unset, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    json_filters: Union[Unset, List[Dict[str, Any]]] = UNSET
    if not isinstance(filters, Unset):
        json_filters = []
        for filters_item_data in filters:
            filters_item = filters_item_data.to_dict()
            json_filters.append(filters_item)

    params["filters[]"] = json_filters

    params["limit"] = limit

    params["skip"] = skip

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/text-reuse-clusters",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Error, GetTextReuseClustersResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetTextReuseClustersResponse200.from_dict(response.json())

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
) -> Response[Union[Any, Error, GetTextReuseClustersResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    text: Union[Unset, str] = UNSET,
    order_by: Union[Unset, GetTextReuseClustersOrderBy] = UNSET,
    filters: Union[Unset, List["Filter"]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    skip: Union[Unset, int] = UNSET,
) -> Response[Union[Any, Error, GetTextReuseClustersResponse200]]:
    """Find text reuse clusters

    Args:
        text (Union[Unset, str]):
        order_by (Union[Unset, GetTextReuseClustersOrderBy]):
        filters (Union[Unset, List['Filter']]):
        limit (Union[Unset, int]):
        skip (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, GetTextReuseClustersResponse200]]
    """

    kwargs = _get_kwargs(
        text=text,
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
    text: Union[Unset, str] = UNSET,
    order_by: Union[Unset, GetTextReuseClustersOrderBy] = UNSET,
    filters: Union[Unset, List["Filter"]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    skip: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, Error, GetTextReuseClustersResponse200]]:
    """Find text reuse clusters

    Args:
        text (Union[Unset, str]):
        order_by (Union[Unset, GetTextReuseClustersOrderBy]):
        filters (Union[Unset, List['Filter']]):
        limit (Union[Unset, int]):
        skip (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, GetTextReuseClustersResponse200]
    """

    return sync_detailed(
        client=client,
        text=text,
        order_by=order_by,
        filters=filters,
        limit=limit,
        skip=skip,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    text: Union[Unset, str] = UNSET,
    order_by: Union[Unset, GetTextReuseClustersOrderBy] = UNSET,
    filters: Union[Unset, List["Filter"]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    skip: Union[Unset, int] = UNSET,
) -> Response[Union[Any, Error, GetTextReuseClustersResponse200]]:
    """Find text reuse clusters

    Args:
        text (Union[Unset, str]):
        order_by (Union[Unset, GetTextReuseClustersOrderBy]):
        filters (Union[Unset, List['Filter']]):
        limit (Union[Unset, int]):
        skip (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, GetTextReuseClustersResponse200]]
    """

    kwargs = _get_kwargs(
        text=text,
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
    text: Union[Unset, str] = UNSET,
    order_by: Union[Unset, GetTextReuseClustersOrderBy] = UNSET,
    filters: Union[Unset, List["Filter"]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    skip: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, Error, GetTextReuseClustersResponse200]]:
    """Find text reuse clusters

    Args:
        text (Union[Unset, str]):
        order_by (Union[Unset, GetTextReuseClustersOrderBy]):
        filters (Union[Unset, List['Filter']]):
        limit (Union[Unset, int]):
        skip (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, GetTextReuseClustersResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            text=text,
            order_by=order_by,
            filters=filters,
            limit=limit,
            skip=skip,
        )
    ).parsed
