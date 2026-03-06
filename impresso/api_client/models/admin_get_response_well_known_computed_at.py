from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AdminGETResponseWellKnownComputedAt")


@_attrs_define
class AdminGETResponseWellKnownComputedAt:
    """
    Attributes:
        media_sources (Union[None, str]):
        topics (Union[None, str]):
        years (Union[None, str]):
    """

    media_sources: Union[None, str]
    topics: Union[None, str]
    years: Union[None, str]

    def to_dict(self) -> Dict[str, Any]:
        media_sources: Union[None, str]
        media_sources = self.media_sources

        topics: Union[None, str]
        topics = self.topics

        years: Union[None, str]
        years = self.years

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "mediaSources": media_sources,
                "topics": topics,
                "years": years,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_media_sources(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        media_sources = _parse_media_sources(d.pop("mediaSources"))

        def _parse_topics(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        topics = _parse_topics(d.pop("topics"))

        def _parse_years(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        years = _parse_years(d.pop("years"))

        admin_get_response_well_known_computed_at = cls(
            media_sources=media_sources,
            topics=topics,
            years=years,
        )

        return admin_get_response_well_known_computed_at
