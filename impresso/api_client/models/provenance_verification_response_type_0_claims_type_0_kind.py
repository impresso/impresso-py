from enum import Enum
from typing import Literal


class ProvenanceVerificationResponseType0ClaimsType0Kind(str, Enum):
    API = "api"

    def __str__(self) -> str:
        return str(self.value)


ProvenanceVerificationResponseType0ClaimsType0KindLiteral = Literal["api",]
