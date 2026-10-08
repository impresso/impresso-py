from enum import Enum
from typing import Literal


class ProvenanceVerificationResponseType0ClaimsType1Kind(str, Enum):
    EXPORT = "export"

    def __str__(self) -> str:
        return str(self.value)


ProvenanceVerificationResponseType0ClaimsType1KindLiteral = Literal["export",]
