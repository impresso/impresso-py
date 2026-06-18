import asyncio

import pytest
import httpx

from impresso.api_client import Client
from impresso.api_client.api.reference_data import get_data_sources_csv_export
from impresso.api_client.retry import AsyncRetryingClient, RetryingClient


def _client_with_responses(
    responses: list[httpx.Response],
) -> tuple[Client, list[httpx.Request]]:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        response = responses.pop(0)
        return httpx.Response(
            response.status_code,
            headers=response.headers,
            content=response.content,
            request=request,
        )

    client = Client(
        base_url="https://example.test",
        httpx_args={"transport": httpx.MockTransport(handler)},
    )
    return client, requests


def _response(
    status_code: int,
    content: bytes | str = b"",
    headers: dict[str, str] | None = None,
) -> httpx.Response:
    if isinstance(content, str):
        content = content.encode()
    return httpx.Response(status_code, headers=headers, content=content)


def _disable_sync_sleep(client: Client) -> list[float]:
    delays: list[float] = []
    httpx_client = client.get_httpx_client()
    assert isinstance(httpx_client, RetryingClient)
    httpx_client._sleep = delays.append
    return delays


async def _disable_async_sleep(client: Client) -> list[float]:
    delays: list[float] = []
    httpx_client = client.get_async_httpx_client()
    assert isinstance(httpx_client, AsyncRetryingClient)

    async def sleep(delay: float) -> None:
        delays.append(delay)

    httpx_client._sleep = sleep
    return delays


def test_retries_500_responses_then_returns_success(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
):
    monkeypatch.setattr(
        "impresso.api_client.retry.random.uniform", lambda _min, _max: 0
    )
    client, requests = _client_with_responses(
        [
            _response(500, b'{"type":"error","title":"Error","status":500}'),
            _response(500, b'{"type":"error","title":"Error","status":500}'),
            _response(200, "id,label\n1,Source\n"),
        ]
    )
    delays = _disable_sync_sleep(client)

    result = get_data_sources_csv_export.sync(client=client)

    assert result == "id,label\n1,Source\n"
    assert len(requests) == 3
    assert delays == [1.0, 2.0]
    captured = capsys.readouterr()
    assert "☕ I will try again in 1.0s (1/5)" in captured.out
    assert "☕ I will try again in 2.0s (2/5)" in captured.out
    assert "The API had a wobbly espresso shot" in captured.out
    assert "Reason: HTTP 500 from GET /reference-data/data-sources.csv" in captured.out


def test_retries_418_response(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        "impresso.api_client.retry.random.uniform", lambda _min, _max: 0
    )
    client, requests = _client_with_responses(
        [
            _response(418, b'{"type":"error","title":"Error","status":418}'),
            _response(200, "ok\n"),
        ]
    )
    delays = _disable_sync_sleep(client)

    result = get_data_sources_csv_export.sync(client=client)

    assert result == "ok\n"
    assert len(requests) == 2
    assert delays == [1.0]


def test_retries_429_response_with_backoff(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
):
    monkeypatch.setattr(
        "impresso.api_client.retry.random.uniform", lambda _min, _max: 0
    )
    client, requests = _client_with_responses(
        [
            _response(
                429, b'{"type":"error","title":"Too Many Requests","status":429}'
            ),
            _response(200, "ok\n"),
        ]
    )
    delays = _disable_sync_sleep(client)

    result = get_data_sources_csv_export.sync(client=client)

    assert result == "ok\n"
    assert len(requests) == 2
    assert delays == [1.0]
    captured = capsys.readouterr()
    assert "☕ I will try again in 1.0s (1/5)" in captured.out
    assert "The API asked us to slow down the pour" in captured.out
    assert "Reason: HTTP 429 from GET /reference-data/data-sources.csv" in captured.out


def test_retries_429_response_with_retry_after_header(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
):
    monkeypatch.setattr(
        "impresso.api_client.retry.random.uniform", lambda _min, _max: 0
    )
    client, requests = _client_with_responses(
        [
            _response(
                429,
                b'{"type":"error","title":"Too Many Requests","status":429}',
                {"retry-after": "7"},
            ),
            _response(200, "ok\n"),
        ]
    )
    delays = _disable_sync_sleep(client)

    result = get_data_sources_csv_export.sync(client=client)

    assert result == "ok\n"
    assert len(requests) == 2
    assert delays == [7.0]
    captured = capsys.readouterr()
    assert "☕ I will try again in 7.0s (1/5)" in captured.out
    assert "The API asked us to slow down the pour" in captured.out


