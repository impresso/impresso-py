import base64
from unittest.mock import Mock, patch

import pytest

from impresso.api_client.models.impresso_embedding_response import (
    ImpressoEmbeddingResponse,
)
from impresso.protobuf import query_pb2 as pb
from impresso.resources.search import SearchResource
from impresso.resources.tools import ToolsResource
from impresso.structures import NumericRange


@pytest.mark.parametrize(
    "kind,target", [("text", "multimodal"), ("image", "multimodal")]
)
@pytest.mark.parametrize("model", [None, "siglip2-768"])
def test_embedding_model(kind, target, model):
    resource = ToolsResource(Mock())
    with patch(f"impresso.resources.tools.perform_{kind}_embedding.sync") as request:
        request.return_value = ImpressoEmbeddingResponse(embedding="encoded")
        value = "example" if kind == "text" else b"image"
        assert (
            getattr(resource, f"embed_{kind}")(value, target, model=model) == "encoded"
        )
        body = request.call_args.kwargs["body"].to_dict()
        if model is None:
            assert "model" not in body
        else:
            assert body["model"] == model


@pytest.mark.parametrize(
    "method,container,endpoint",
    [
        ("find", "SearchDataContainer", "search"),
        ("facet", "FacetDataContainer", "get_search_facet"),
    ],
)
@pytest.mark.parametrize("inverted", [False, True])
def test_ocr_quality_filter(method, container, endpoint, inverted):
    resource = SearchResource(Mock())
    quality = NumericRange(0.8, 1)
    if inverted:
        quality = ~quality
    with patch(f"impresso.resources.search.{endpoint}.sync") as request, patch(
        f"impresso.resources.search.{container}"
    ) as result, patch("impresso.resources.search.raise_for_error"):
        kwargs = {"facet": "newspaper"} if method == "facet" else {}
        getattr(resource, method)(ocr_quality=quality, **kwargs)
        query = pb.SearchQuery()
        query.ParseFromString(base64.b64decode(request.call_args.kwargs["filters"]))
        assert len(query.filters) == 1
        filter_ = query.filters[0]
        assert filter_.type == pb.TYPE_OCR_QUALITY
        assert list(filter_.q) == ["0.8 TO 1"]
        if inverted:
            assert filter_.context == pb.CONTEXT_EXCLUDE
        else:
            assert not filter_.HasField("context")
        assert result.call_args.kwargs["fetch_method_args"]["ocr_quality"] is quality
