from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.article_search_response import ArticleSearchResponse
from ...models.get_search_facets import GetSearchFacets
from ...models.get_search_filters_item import GetSearchFiltersItem
from ...models.get_search_group_by import GetSearchGroupBy
from ...models.get_search_order_by import GetSearchOrderBy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: Union[Unset, str] = UNSET,
    group_by: GetSearchGroupBy = GetSearchGroupBy.ARTICLES,
    order_by: Union[Unset, GetSearchOrderBy] = UNSET,
    facets: Union[Unset, GetSearchFacets] = UNSET,
    filters: Union[Unset, List["GetSearchFiltersItem"]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    skip: Union[Unset, int] = UNSET,
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

    json_filters: Union[Unset, List[Dict[str, Any]]] = UNSET
    if not isinstance(filters, Unset):
        json_filters = []
        for filters_item_data in filters:
            filters_item = filters_item_data.to_dict()
            json_filters.append(filters_item)

    params["filters"] = json_filters

    params["limit"] = limit

    params["skip"] = skip

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ArticleSearchResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ArticleSearchResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ArticleSearchResponse]]:
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
    group_by: GetSearchGroupBy = GetSearchGroupBy.ARTICLES,
    order_by: Union[Unset, GetSearchOrderBy] = UNSET,
    facets: Union[Unset, GetSearchFacets] = UNSET,
    filters: Union[Unset, List["GetSearchFiltersItem"]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    skip: Union[Unset, int] = UNSET,
) -> Response[Union[Any, ArticleSearchResponse]]:
    """Find articles that match the given query

    Args:
        q (Union[Unset, str]):
        group_by (GetSearchGroupBy):  Default: GetSearchGroupBy.ARTICLES.
        order_by (Union[Unset, GetSearchOrderBy]):
        facets (Union[Unset, GetSearchFacets]):
        filters (Union[Unset, List['GetSearchFiltersItem']]):
        limit (Union[Unset, int]):
        skip (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ArticleSearchResponse]]
    """

    kwargs = _get_kwargs(
        q=q,
        group_by=group_by,
        order_by=order_by,
        facets=facets,
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
    q: Union[Unset, str] = UNSET,
    group_by: GetSearchGroupBy = GetSearchGroupBy.ARTICLES,
    order_by: Union[Unset, GetSearchOrderBy] = UNSET,
    facets: Union[Unset, GetSearchFacets] = UNSET,
    filters: Union[Unset, List["GetSearchFiltersItem"]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    skip: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, ArticleSearchResponse]]:
    """Find articles that match the given query

    Args:
        q (Union[Unset, str]):
        group_by (GetSearchGroupBy):  Default: GetSearchGroupBy.ARTICLES.
        order_by (Union[Unset, GetSearchOrderBy]):
        facets (Union[Unset, GetSearchFacets]):
        filters (Union[Unset, List['GetSearchFiltersItem']]):
        limit (Union[Unset, int]):
        skip (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ArticleSearchResponse]
    """

    return sync_detailed(
        client=client,
        q=q,
        group_by=group_by,
        order_by=order_by,
        facets=facets,
        filters=filters,
        limit=limit,
        skip=skip,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, str] = UNSET,
    group_by: GetSearchGroupBy = GetSearchGroupBy.ARTICLES,
    order_by: Union[Unset, GetSearchOrderBy] = UNSET,
    facets: Union[Unset, GetSearchFacets] = UNSET,
    filters: Union[Unset, List["GetSearchFiltersItem"]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    skip: Union[Unset, int] = UNSET,
) -> Response[Union[Any, ArticleSearchResponse]]:
    """Find articles that match the given query

    Args:
        q (Union[Unset, str]):
        group_by (GetSearchGroupBy):  Default: GetSearchGroupBy.ARTICLES.
        order_by (Union[Unset, GetSearchOrderBy]):
        facets (Union[Unset, GetSearchFacets]):
        filters (Union[Unset, List['GetSearchFiltersItem']]):
        limit (Union[Unset, int]):
        skip (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ArticleSearchResponse]]
    """

    kwargs = _get_kwargs(
        q=q,
        group_by=group_by,
        order_by=order_by,
        facets=facets,
        filters=filters,
        limit=limit,
        skip=skip,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, str] = UNSET,
    group_by: GetSearchGroupBy = GetSearchGroupBy.ARTICLES,
    order_by: Union[Unset, GetSearchOrderBy] = UNSET,
    facets: Union[Unset, GetSearchFacets] = UNSET,
    filters: Union[Unset, List["GetSearchFiltersItem"]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    skip: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, ArticleSearchResponse]]:
    """Find articles that match the given query

    Args:
        q (Union[Unset, str]):
        group_by (GetSearchGroupBy):  Default: GetSearchGroupBy.ARTICLES.
        order_by (Union[Unset, GetSearchOrderBy]):
        facets (Union[Unset, GetSearchFacets]):
        filters (Union[Unset, List['GetSearchFiltersItem']]):
        limit (Union[Unset, int]):
        skip (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ArticleSearchResponse]
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
            skip=skip,
        )
    ).parsed
