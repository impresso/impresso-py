from enum import Enum
from typing import Literal


class GetSearchFacetId(str, Enum):
    COLLECTION = "collection"
    CONTENTLENGTH = "contentLength"
    COPYRIGHT = "copyright"
    COUNTRY = "country"
    DATADOMAIN = "dataDomain"
    DATERANGE = "daterange"
    LANGUAGE = "language"
    LOCATION = "location"
    MEDIASOURCE = "mediaSource"
    MONTH = "month"
    NAG = "nag"
    NEWSPAPER = "newspaper"
    OCRQUALITY = "ocrQuality"
    ORGANISATION = "organisation"
    PARTNER = "partner"
    PERMISSIONEXPLORE = "permissionExplore"
    PERMISSIONGETIMAGE = "permissionGetImage"
    PERMISSIONGETTRANSCRIPT = "permissionGetTranscript"
    PERSON = "person"
    SOURCEMEDIUM = "sourceMedium"
    SOURCETYPE = "sourceType"
    TOPIC = "topic"
    TYPE = "type"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)


GetSearchFacetIdLiteral = Literal[
    "collection",
    "contentLength",
    "copyright",
    "country",
    "dataDomain",
    "daterange",
    "language",
    "location",
    "mediaSource",
    "month",
    "nag",
    "newspaper",
    "ocrQuality",
    "organisation",
    "partner",
    "permissionExplore",
    "permissionGetImage",
    "permissionGetTranscript",
    "person",
    "sourceMedium",
    "sourceType",
    "topic",
    "type",
    "year",
]
