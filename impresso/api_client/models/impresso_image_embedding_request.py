from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.impresso_image_embedding_request_search_target import ImpressoImageEmbeddingRequestSearchTarget

T = TypeVar("T", bound="ImpressoImageEmbeddingRequest")


@_attrs_define
class ImpressoImageEmbeddingRequest:
    """Body of a request to the Impresso Image Embedding endpoint

    Attributes:
        search_target (ImpressoImageEmbeddingRequestSearchTarget): Where the embedding is going to be used
        bytes_ (str): Base64-encoded image bytes. JPG and PNG formats are supported.
    """

    search_target: ImpressoImageEmbeddingRequestSearchTarget
    bytes_: str

    def to_dict(self) -> Dict[str, Any]:
        search_target = self.search_target.value

        bytes_ = self.bytes_

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "searchTarget": search_target,
                "bytes": bytes_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        search_target = ImpressoImageEmbeddingRequestSearchTarget(d.pop("searchTarget"))

        bytes_ = d.pop("bytes")

        impresso_image_embedding_request = cls(
            search_target=search_target,
            bytes_=bytes_,
        )

        return impresso_image_embedding_request
