from enum import Enum
from typing import Literal


class ProvenanceVerificationResponseProvenanceVerificationApiClaimsKind(str, Enum):
    API = "api"

    def __str__(self) -> str:
        return str(self.value)


ProvenanceVerificationResponseProvenanceVerificationApiClaimsKindLiteral = Literal["api",]
