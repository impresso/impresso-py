from enum import Enum
from typing import Literal


class AdminPatchRequestAction(str, Enum):
    CLEAR_DB_CACHE = "clear-db-cache"
    CLEAR_SOLR_CACHE = "clear-solr-cache"
    CLEAR_WIKIDATA_CACHE = "clear-wikidata-cache"
    REBUILD_WELL_KNOWN_CACHE = "rebuild-well-known-cache"

    def __str__(self) -> str:
        return str(self.value)


AdminPatchRequestActionLiteral = Literal[
    "clear-db-cache",
    "clear-solr-cache",
    "clear-wikidata-cache",
    "rebuild-well-known-cache",
]
