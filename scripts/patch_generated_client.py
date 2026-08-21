"""Re-apply the retry wiring to the generated `impresso/api_client/client.py`.

`openapi-python-client` regenerates `impresso/api_client` from scratch, which
wipes any manual edits. This script is run at the end of
`scripts/generate_openapi_client.sh` so the generated clients keep using the
retrying httpx clients from `impresso.util.retry`.
"""

import sys
from pathlib import Path

CLIENT_FILE = Path(__file__).resolve().parent.parent / "impresso" / "api_client" / "client.py"

IMPORT_ANCHOR = "from attrs import define, evolve, field\n"
IMPORT_LINE = "from impresso.util.retry import AsyncRetryingClient, RetryingClient\n"

REPLACEMENTS = [
    ("self._client = httpx.Client(", "self._client = RetryingClient("),
    (
        "self._async_client = httpx.AsyncClient(",
        "self._async_client = AsyncRetryingClient(",
    ),
]


def main() -> int:
    source = CLIENT_FILE.read_text()

    if IMPORT_LINE not in source:
        if IMPORT_ANCHOR not in source:
            print(f"Could not find import anchor in {CLIENT_FILE}", file=sys.stderr)
            return 1
        source = source.replace(IMPORT_ANCHOR, IMPORT_ANCHOR + "\n" + IMPORT_LINE, 1)

    for old, new in REPLACEMENTS:
        if old not in source and new not in source:
            print(f"Could not find {old!r} in {CLIENT_FILE}", file=sys.stderr)
            return 1
        source = source.replace(old, new)

    CLIENT_FILE.write_text(source)
    print(f"Patched {CLIENT_FILE} to use the retrying httpx clients.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
