from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.impresso_image_embedding_request_model import ImpressoImageEmbeddingRequestModel
from ..models.impresso_image_embedding_request_search_target import ImpressoImageEmbeddingRequestSearchTarget
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImpressoImageEmbeddingRequest")


@_attrs_define
class ImpressoImageEmbeddingRequest:
    """Body of a request to the Impresso Image Embedding endpoint

    Attributes:
        search_target (ImpressoImageEmbeddingRequestSearchTarget): Which embedding space the embedding is going to be
            used in
        bytes_ (str): Base64-encoded image bytes. JPG and PNG formats are supported.
        model (Union[Unset, ImpressoImageEmbeddingRequestModel]): Embedding model to use. Must be compatible with
            `searchTarget`: `image` supports `dinov2-1024` (default); `multimodal` supports `openclip-768` (default) and
            `siglip2-768`. When not provided, the default model for the `searchTarget` is used.
    """

    search_target: ImpressoImageEmbeddingRequestSearchTarget
    bytes_: str
    model: Union[Unset, ImpressoImageEmbeddingRequestModel] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        search_target = self.search_target.value

        bytes_ = self.bytes_

        model: Union[Unset, str] = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "searchTarget": search_target,
                "bytes": bytes_,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        search_target = ImpressoImageEmbeddingRequestSearchTarget(d.pop("searchTarget"))

        bytes_ = d.pop("bytes")

        _model = d.pop("model", UNSET)
        model: Union[Unset, ImpressoImageEmbeddingRequestModel]
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = ImpressoImageEmbeddingRequestModel(_model)

        impresso_image_embedding_request = cls(
            search_target=search_target,
            bytes_=bytes_,
            model=model,
        )

        return impresso_image_embedding_request
