from enum import Enum
from typing import Literal


class GetImagesFacetId(str, Enum):
    COLLECTION = "collection"
    IMAGECOMMUNICATIONGOAL = "imageCommunicationGoal"
    IMAGECONTENTTYPE = "imageContentType"
    IMAGETECHNIQUE = "imageTechnique"
    IMAGEVISUALCONTENT = "imageVisualContent"
    NEWSPAPER = "newspaper"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)


GetImagesFacetIdLiteral = Literal[
    "collection",
    "imageCommunicationGoal",
    "imageContentType",
    "imageTechnique",
    "imageVisualContent",
    "newspaper",
    "year",
]
