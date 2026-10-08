from enum import Enum
from typing import Literal


class ProvenanceVerificationResponseJsonType0ClaimsType0Kind(str, Enum):
    API = "api"

    def __str__(self) -> str:
        return str(self.value)


ProvenanceVerificationResponseJsonType0ClaimsType0KindLiteral = Literal["api",]
