from enum import Enum


class GetSearchFacets(str, Enum):
    ACCESSRIGHT = "accessRight"
    COLLECTION = "collection"
    CONTENTLENGTH = "contentLength"
    COUNTRY = "country"
    DATERANGE = "daterange"
    LANGUAGE = "language"
    LOCATION = "location"
    MONTH = "month"
    NAG = "nag"
    NEWSPAPER = "newspaper"
    PARTNER = "partner"
    PERSON = "person"
    TOPIC = "topic"
    TYPE = "type"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
