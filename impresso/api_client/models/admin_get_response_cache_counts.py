from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AdminGETResponseCacheCounts")


@_attrs_define
class AdminGETResponseCacheCounts:
    """
    Attributes:
        db (int):
        solr (int):
        wikidata (int):
    """

    db: int
    solr: int
    wikidata: int

    def to_dict(self) -> Dict[str, Any]:
        db = self.db

        solr = self.solr

        wikidata = self.wikidata

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "db": db,
                "solr": solr,
                "wikidata": wikidata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        db = d.pop("db")

        solr = d.pop("solr")

        wikidata = d.pop("wikidata")

        admin_get_response_cache_counts = cls(
            db=db,
            solr=solr,
            wikidata=wikidata,
        )

        return admin_get_response_cache_counts
