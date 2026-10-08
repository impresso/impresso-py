from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.provenance_verification_response_type_0 import ProvenanceVerificationResponseType0
from ...models.provenance_verification_response_type_1 import ProvenanceVerificationResponseType1
from ...types import Response


def _get_kwargs(
    *,
    body: Any,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/tools/provenance",
    }

    _body: Any
    _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, Union["ProvenanceVerificationResponseType0", "ProvenanceVerificationResponseType1"]]]:
    if response.status_code == HTTPStatus.CREATED:

        def _parse_response_201(
            data: object,
        ) -> Union["ProvenanceVerificationResponseType0", "ProvenanceVerificationResponseType1"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_provenance_verification_response_type_0 = (
                    ProvenanceVerificationResponseType0.from_dict(data)
                )

                return componentsschemas_provenance_verification_response_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_provenance_verification_response_type_1 = ProvenanceVerificationResponseType1.from_dict(
                data
            )

            return componentsschemas_provenance_verification_response_type_1

        response_201 = _parse_response_201(response.json())

        return response_201
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
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
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = Error.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, Union["ProvenanceVerificationResponseType0", "ProvenanceVerificationResponseType1"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Any,
) -> Response[Union[Error, Union["ProvenanceVerificationResponseType0", "ProvenanceVerificationResponseType1"]]]:
    r"""Usually send only { \"token\": \"<receipt>\" }. Copy the receipt from meta.provenance.token or
    X-Impresso-Provenance; authenticate the request with your normal API JWT. This verifies the
    signature and claims and returns valid and claims (no idsMatch). Optionally supply ID material to
    compare membership/order only; idsHash compares the supplied digest without examining a dataset,
    while ids/csv are examined server-side. The embedded CSV receipt is ignored.

    Args:
        body (Any): Signed delivery receipts identify receiving accounts and ordered item IDs
            only. They do not attest item content or identify a publisher.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['ProvenanceVerificationResponseType0', 'ProvenanceVerificationResponseType1']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Any,
) -> Optional[Union[Error, Union["ProvenanceVerificationResponseType0", "ProvenanceVerificationResponseType1"]]]:
    r"""Usually send only { \"token\": \"<receipt>\" }. Copy the receipt from meta.provenance.token or
    X-Impresso-Provenance; authenticate the request with your normal API JWT. This verifies the
    signature and claims and returns valid and claims (no idsMatch). Optionally supply ID material to
    compare membership/order only; idsHash compares the supplied digest without examining a dataset,
    while ids/csv are examined server-side. The embedded CSV receipt is ignored.

    Args:
        body (Any): Signed delivery receipts identify receiving accounts and ordered item IDs
            only. They do not attest item content or identify a publisher.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Union['ProvenanceVerificationResponseType0', 'ProvenanceVerificationResponseType1']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Any,
) -> Response[Union[Error, Union["ProvenanceVerificationResponseType0", "ProvenanceVerificationResponseType1"]]]:
    r"""Usually send only { \"token\": \"<receipt>\" }. Copy the receipt from meta.provenance.token or
    X-Impresso-Provenance; authenticate the request with your normal API JWT. This verifies the
    signature and claims and returns valid and claims (no idsMatch). Optionally supply ID material to
    compare membership/order only; idsHash compares the supplied digest without examining a dataset,
    while ids/csv are examined server-side. The embedded CSV receipt is ignored.

    Args:
        body (Any): Signed delivery receipts identify receiving accounts and ordered item IDs
            only. They do not attest item content or identify a publisher.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['ProvenanceVerificationResponseType0', 'ProvenanceVerificationResponseType1']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Any,
) -> Optional[Union[Error, Union["ProvenanceVerificationResponseType0", "ProvenanceVerificationResponseType1"]]]:
    r"""Usually send only { \"token\": \"<receipt>\" }. Copy the receipt from meta.provenance.token or
    X-Impresso-Provenance; authenticate the request with your normal API JWT. This verifies the
    signature and claims and returns valid and claims (no idsMatch). Optionally supply ID material to
    compare membership/order only; idsHash compares the supplied digest without examining a dataset,
    while ids/csv are examined server-side. The embedded CSV receipt is ignored.

    Args:
        body (Any): Signed delivery receipts identify receiving accounts and ordered item IDs
            only. They do not attest item content or identify a publisher.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Union['ProvenanceVerificationResponseType0', 'ProvenanceVerificationResponseType1']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
