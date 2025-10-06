from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.impresso_text_embedding_request_search_target import ImpressoTextEmbeddingRequestSearchTarget

T = TypeVar("T", bound="ImpressoTextEmbeddingRequest")


@_attrs_define
class ImpressoTextEmbeddingRequest:
    """Body of a request to the Impresso Text Embedding endpoint

    Attributes:
        search_target (ImpressoTextEmbeddingRequestSearchTarget): Where the embedding is going to be used
        text (str): Text to be embedded
    """

    search_target: ImpressoTextEmbeddingRequestSearchTarget
    text: str

    def to_dict(self) -> Dict[str, Any]:
        search_target = self.search_target.value

        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "searchTarget": search_target,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        search_target = ImpressoTextEmbeddingRequestSearchTarget(d.pop("searchTarget"))

        text = d.pop("text")

        impresso_text_embedding_request = cls(
            search_target=search_target,
            text=text,
        )

        return impresso_text_embedding_request