def test_exhausting_429_retries_prints_rate_limit_message(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
):
    monkeypatch.setattr(
        "impresso.api_client.retry.random.uniform", lambda _min, _max: 0
    )
    client, requests = _client_with_responses(
        [
            _response(
                429,
                b'{"type":"error","title":"Too Many Requests","status":429}',
            )
            for _ in range(6)
        ]
    )
    delays = _disable_sync_sleep(client)

    result = get_data_sources_csv_export.sync_detailed(client=client)

    assert result.status_code == 429
    assert len(requests) == 6
    assert delays == [1.0, 2.0, 4.0, 8.0, 16.0]
    captured = capsys.readouterr()
    assert "the API is still asking us to slow down" in captured.out
    assert "Please retry in a few minutes" in captured.out
    assert "contact the Impresso team" in captured.out
    assert "espresso queue has become a very tiny traffic jam" in captured.out
    assert "Reason: HTTP 429 for GET /reference-data/data-sources.csv" in captured.out


@pytest.mark.parametrize("status_code", [401, 403])
def test_retries_html_auth_responses(status_code: int, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        "impresso.api_client.retry.random.uniform", lambda _min, _max: 0
    )
    client, requests = _client_with_responses(
        [
            _response(
                status_code,
                "<!doctype html><html><body>blocked</body></html>",
                {"content-type": "text/html"},
            ),
            _response(200, "ok\n"),
        ]
    )
    delays = _disable_sync_sleep(client)

    result = get_data_sources_csv_export.sync(client=client)

    assert result == "ok\n"
    assert len(requests) == 2
    assert delays == [1.0]


@pytest.mark.parametrize("status_code", [401, 403])
def test_does_not_retry_json_auth_responses(
    status_code: int, capsys: pytest.CaptureFixture[str]
):
    client, requests = _client_with_responses(
        [
            _response(
                status_code,
                b'{"type":"auth","title":"Auth error","status":401}',
                {"content-type": "application/json"},
            ),
            _response(200, "should not be used\n"),
        ]
    )
    delays = _disable_sync_sleep(client)

    result = get_data_sources_csv_export.sync(client=client)

    assert result is None
    assert len(requests) == 1
    assert delays == []
    assert capsys.readouterr().out == ""


def test_exhausting_retries_returns_final_response(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
):
    monkeypatch.setattr(
        "impresso.api_client.retry.random.uniform", lambda _min, _max: 0
    )
    client, requests = _client_with_responses(
        [
            _response(500, b'{"type":"error","title":"Error","status":500}')
            for _ in range(6)
        ]
    )
    delays = _disable_sync_sleep(client)

    result = get_data_sources_csv_export.sync(client=client)

    assert result.status == 500
    assert len(requests) == 6
    assert delays == [1.0, 2.0, 4.0, 8.0, 16.0]
    captured = capsys.readouterr()
    assert "Sorry, I tried a few times" in captured.out
    assert "Please retry in a few minutes" in captured.out
    assert "contact the Impresso team" in captured.out
    assert "espresso tamper has officially filed a complaint" in captured.out
    assert "Reason: HTTP 500 for GET /reference-data/data-sources.csv" in captured.out


def test_retry_after_header_overrides_backoff(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        "impresso.api_client.retry.random.uniform", lambda _min, _max: 0
    )
    client, _requests = _client_with_responses(
        [
            _response(
                503,
                b'{"type":"error","title":"Error","status":503}',
                {"retry-after": "3"},
            ),
            _response(200, "ok\n"),
        ]
    )
    delays = _disable_sync_sleep(client)

    result = get_data_sources_csv_export.sync(client=client)

    assert result == "ok\n"
    assert delays == [3.0]


def test_retries_post_request_with_json_body(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        "impresso.api_client.retry.random.uniform", lambda _min, _max: 0
    )
    bodies: list[bytes] = []

    def handler(request: httpx.Request) -> httpx.Response:
        bodies.append(request.content)
        status_code = 500 if len(bodies) == 1 else 200
        return httpx.Response(status_code, content=b"ok", request=request)

    client = Client(
        base_url="https://example.test",
        httpx_args={"transport": httpx.MockTransport(handler)},
    )
    delays = _disable_sync_sleep(client)

    response = client.get_httpx_client().post("/collections", json={"name": "demo"})

    assert response.status_code == 200
    assert bodies == [b'{"name": "demo"}', b'{"name": "demo"}']
    assert delays == [1.0]


