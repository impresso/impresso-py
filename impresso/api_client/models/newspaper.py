from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.newspaper_issue import NewspaperIssue
    from ..models.newspaper_property import NewspaperProperty


T = TypeVar("T", bound="Newspaper")


@_attrs_define
class Newspaper:
    """A newspaper

    Attributes:
        uid (str): The unique identifier of the newspaper
        acronym (str): The acronym of the newspaper
        labels (List[str]): The labels of the newspaper
        languages (List[str]): Language codes of the languages used in the newspaper
        included (bool): TODO
        name (str): Title of the newspaper
        end_year (str): Last available year of the newspaper articles
        start_year (str): First available year of the newspaper articles
        first_issue (NewspaperIssue):
        last_issue (NewspaperIssue):
        count_articles (int): The number of articles in the newspaper
        count_issues (int): The number of issues in the newspaper
        count_pages (int): The number of pages in the newspaper
        delta_year (int): The number of years of the newspaper available
        properties (Union[Unset, List['NewspaperProperty']]): TODO
        fetched (Union[Unset, bool]): TODO
    """

    uid: str
    acronym: str
    labels: List[str]
    languages: List[str]
    included: bool
    name: str
    end_year: str
    start_year: str
    first_issue: "NewspaperIssue"
    last_issue: "NewspaperIssue"
    count_articles: int
    count_issues: int
    count_pages: int
    delta_year: int
    properties: Union[Unset, List["NewspaperProperty"]] = UNSET
    fetched: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uid = self.uid

        acronym = self.acronym

        labels = self.labels

        languages = self.languages

        included = self.included

        name = self.name

        end_year = self.end_year

        start_year = self.start_year

        first_issue = self.first_issue.to_dict()

        last_issue = self.last_issue.to_dict()

        count_articles = self.count_articles

        count_issues = self.count_issues

        count_pages = self.count_pages

        delta_year = self.delta_year

        properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        fetched = self.fetched

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "uid": uid,
                "acronym": acronym,
                "labels": labels,
                "languages": languages,
                "included": included,
                "name": name,
                "endYear": end_year,
                "startYear": start_year,
                "firstIssue": first_issue,
                "lastIssue": last_issue,
                "countArticles": count_articles,
                "countIssues": count_issues,
                "countPages": count_pages,
                "deltaYear": delta_year,
            }
        )
        if properties is not UNSET:
            field_dict["properties"] = properties
        if fetched is not UNSET:
            field_dict["fetched"] = fetched

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.newspaper_issue import NewspaperIssue
        from ..models.newspaper_property import NewspaperProperty

        d = src_dict.copy()
        uid = d.pop("uid")

        acronym = d.pop("acronym")

        labels = cast(List[str], d.pop("labels"))

        languages = cast(List[str], d.pop("languages"))

        included = d.pop("included")

        name = d.pop("name")

        end_year = d.pop("endYear")

        start_year = d.pop("startYear")

        first_issue = NewspaperIssue.from_dict(d.pop("firstIssue"))

        last_issue = NewspaperIssue.from_dict(d.pop("lastIssue"))

        count_articles = d.pop("countArticles")

        count_issues = d.pop("countIssues")

        count_pages = d.pop("countPages")

        delta_year = d.pop("deltaYear")

        properties = []
        _properties = d.pop("properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = NewspaperProperty.from_dict(properties_item_data)

            properties.append(properties_item)

        fetched = d.pop("fetched", UNSET)

        newspaper = cls(
            uid=uid,
            acronym=acronym,
            labels=labels,
            languages=languages,
            included=included,
            name=name,
            end_year=end_year,
            start_year=start_year,
            first_issue=first_issue,
            last_issue=last_issue,
            count_articles=count_articles,
            count_issues=count_issues,
            count_pages=count_pages,
            delta_year=delta_year,
            properties=properties,
            fetched=fetched,
        )

        return newspaper
