import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_reuse_passage_article_details import TextReusePassageArticleDetails
    from ..models.text_reuse_passage_cluster_details import TextReusePassageClusterDetails
    from ..models.text_reuse_passage_connected_clusters import TextReusePassageConnectedClusters
    from ..models.text_reuse_passage_issue import TextReusePassageIssue
    from ..models.text_reuse_passage_newspaper import TextReusePassageNewspaper


T = TypeVar("T", bound="TextReusePassage")


@_attrs_define
class TextReusePassage:
    """Represents a passage of text that was identified as a part of a text reuse cluster

    Attributes:
        id (str): ID of the text reuse passage Example: abc123.
        article (TextReusePassageArticleDetails): Details of the article the passage belongs to
        text_reuse_cluster (TextReusePassageClusterDetails): Details of the cluster the passage belongs to
        offset_start (int): Offset of the passage in the article text
        offset_end (int): Offset of the passage in the article text
        content (str): Textual content of the passage
        title (str): Title of the content item (article) where this passage was found
        page_regions (List[str]): Bounding box of the passage in the page
        page_numbers (List[int]): Numbers of the pages where the passage was found
        collections (List[str]): Collection IDs the passage belongs to
        connected_clusters (Union[Unset, TextReusePassageConnectedClusters]): Details of the connected clusters
        is_front (Union[Unset, bool]): TBD
        size (Union[Unset, int]): Size of the passage
        newspaper (Union[Unset, TextReusePassageNewspaper]): Newspaper details
        issue (Union[Unset, TextReusePassageIssue]): Issue details
        date (Union[Unset, datetime.datetime]): Date of the item (article) where this passage was found
    """

    id: str
    article: "TextReusePassageArticleDetails"
    text_reuse_cluster: "TextReusePassageClusterDetails"
    offset_start: int
    offset_end: int
    content: str
    title: str
    page_regions: List[str]
    page_numbers: List[int]
    collections: List[str]
    connected_clusters: Union[Unset, "TextReusePassageConnectedClusters"] = UNSET
    is_front: Union[Unset, bool] = UNSET
    size: Union[Unset, int] = UNSET
    newspaper: Union[Unset, "TextReusePassageNewspaper"] = UNSET
    issue: Union[Unset, "TextReusePassageIssue"] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        article = self.article.to_dict()

        text_reuse_cluster = self.text_reuse_cluster.to_dict()

        offset_start = self.offset_start

        offset_end = self.offset_end

        content = self.content

        title = self.title

        page_regions = self.page_regions

        page_numbers = self.page_numbers

        collections = self.collections

        connected_clusters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.connected_clusters, Unset):
            connected_clusters = self.connected_clusters.to_dict()

        is_front = self.is_front

        size = self.size

        newspaper: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.newspaper, Unset):
            newspaper = self.newspaper.to_dict()

        issue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.issue, Unset):
            issue = self.issue.to_dict()

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "article": article,
                "textReuseCluster": text_reuse_cluster,
                "offsetStart": offset_start,
                "offsetEnd": offset_end,
                "content": content,
                "title": title,
                "pageRegions": page_regions,
                "pageNumbers": page_numbers,
                "collections": collections,
            }
        )
        if connected_clusters is not UNSET:
            field_dict["connectedClusters"] = connected_clusters
        if is_front is not UNSET:
            field_dict["isFront"] = is_front
        if size is not UNSET:
            field_dict["size"] = size
        if newspaper is not UNSET:
            field_dict["newspaper"] = newspaper
        if issue is not UNSET:
            field_dict["issue"] = issue
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.text_reuse_passage_article_details import TextReusePassageArticleDetails
        from ..models.text_reuse_passage_cluster_details import TextReusePassageClusterDetails
        from ..models.text_reuse_passage_connected_clusters import TextReusePassageConnectedClusters
        from ..models.text_reuse_passage_issue import TextReusePassageIssue
        from ..models.text_reuse_passage_newspaper import TextReusePassageNewspaper

        d = src_dict.copy()
        id = d.pop("id")

        article = TextReusePassageArticleDetails.from_dict(d.pop("article"))

        text_reuse_cluster = TextReusePassageClusterDetails.from_dict(d.pop("textReuseCluster"))

        offset_start = d.pop("offsetStart")

        offset_end = d.pop("offsetEnd")

        content = d.pop("content")

        title = d.pop("title")

        page_regions = cast(List[str], d.pop("pageRegions"))

        page_numbers = cast(List[int], d.pop("pageNumbers"))

        collections = cast(List[str], d.pop("collections"))

        _connected_clusters = d.pop("connectedClusters", UNSET)
        connected_clusters: Union[Unset, TextReusePassageConnectedClusters]
        if isinstance(_connected_clusters, Unset):
            connected_clusters = UNSET
        else:
            connected_clusters = TextReusePassageConnectedClusters.from_dict(_connected_clusters)

        is_front = d.pop("isFront", UNSET)

        size = d.pop("size", UNSET)

        _newspaper = d.pop("newspaper", UNSET)
        newspaper: Union[Unset, TextReusePassageNewspaper]
        if isinstance(_newspaper, Unset):
            newspaper = UNSET
        else:
            newspaper = TextReusePassageNewspaper.from_dict(_newspaper)

        _issue = d.pop("issue", UNSET)
        issue: Union[Unset, TextReusePassageIssue]
        if isinstance(_issue, Unset):
            issue = UNSET
        else:
            issue = TextReusePassageIssue.from_dict(_issue)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        text_reuse_passage = cls(
            id=id,
            article=article,
            text_reuse_cluster=text_reuse_cluster,
            offset_start=offset_start,
            offset_end=offset_end,
            content=content,
            title=title,
            page_regions=page_regions,
            page_numbers=page_numbers,
            collections=collections,
            connected_clusters=connected_clusters,
            is_front=is_front,
            size=size,
            newspaper=newspaper,
            issue=issue,
            date=date,
        )

        return text_reuse_passage
