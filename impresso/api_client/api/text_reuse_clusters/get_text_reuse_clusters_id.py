from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.text_reuse_cluster_compound import TextReuseClusterCompound
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    include_details: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["includeDetails"] = include_details

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/text-reuse-clusters/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Error, TextReuseClusterCompound]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TextReuseClusterCompound.from_dict(response.json())

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
) -> Response[Union[Any, Error, TextReuseClusterCompound]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    include_details: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, Error, TextReuseClusterCompound]]:
    """Get text reuse cluster by ID

    Args:
        id (str):
        include_details (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, TextReuseClusterCompound]]
    """

    kwargs = _get_kwargs(
        id=id,
        include_details=include_details,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    include_details: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, Error, TextReuseClusterCompound]]:
    """Get text reuse cluster by ID

    Args:
        id (str):
        include_details (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, TextReuseClusterCompound]
    """

    return sync_detailed(
        id=id,
        client=client,
        include_details=include_details,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    include_details: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, Error, TextReuseClusterCompound]]:
    """Get text reuse cluster by ID

    Args:
        id (str):
        include_details (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, TextReuseClusterCompound]]
    """

    kwargs = _get_kwargs(
        id=id,
        include_details=include_details,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    include_details: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, Error, TextReuseClusterCompound]]:
    """Get text reuse cluster by ID

    Args:
        id (str):
        include_details (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, TextReuseClusterCompound]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include_details=include_details,
        )
    ).parsed
