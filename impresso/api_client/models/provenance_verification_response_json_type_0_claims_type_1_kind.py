from enum import Enum
from typing import Literal


class ProvenanceVerificationResponseJsonType0ClaimsType1Kind(str, Enum):
    EXPORT = "export"

    def __str__(self) -> str:
        return str(self.value)


ProvenanceVerificationResponseJsonType0ClaimsType1KindLiteral = Literal["export",]
