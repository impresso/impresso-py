from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.image import Image
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    include_embeddings: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["include_embeddings"] = include_embeddings

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/images/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, Image]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Image.from_dict(response.json())

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
    if response.status_code == HTTPStatus.IM_A_TEAPOT:
        response_418 = Error.from_dict(response.json())

        return response_418
    if response.status_code == HTTPStatus.UNPROCESSABLE_CONTENT:
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
) -> Response[Union[Error, Image]]:
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
    include_embeddings: Union[Unset, bool] = UNSET,
) -> Response[Union[Error, Image]]:
    """Get image by ID

    Args:
        id (str):
        include_embeddings (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Image]]
    """

    kwargs = _get_kwargs(
        id=id,
        include_embeddings=include_embeddings,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    include_embeddings: Union[Unset, bool] = UNSET,
) -> Optional[Union[Error, Image]]:
    """Get image by ID

    Args:
        id (str):
        include_embeddings (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Image]
    """

    return sync_detailed(
        id=id,
        client=client,
        include_embeddings=include_embeddings,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    include_embeddings: Union[Unset, bool] = UNSET,
) -> Response[Union[Error, Image]]:
    """Get image by ID

    Args:
        id (str):
        include_embeddings (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Image]]
    """

    kwargs = _get_kwargs(
        id=id,
        include_embeddings=include_embeddings,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    include_embeddings: Union[Unset, bool] = UNSET,
) -> Optional[Union[Error, Image]]:
    """Get image by ID

    Args:
        id (str):
        include_embeddings (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Image]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include_embeddings=include_embeddings,
        )
    ).parsed
