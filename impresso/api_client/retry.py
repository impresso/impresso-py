"""Retry-aware HTTP clients for generated API endpoint calls.

At a glance:
- This module is used by ``Client`` and ``AuthenticatedClient`` when they build
  their internal httpx clients, so generated endpoint functions automatically get
  retry behavior without changing their public API.
- Retried responses are server-side failures (5xx), rate limits (429), teapots
  (418), and WAF-looking 401/403 responses whose bodies are HTML instead of the
  normal JSON auth errors.
- Retried transport failures are currently limited to ``httpx.ReadError``, which
  covers connection resets such as "[Errno 54] Connection reset by peer".
- Each retry waits with exponential backoff, small jitter, and ``Retry-After``
  support when the API provides it.
- Console messages are intentionally user-facing: they say what will happen next
  first, then explain why, with gentle barista-flavored humor.
- If all retries are exhausted, the final HTTP response is returned as usual, or
  the original transport exception is re-raised after one final user-facing hint.
"""

from __future__ import annotations

import asyncio
import random
import time
from email.utils import parsedate_to_datetime
from typing import Callable

import httpx

MAX_RETRIES = 5
MAX_ATTEMPTS = MAX_RETRIES + 1
BASE_BACKOFF_SECONDS = 1.0
MAX_BACKOFF_SECONDS = 16.0
JITTER_SECONDS = 0.25
RETRYABLE_AUTH_STATUSES = {401, 403}
RETRYABLE_EXCEPTIONS = (httpx.ReadError,)


def _response_looks_like_html(response: httpx.Response) -> bool:
    content_type = response.headers.get("content-type", "").lower()
    if "html" in content_type:
        return True

    body_start = response.content[:512].lstrip().lower()
    return body_start.startswith(b"<!doctype html") or body_start.startswith(b"<html")


def is_retryable_response(response: httpx.Response) -> bool:
    """Return whether an API response matches the retry policy."""

    if response.status_code >= 500 or response.status_code in {418, 429}:
        return True
    if response.status_code in RETRYABLE_AUTH_STATUSES:
        return _response_looks_like_html(response)
    return False


def _retry_after_seconds(value: str | None) -> float | None:
    if not value:
        return None

    try:
        delay = float(value)
    except ValueError:
        try:
            retry_at = parsedate_to_datetime(value)
        except (TypeError, ValueError):
            return None
        delay = retry_at.timestamp() - time.time()

    return max(0.0, min(delay, MAX_BACKOFF_SECONDS))


def _backoff_seconds(response: httpx.Response, retry_number: int) -> float:
    retry_after = _retry_after_seconds(response.headers.get("retry-after"))
    if retry_after is not None:
        return retry_after

    exponential_backoff = min(
        BASE_BACKOFF_SECONDS * (2 ** (retry_number - 1)),
        MAX_BACKOFF_SECONDS,
    )
    return min(
        exponential_backoff + random.uniform(0, JITTER_SECONDS), MAX_BACKOFF_SECONDS
    )


def _exception_backoff_seconds(retry_number: int) -> float:
    exponential_backoff = min(
        BASE_BACKOFF_SECONDS * (2 ** (retry_number - 1)),
        MAX_BACKOFF_SECONDS,
    )
    return min(
        exponential_backoff + random.uniform(0, JITTER_SECONDS), MAX_BACKOFF_SECONDS
    )


def _format_url(request: httpx.Request) -> str:
    return request.url.raw_path.decode("ascii", errors="ignore") or str(request.url)


def _response_retry_explanation(response: httpx.Response) -> str:
    if response.status_code == 429:
        return "The API asked us to slow down the pour."
    return "The API had a wobbly espresso shot."


def _print_retry_message(
    *,
    request: httpx.Request,
    response: httpx.Response,
    retry_number: int,
    delay_seconds: float,
) -> None:
    print(
        "☕ I will try again "
        f"in {delay_seconds:.1f}s ({retry_number}/{MAX_RETRIES}). "
        f"{_response_retry_explanation(response)} "
        f"Reason: HTTP {response.status_code} from {request.method} "
        f"{_format_url(request)}."
    )


def _print_retry_exception_message(
    *,
    request: httpx.Request,
    exception: Exception,
    retry_number: int,
    delay_seconds: float,
) -> None:
    print(
        "☕ I will try again "
        f"in {delay_seconds:.1f}s ({retry_number}/{MAX_RETRIES}). "
        "The API spilled the milk mid-pour. "
        f"Reason: {exception.__class__.__name__} for {request.method} "
        f"{_format_url(request)} ({exception})."
    )