def test_retries_read_error_then_returns_success(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
):
    monkeypatch.setattr(
        "impresso.api_client.retry.random.uniform", lambda _min, _max: 0
    )
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if len(requests) == 1:
            raise httpx.ReadError("[Errno 54] Connection reset by peer")
        return httpx.Response(200, content=b"ok\n", request=request)

    client = Client(
        base_url="https://example.test",
        httpx_args={"transport": httpx.MockTransport(handler)},
    )
    delays = _disable_sync_sleep(client)

    result = get_data_sources_csv_export.sync(client=client)

    assert result == "ok\n"
    assert len(requests) == 2
    assert delays == [1.0]
    captured = capsys.readouterr()
    assert "☕ I will try again in 1.0s (1/5)" in captured.out
    assert "The API spilled the milk mid-pour" in captured.out
    assert "Reason: ReadError for GET /reference-data/data-sources.csv" in captured.out
    assert "Connection reset by peer" in captured.out


def test_exhausting_read_error_retries_raises_original_error(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
):
    monkeypatch.setattr(
        "impresso.api_client.retry.random.uniform", lambda _min, _max: 0
    )
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        raise httpx.ReadError("[Errno 54] Connection reset by peer")

    client = Client(
        base_url="https://example.test",
        httpx_args={"transport": httpx.MockTransport(handler)},
    )
    delays = _disable_sync_sleep(client)

    with pytest.raises(httpx.ReadError, match="Connection reset by peer"):
        get_data_sources_csv_export.sync(client=client)

    assert len(requests) == 6
    assert delays == [1.0, 2.0, 4.0, 8.0, 16.0]
    captured = capsys.readouterr()
    assert "Sorry, I tried a few times" in captured.out
    assert "Please retry in a few minutes" in captured.out
    assert "contact the Impresso team" in captured.out
    assert "Reason: ReadError" in captured.out
    assert "Connection reset by peer" in captured.out


def test_async_retries_html_auth_response(monkeypatch: pytest.MonkeyPatch):
    async def run_test() -> None:
        delays = await _disable_async_sleep(client)

        result = await get_data_sources_csv_export.asyncio(client=client)

        assert result == "ok\n"
        assert len(requests) == 2
        assert delays == [1.0]

    monkeypatch.setattr(
        "impresso.api_client.retry.random.uniform", lambda _min, _max: 0
    )
    client, requests = _client_with_responses(
        [
            _response(401, "<html>blocked</html>", {"content-type": "text/html"}),
            _response(200, "ok\n"),
        ]
    )

    asyncio.run(run_test())


def test_async_retries_read_error_then_returns_success(
    monkeypatch: pytest.MonkeyPatch,
):
    async def run_test() -> None:
        delays = await _disable_async_sleep(client)

        result = await get_data_sources_csv_export.asyncio(client=client)

        assert result == "ok\n"
        assert len(requests) == 2
        assert delays == [1.0]

    monkeypatch.setattr(
        "impresso.api_client.retry.random.uniform", lambda _min, _max: 0
    )
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if len(requests) == 1:
            raise httpx.ReadError("[Errno 54] Connection reset by peer")
        return httpx.Response(200, content=b"ok\n", request=request)

    client = Client(
        base_url="https://example.test",
        httpx_args={"transport": httpx.MockTransport(handler)},
    )

    asyncio.run(run_test())


def test_async_does_not_retry_json_auth_response(capsys: pytest.CaptureFixture[str]):
    async def run_test() -> None:
        delays = await _disable_async_sleep(client)

        result = await get_data_sources_csv_export.asyncio(client=client)

        assert result is None
        assert len(requests) == 1
        assert delays == []
        assert capsys.readouterr().out == ""

    client, requests = _client_with_responses(
        [
            _response(
                403,
                b'{"type":"auth","title":"Auth error","status":403}',
                {"content-type": "application/json"},
            ),
            _response(200, "should not be used\n"),
        ]
    )

    asyncio.run(run_test())
