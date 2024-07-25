from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.filter_ import Filter
from ...models.search_facets import SearchFacets
from ...models.search_group_by import SearchGroupBy
from ...models.search_order_by import SearchOrderBy
from ...models.search_response_200 import SearchResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: Union[Unset, str] = UNSET,
    group_by: SearchGroupBy = SearchGroupBy.ARTICLES,
    order_by: Union[Unset, SearchOrderBy] = UNSET,
    facets: Union[Unset, SearchFacets] = UNSET,
    filters: Union[List["Filter"], Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["q"] = q

    json_group_by = group_by.value
    params["group_by"] = json_group_by

    json_order_by: Union[Unset, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    json_facets: Union[Unset, str] = UNSET
    if not isinstance(facets, Unset):
        json_facets = facets.value

    params["facets"] = json_facets

    json_filters: Union[List[Dict[str, Any]], Unset, str]
    if isinstance(filters, Unset):
        json_filters = UNSET
    elif isinstance(filters, list):
        json_filters = []
        for filters_type_1_item_data in filters:
            filters_type_1_item = filters_type_1_item_data.to_dict()
            json_filters.append(filters_type_1_item)

    else:
        json_filters = filters
    params["filters"] = json_filters

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, SearchResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SearchResponse200.from_dict(response.json())

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
) -> Response[Union[Error, SearchResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, str] = UNSET,
    group_by: SearchGroupBy = SearchGroupBy.ARTICLES,
    order_by: Union[Unset, SearchOrderBy] = UNSET,
    facets: Union[Unset, SearchFacets] = UNSET,
    filters: Union[List["Filter"], Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[Error, SearchResponse200]]:
    """Find articles that match the given query

    Args:
        q (Union[Unset, str]):
        group_by (SearchGroupBy):  Default: SearchGroupBy.ARTICLES.
        order_by (Union[Unset, SearchOrderBy]):
        facets (Union[Unset, SearchFacets]):
        filters (Union[List['Filter'], Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SearchResponse200]]
    """

    kwargs = _get_kwargs(
        q=q,
        group_by=group_by,
        order_by=order_by,
        facets=facets,
        filters=filters,
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
    q: Union[Unset, str] = UNSET,
    group_by: SearchGroupBy = SearchGroupBy.ARTICLES,
    order_by: Union[Unset, SearchOrderBy] = UNSET,
    facets: Union[Unset, SearchFacets] = UNSET,
    filters: Union[List["Filter"], Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[Error, SearchResponse200]]:
    """Find articles that match the given query

    Args:
        q (Union[Unset, str]):
        group_by (SearchGroupBy):  Default: SearchGroupBy.ARTICLES.
        order_by (Union[Unset, SearchOrderBy]):
        facets (Union[Unset, SearchFacets]):
        filters (Union[List['Filter'], Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SearchResponse200]
    """

    return sync_detailed(
        client=client,
        q=q,
        group_by=group_by,
        order_by=order_by,
        facets=facets,
        filters=filters,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, str] = UNSET,
    group_by: SearchGroupBy = SearchGroupBy.ARTICLES,
    order_by: Union[Unset, SearchOrderBy] = UNSET,
    facets: Union[Unset, SearchFacets] = UNSET,
    filters: Union[List["Filter"], Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[Error, SearchResponse200]]:
    """Find articles that match the given query

    Args:
        q (Union[Unset, str]):
        group_by (SearchGroupBy):  Default: SearchGroupBy.ARTICLES.
        order_by (Union[Unset, SearchOrderBy]):
        facets (Union[Unset, SearchFacets]):
        filters (Union[List['Filter'], Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SearchResponse200]]
    """

    kwargs = _get_kwargs(
        q=q,
        group_by=group_by,
        order_by=order_by,
        facets=facets,
        filters=filters,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, str] = UNSET,
    group_by: SearchGroupBy = SearchGroupBy.ARTICLES,
    order_by: Union[Unset, SearchOrderBy] = UNSET,
    facets: Union[Unset, SearchFacets] = UNSET,
    filters: Union[List["Filter"], Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[Error, SearchResponse200]]:
    """Find articles that match the given query

    Args:
        q (Union[Unset, str]):
        group_by (SearchGroupBy):  Default: SearchGroupBy.ARTICLES.
        order_by (Union[Unset, SearchOrderBy]):
        facets (Union[Unset, SearchFacets]):
        filters (Union[List['Filter'], Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SearchResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            group_by=group_by,
            order_by=order_by,
            facets=facets,
            filters=filters,
            limit=limit,
            offset=offset,
        )
    ).parsed