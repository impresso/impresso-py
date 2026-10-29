from enum import Enum
from typing import Literal


class ProvenanceVerificationResponseProvenanceVerificationExportClaimsKind(str, Enum):
    EXPORT = "export"

    def __str__(self) -> str:
        return str(self.value)


ProvenanceVerificationResponseProvenanceVerificationExportClaimsKindLiteral = Literal["export",]