def _print_retries_exhausted_message(
    *,
    request: httpx.Request,
    reason: str,
) -> None:
    if reason == "HTTP 429":
        advice = (
            "☕ Sorry, the API is still asking us to slow down. "
            "Please retry in a few minutes. If it keeps happening, contact the "
            "Impresso team. My espresso queue has become a very tiny traffic jam. "
        )
    else:
        advice = (
            "☕ Sorry, I tried a few times and the API still is not cooperating. "
            "Please retry in a few minutes. If it keeps happening, contact the "
            "Impresso team. My espresso tamper has officially filed a complaint. "
        )
    print(f"{advice}Reason: {reason} for {request.method} {_format_url(request)}.")


class RetryingClient(httpx.Client):
    """Synchronous httpx client that retries flaky Impresso API responses."""

    def __init__(
        self,
        *args: object,
        sleep: Callable[[float], None] = time.sleep,
        **kwargs: object,
    ) -> None:
        super().__init__(*args, **kwargs)
        self._sleep = sleep

    def send(self, request: httpx.Request, **kwargs: object) -> httpx.Response:
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                response = super().send(request, **kwargs)
            except RETRYABLE_EXCEPTIONS as exc:
                if attempt == MAX_ATTEMPTS:
                    _print_retries_exhausted_message(
                        request=request,
                        reason=f"{exc.__class__.__name__} ({exc})",
                    )
                    raise

                retry_number = attempt
                delay_seconds = _exception_backoff_seconds(retry_number)
                _print_retry_exception_message(
                    request=request,
                    exception=exc,
                    retry_number=retry_number,
                    delay_seconds=delay_seconds,
                )
                self._sleep(delay_seconds)
                continue

            retryable_response = is_retryable_response(response)
            if attempt == MAX_ATTEMPTS:
                if retryable_response:
                    response.read()
                    _print_retries_exhausted_message(
                        request=request,
                        reason=f"HTTP {response.status_code}",
                    )
                return response
            if not retryable_response:
                return response

            response.read()
            retry_number = attempt
            delay_seconds = _backoff_seconds(response, retry_number)
            _print_retry_message(
                request=request,
                response=response,
                retry_number=retry_number,
                delay_seconds=delay_seconds,
            )
            response.close()
            self._sleep(delay_seconds)

        raise RuntimeError("Retry loop exited unexpectedly")


class AsyncRetryingClient(httpx.AsyncClient):
    """Asynchronous httpx client that retries flaky Impresso API responses."""

    def __init__(
        self,
        *args: object,
        sleep: Callable[[float], object] = asyncio.sleep,
        **kwargs: object,
    ) -> None:
        super().__init__(*args, **kwargs)
        self._sleep = sleep

    async def send(self, request: httpx.Request, **kwargs: object) -> httpx.Response:
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                response = await super().send(request, **kwargs)
            except RETRYABLE_EXCEPTIONS as exc:
                if attempt == MAX_ATTEMPTS:
                    _print_retries_exhausted_message(
                        request=request,
                        reason=f"{exc.__class__.__name__} ({exc})",
                    )
                    raise

                retry_number = attempt
                delay_seconds = _exception_backoff_seconds(retry_number)
                _print_retry_exception_message(
                    request=request,
                    exception=exc,
                    retry_number=retry_number,
                    delay_seconds=delay_seconds,
                )
                await self._sleep(delay_seconds)
                continue

            retryable_response = is_retryable_response(response)
            if attempt == MAX_ATTEMPTS:
                if retryable_response:
                    await response.aread()
                    _print_retries_exhausted_message(
                        request=request,
                        reason=f"HTTP {response.status_code}",
                    )
                return response
            if not retryable_response:
                return response

            await response.aread()
            retry_number = attempt
            delay_seconds = _backoff_seconds(response, retry_number)
            _print_retry_message(
                request=request,
                response=response,
                retry_number=retry_number,
                delay_seconds=delay_seconds,
            )
            await response.aclose()
            await self._sleep(delay_seconds)

        raise RuntimeError("Retry loop exited unexpectedly")


__all__ = [
    "AsyncRetryingClient",
    "RetryingClient",
    "is_retryable_response",
]
