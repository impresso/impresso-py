from enum import Enum
from typing import Literal


class ImpressoNamedEntityRecognitionRequestMethod(str, Enum):
    NER = "ner"
    NER_NEL = "ner-nel"

    def __str__(self) -> str:
        return str(self.value)


ImpressoNamedEntityRecognitionRequestMethodLiteral = Literal[
    "ner",
    "ner-nel",
]
