from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ImpressoEmbeddingResponse")


@_attrs_define
class ImpressoEmbeddingResponse:
    """Body of a response from the Impresso Embedding endpoint

    Attributes:
        embedding (str): Embedding vector, base64-encoded with the model prefix. E.g. <model>:<base64-encoded vector>
    """

    embedding: str

    def to_dict(self) -> Dict[str, Any]:
        embedding = self.embedding

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "embedding": embedding,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        embedding = d.pop("embedding")

        impresso_embedding_response = cls(
            embedding=embedding,
        )

        return impresso_embedding_response
