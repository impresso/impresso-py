import base64
from typing import Annotated, cast
from urllib.parse import urlparse

import httpx
from pandas import DataFrame, json_normalize

from impresso.api_client.api.tools import (
    perform_image_embedding,
    perform_ner,
    perform_text_embedding,
)
from impresso.api_client.models.impresso_embedding_response import (
    ImpressoEmbeddingResponse,
)
from impresso.api_client.models.impresso_image_embedding_request import (
    ImpressoImageEmbeddingRequest,
)
from impresso.api_client.models.impresso_image_embedding_request_search_target import (
    ImpressoImageEmbeddingRequestSearchTarget,
    ImpressoImageEmbeddingRequestSearchTargetLiteral,
)
from impresso.api_client.models.impresso_named_entity_recognition_request import (
    ImpressoNamedEntityRecognitionRequest,
)
from impresso.api_client.models.impresso_named_entity_recognition_request_method import (
    ImpressoNamedEntityRecognitionRequestMethod,
)
from impresso.api_client.models.impresso_text_embedding_request import (
    ImpressoTextEmbeddingRequest,
)
from impresso.api_client.models.impresso_text_embedding_request_search_target import (
    ImpressoTextEmbeddingRequestSearchTarget,
    ImpressoTextEmbeddingRequestSearchTargetLiteral,
)
from impresso.api_client.types import UNSET
from impresso.api_models import ImpressoNerResponse
from impresso.data_container import DataContainer
from impresso.resources.base import Resource
from impresso.util.error import raise_for_error
from impresso.util.py import get_enum_from_literal

Base64Str = Annotated[str, "base64-encoded string"]
Embedding = Annotated[str, "base64-encoded string with model prefix"]


def is_url(string: str) -> bool:
    """Check if a string is a valid URL."""
    try:
        parsed = urlparse(string)
        return parsed.scheme in ("http", "https", "ftp", "ftps") and bool(parsed.netloc)
    except Exception:
        return False


class ImpressoNerSchema(ImpressoNerResponse):
    """Schema for the find entities response."""

    pass


class NerContainer(DataContainer):
    """Name entity recognition result container."""

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        data = self._data.to_dict()["entities"]
        if len(data):
            return json_normalize(self._data.to_dict()["entities"]).set_index("id")
        return DataFrame()

    @property
    def total(self) -> int:
        """Total number of results."""
        return len(self.raw.get("entities", []))

    @property
    def limit(self) -> int:
        """Page size."""
        return len(self.raw.get("entities", []))

    @property
    def offset(self) -> int:
        """Page offset."""
        return 0

    @property
    def size(self) -> int:
        """Current page size."""
        return len(self.raw.get("entities", []))


class ToolsResource(Resource):
    """Various helper tools"""

    name = "tools"

    def ner(self, text: str) -> NerContainer:
        """Named Entity Recognition

        This method is faster than `ner_nel` but does not provide any linking to external resources.

        Args:
            text (str): Text to process

        Returns:
            NerContainer: List of named entities
        """
        result = perform_ner.sync(
            client=self._api_client,
            body=ImpressoNamedEntityRecognitionRequest(
                text=text, method=ImpressoNamedEntityRecognitionRequestMethod.NER
            ),
        )
        raise_for_error(result)

        return NerContainer(
            result,
            ImpressoNerSchema,
            web_app_search_result_url=None,
        )

    def ner_nel(self, text: str) -> NerContainer:
        """Named Entity Recognition and Named Entity Linking

        This method is slower than `ner` but provides linking to external resources.

        Args:
            text (str): Text to process

        Returns:
            NerContainer: List of named entities
        """
        result = perform_ner.sync(
            client=self._api_client,
            body=ImpressoNamedEntityRecognitionRequest(
                text=text, method=ImpressoNamedEntityRecognitionRequestMethod.NER_NEL
            ),
        )
        raise_for_error(result)

        return NerContainer(
            result,
            ImpressoNerSchema,
            web_app_search_result_url=None,
        )

    def nel(self, text: str) -> NerContainer:
        """Named Entity Linking

        This method requires named entities to be enclosed in tags: [START]entity[END].

        Args:
            text (str): Text to process

        Returns:
            NerContainer: List of named entities
        """
        result = perform_ner.sync(
            client=self._api_client,
            body=ImpressoNamedEntityRecognitionRequest(
                text=text, method=ImpressoNamedEntityRecognitionRequestMethod.NEL
            ),
        )
        raise_for_error(result)

        return NerContainer(
            result,
            ImpressoNerSchema,
            web_app_search_result_url=None,
        )

    def embed_image(
        self,
        image: bytes | Base64Str | str,
        target: ImpressoImageEmbeddingRequestSearchTargetLiteral,
    ) -> Embedding:
        """Embed an image into a vector space.

        Args:
            image (bytes | Base64Str | str): Image to embed. Can be raw bytes, a base64-encoded string, or a URL to an image.
            target (ImpressoImageEmbeddingRequestSearchTargetLiteral): Target collection to embed the image into. Currently, only "image" is supported.

        Returns:
            list[float]: The image embedding as a list of floats.
        """
        image_as_base64: str
        if isinstance(image, bytes):
            image_as_base64 = base64.b64encode(image).decode("utf-8")
        elif is_url(image):
            response = httpx.get(image)
            response.raise_for_status()
            image_as_base64 = base64.b64encode(response.content).decode("utf-8")
        else:
            image_as_base64 = image  # assume it's already a base64-encoded string

        search_target = get_enum_from_literal(
            target,
            ImpressoImageEmbeddingRequestSearchTarget,
        )
        if search_target == UNSET:
            raise ValueError(f"Invalid search target: {target}")

        result = perform_image_embedding.sync(
            client=self._api_client,
            body=ImpressoImageEmbeddingRequest(
                bytes_=image_as_base64,
                search_target=cast(
                    ImpressoImageEmbeddingRequestSearchTarget, search_target
                ),
            ),
        )
        raise_for_error(result)
        if isinstance(result, ImpressoEmbeddingResponse):
            return cast(str, result.embedding)
        raise ValueError("Unexpected response format")

    def embed_text(
        self,
        text: str,
        target: ImpressoTextEmbeddingRequestSearchTargetLiteral,
    ) -> Embedding:
        """Embed text into a vector space.

        Args:
            text (str): Text to embed.
            target (ImpressoTextEmbeddingRequestSearchTargetLiteral): Target collection to embed the text into.

        Returns:
            list[float]: The text embedding as a list of floats.
        """
        search_target = get_enum_from_literal(
            target,
            ImpressoTextEmbeddingRequestSearchTarget,
        )
        if search_target == UNSET:
            raise ValueError(f"Invalid search target: {target}")

        result = perform_text_embedding.sync(
            client=self._api_client,
            body=ImpressoTextEmbeddingRequest(
                text=text,
                search_target=cast(
                    ImpressoTextEmbeddingRequestSearchTarget, search_target
                ),
            ),
        )
        raise_for_error(result)
        if isinstance(result, ImpressoEmbeddingResponse):
            return cast(str, result.embedding)
        raise ValueError("Unexpected response format")
