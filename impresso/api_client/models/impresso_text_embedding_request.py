from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.impresso_text_embedding_request_model import ImpressoTextEmbeddingRequestModel
from ..models.impresso_text_embedding_request_search_target import ImpressoTextEmbeddingRequestSearchTarget
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImpressoTextEmbeddingRequest")


@_attrs_define
class ImpressoTextEmbeddingRequest:
    """Body of a request to the Impresso Text Embedding endpoint

    Attributes:
        search_target (ImpressoTextEmbeddingRequestSearchTarget): Which embedding space the embedding is going to be
            used in
        text (str): Text to be embedded
        model (Union[Unset, ImpressoTextEmbeddingRequestModel]): Embedding model to use. Must be compatible with
            `searchTarget`: `multimodal` supports `openclip-768` (default) and `siglip2-768`; `text` supports only the text
            embedding model configured on the server (default). When not provided, the default model for the `searchTarget`
            is used.
    """

    search_target: ImpressoTextEmbeddingRequestSearchTarget
    text: str
    model: Union[Unset, ImpressoTextEmbeddingRequestModel] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        search_target = self.search_target.value

        text = self.text

        model: Union[Unset, str] = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "searchTarget": search_target,
                "text": text,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        search_target = ImpressoTextEmbeddingRequestSearchTarget(d.pop("searchTarget"))

        text = d.pop("text")

        _model = d.pop("model", UNSET)
        model: Union[Unset, ImpressoTextEmbeddingRequestModel]
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = ImpressoTextEmbeddingRequestModel(_model)

        impresso_text_embedding_request = cls(
            search_target=search_target,
            text=text,
            model=model,
        )

        return impresso_text_embedding_request
