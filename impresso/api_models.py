# generated by datamodel-codegen:
#   filename:  http://localhost:3030/swagger.json

from __future__ import annotations

from datetime import date
from typing import Any, Mapping, Optional, Sequence, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated, Literal


class AuthenticationCreateRequest(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    strategy: Literal['local', 'jwt-app']
    email: Optional[str] = None
    password: Optional[str] = None
    accessToken: Optional[str] = None


class Authentication(BaseModel):
    strategy: Optional[str] = None
    payload: Optional[Mapping[str, Any]] = None


class BaseFind(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    limit: Annotated[
        int, Field(description='The number of items returned in this response')
    ]
    offset: Annotated[
        int,
        Field(
            description='Starting index of the items subset returned in this response'
        ),
    ]
    total: Annotated[
        int, Field(description='The total number of items matching the query')
    ]
    info: Annotated[
        Mapping[str, Any],
        Field(description='Additional information about the response.'),
    ]
    data: Sequence


class BaseUser(BaseModel):
    uid: Annotated[
        str,
        Field(
            examples=['local-dg'],
            pattern='^([a-zA-Z-]+)$',
            title='unique identifier for the user',
        ),
    ]
    username: Annotated[
        str,
        Field(
            examples=['daniele.guido'],
            pattern='^([a-z.]+)$',
            title='unique username for the user for other humans',
        ),
    ]


class CollectableItemsUpdatedResponse(BaseModel):
    totalAdded: Annotated[
        int, Field(description='Total number of items added to the collection')
    ]
    totalRemoved: Annotated[
        int, Field(description='Total number of items removed from the collection')
    ]


class Collection(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    uid: Annotated[str, Field(max_length=50, min_length=2)]
    name: Annotated[str, Field(max_length=50, min_length=2)]
    description: Annotated[str, Field(max_length=500)]
    status: Annotated[
        str,
        Field(
            examples=['PRI'],
            max_length=3,
            min_length=2,
            title='Status of the collection',
        ),
    ]
    creationDate: AwareDatetime
    lastModifiedDate: AwareDatetime
    countItems: Annotated[
        Union[int, str], Field(title='Number of items in the collection')
    ]
    creator: BaseUser
    labels: Optional[Sequence[str]] = None


class Params(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Annotated[Optional[str], Field(None, description='The collection id')]
    status: Annotated[
        Optional[Literal['DEL']], Field(None, description='The status of the operation')
    ]


class Task(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    task_id: Annotated[Optional[str], Field(None, description='The ID of the task')]
    creationDate: Annotated[
        Optional[str], Field(None, description='When task was created')
    ]


class CollectionsRemoveResponse(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    params: Params
    task: Annotated[Task, Field(description='Deletion task details')]


class PersonItem(RootModel[Sequence[Any]]):
    root: Annotated[Sequence[Any], Field(max_length=2, min_length=2)]


class LocationItem(RootModel[Sequence[Any]]):
    root: Annotated[Sequence[Any], Field(max_length=2, min_length=2)]


class Mention(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    person: Optional[Sequence[PersonItem]] = None
    location: Optional[Sequence[LocationItem]] = None


class ContentItemMatch(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    fragment: Annotated[str, Field(description='TODO')]
    coords: Annotated[Optional[Sequence[float]], Field(None, description='TODO')]
    pageUid: Annotated[Optional[str], Field(None, description='TODO')]
    iiif: Annotated[Optional[str], Field(None, description='TODO')]


class ContentItemRegion(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    pageUid: str
    coords: Sequence[float]
    isEmpty: Annotated[bool, Field(description='TODO')]
    iiifFragment: Annotated[Optional[str], Field(None, description='IIIF fragment URL')]
    g: Annotated[Optional[Sequence[str]], Field(None, description='TODO')]


class Entity(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    uid: Annotated[str, Field(description='Unique identifier of the entity')]
    relevance: Annotated[
        int, Field(description='Relevance of the entity in the document')
    ]


class Error(BaseModel):
    type: Annotated[
        AnyUrl,
        Field(
            description='A URI reference [RFC3986] that identifies the problem type.'
        ),
    ]
    title: Annotated[
        str, Field(description='A short, human-readable summary of the problem type.')
    ]
    status: Annotated[
        int, Field(description='The HTTP status code ([RFC7231], Section 6)')
    ]
    detail: Annotated[
        Optional[str],
        Field(
            None,
            description='A human-readable explanation specific to this occurrence of the problem.',
        ),
    ]


class Q(RootModel[str]):
    root: Annotated[str, Field(max_length=500, min_length=2)]


class QItem(RootModel[str]):
    root: Annotated[str, Field(max_length=500, min_length=2)]


class Filter(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    context: Optional[Literal['include', 'exclude']] = 'include'
    op: Optional[Literal['AND', 'OR']] = 'OR'
    type: Annotated[
        str,
        Field(
            description="Possible values are in 'search.validators:eachFilterValidator.type.choices'"
        ),
    ]
    precision: Optional[Literal['fuzzy', 'soft', 'exact', 'partial']] = 'exact'
    q: Optional[Union[Q, Sequence[QItem]]] = None
    daterange: Annotated[
        Optional[str],
        Field(
            None,
            pattern='\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z TO \\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z',
        ),
    ]
    uids: Optional[str] = None
    uid: Optional[str] = None


class Offset(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    start: Annotated[int, Field(description='Start offset of the entity in the text')]
    end: Annotated[int, Field(description='End offset of the entity in the text')]


class Confidence(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    ner: Annotated[
        Optional[float],
        Field(None, description='Confidence score for the named entity recognition'),
    ]
    nel: Annotated[
        Optional[float],
        Field(None, description='Confidence score for the named entity linking'),
    ]


class Wikidata(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Annotated[str, Field(description='Wikidata ID of the entity')]
    wikipediaPageName: Annotated[
        Optional[str], Field(None, description='Wikipedia page name of the entity')
    ]
    wikipediaPageUrl: Annotated[
        Optional[str], Field(None, description='Wikipedia page URL of the entity')
    ]


class ImpressoNerEntity(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Annotated[str, Field(description='ID of the entity')]
    type: Annotated[
        Literal[
            'comp.demonym',
            'comp.function',
            'comp.name',
            'comp.qualifier',
            'comp.title',
            'loc',
            'loc.add.elec',
            'loc.add.phys',
            'loc.adm.nat',
            'loc.adm.reg',
            'loc.adm.sup',
            'loc.adm.town',
            'loc.fac',
            'loc.oro',
            'loc.phys.astro',
            'loc.phys.geo',
            'loc.phys.hydro',
            'loc.unk',
            'org',
            'org.adm',
            'org.ent',
            'org.ent.pressagency',
            'org.ent.pressagency.AFP',
            'org.ent.pressagency.ANSA',
            'org.ent.pressagency.AP',
            'org.ent.pressagency.APA',
            'org.ent.pressagency.ATS-SDA',
            'org.ent.pressagency.Belga',
            'org.ent.pressagency.CTK',
            'org.ent.pressagency.DDP-DAPD',
            'org.ent.pressagency.DNB',
            'org.ent.pressagency.DPA',
            'org.ent.pressagency.Domei',
            'org.ent.pressagency.Europapress',
            'org.ent.pressagency.Extel',
            'org.ent.pressagency.Havas',
            'org.ent.pressagency.Kipa',
            'org.ent.pressagency.Reuters',
            'org.ent.pressagency.SPK-SMP',
            'org.ent.pressagency.Stefani',
            'org.ent.pressagency.TASS',
            'org.ent.pressagency.UP-UPI',
            'org.ent.pressagency.Wolff',
            'org.ent.pressagency.Xinhua',
            'org.ent.pressagency.ag',
            'org.ent.pressagency.unk',
            'pers',
            'pers.coll',
            'pers.ind',
            'pers.ind.articleauthor',
            'prod',
            'prod.doctr',
            'prod.media',
            'time',
            'time.date.abs',
            'time.hour.abs',
            'unk',
        ],
        Field(description='Type of the entity'),
    ]
    surfaceForm: Annotated[
        Optional[str], Field(None, description='Surface form of the entity')
    ]
    offset: Optional[Offset] = None
    isTypeNested: Annotated[
        Optional[bool], Field(None, description='Whether the entity type is nested')
    ]
    confidence: Confidence
    wikidata: Optional[Wikidata] = None
    function: Annotated[
        Optional[str], Field(None, description='Function of the entity')
    ]
    name: Annotated[Optional[str], Field(None, description='Name of the entity')]


class ImpressoNerRequest(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    text: Annotated[
        str,
        Field(
            description='Text to be processed for named entity recognition',
            max_length=3999,
            min_length=1,
        ),
    ]
    method: Annotated[
        Optional[Literal['ner', 'ner-nel', 'nel']],
        Field(
            'ner',
            description='NER method to be used: `ner` (default), `ner-nel` (named entity recognition with named entity linking) and `nel` (linking only - enclose entities in [START] [END] tags).',
        ),
    ]


class ImpressoNerResponse(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    modelId: Annotated[
        str, Field(description='ID of the model used for the named entity recognition')
    ]
    text: Annotated[
        str, Field(description='Text processed for named entity recognition')
    ]
    timestamp: Annotated[
        AwareDatetime,
        Field(description='Timestamp of when named entity recognition was performed'),
    ]
    entities: Sequence[ImpressoNerEntity]


class NewCollection(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    name: Annotated[str, Field(max_length=50, min_length=2)]
    description: Annotated[Optional[str], Field(None, max_length=500)]
    status: Annotated[
        Optional[str],
        Field(
            None,
            examples=['PRI'],
            max_length=3,
            min_length=2,
            title='Status of the collection',
        ),
    ]


class NewspaperIssue(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    uid: Annotated[str, Field(description='The unique identifier of the issue')]
    cover: Annotated[str, Field(description='TODO')]
    labels: Annotated[Sequence[str], Field(description='The labels of the issue')]
    fresh: Annotated[bool, Field(description='TODO')]
    accessRights: Annotated[str, Field(description='TODO: list available options')]
    date: Annotated[
        Optional[AwareDatetime], Field(None, description='The date of the issue')
    ]
    year: Annotated[Optional[str], Field(None, description='The year of the issue')]


class NewspaperProperty(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    name: Annotated[str, Field(description='The name of the property')]
    value: Annotated[str, Field(description='The value of the property')]
    label: Annotated[str, Field(description='The label of the property')]
    isUrl: Annotated[
        Optional[bool], Field(None, description='Whether the value is a URL')
    ]


class Page(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    uid: Annotated[str, Field(description='The unique identifier of the page')]
    num: Annotated[int, Field(description='The number of the page')]
    issueUid: Annotated[str, Field(description='Reference to the article')]
    newspaperUid: Annotated[str, Field(description='Unique ID of the newspaper')]
    iiif: Annotated[str, Field(description='The IIF image file name of the page')]
    iiifThumbnail: Annotated[
        str, Field(description='The IIF image thumbnail file name of the page')
    ]
    accessRights: Annotated[str, Field(description='The access rights code')]
    labels: Annotated[Sequence[str], Field(description='Page labels')]
    hasCoords: Annotated[bool, Field(description='Whether the page has coordinates')]
    hasErrors: Annotated[bool, Field(description='Whether the page has errors')]
    regions: Annotated[
        Sequence[Mapping[str, Any]], Field(description='Regions of the page')
    ]
    obfuscated: Annotated[
        Optional[bool],
        Field(
            None,
            description='Whether the page image has been obfuscated because the user is not authorised to access it',
        ),
    ]
    iiifFragment: Annotated[
        Optional[str],
        Field(None, description='The IIIF fragment of the page, image file name'),
    ]


class SearchFacetRangeBucket(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    count: Annotated[int, Field(description='Number of items in the bucket')]
    val: Annotated[int, Field(description="Value of the 'type' element")]
    lower: Annotated[Optional[int], Field(None, description='Lower bound of the range')]
    upper: Annotated[Optional[int], Field(None, description='Lower bound of the range')]


class TimeCoverage(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    from_: Annotated[Optional[date], Field(None, alias='from')]
    to: Optional[date] = None


class TextReuseCluster(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Annotated[
        str,
        Field(
            description='ID of the text reuse passage',
            examples=['abc123'],
            pattern='^[a-zA-Z0-9-_]+$',
            title='Passage ID',
        ),
    ]
    lexicalOverlap: Annotated[
        Optional[float],
        Field(
            None,
            description='Percentage of overlap between passages in the cluster',
            ge=0.0,
            le=100.0,
        ),
    ]
    clusterSize: Annotated[
        Optional[float],
        Field(None, description='Number of passages in cluster', ge=0.0),
    ]
    connectedClustersCount: Annotated[
        Optional[float], Field(None, description='Number of connected clusters', ge=0.0)
    ]
    timeCoverage: Annotated[
        Optional[TimeCoverage],
        Field(None, description='Time window covered by documents in the cluster'),
    ]


class Facet(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[Optional[str], Field(None, description='Facet type')]
    numBuckets: Annotated[Optional[int], Field(None, description='Number of buckets')]
    buckets: Optional[Sequence[Mapping[str, Any]]] = None


class TextReuseClusterDetails(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    facets: Sequence[Facet]
    resolution: Annotated[
        Optional[Literal['year', 'month', 'day']],
        Field(None, description="Resolution for the 'date' facet"),
    ]


class Article(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Annotated[str, Field(description='ID of the article', title='Article ID')]


class TextReuseCluster1(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Annotated[str, Field(description='ID of the cluster', title='Cluster ID')]
    clusterSize: Annotated[
        Optional[int],
        Field(None, description='The size of the cluster', title='Cluster size'),
    ]
    timeDifferenceDay: Annotated[
        Optional[int],
        Field(
            None,
            description='The time difference in days between the two articles',
            title='Time difference in days',
        ),
    ]
    lexicalOverlap: Annotated[
        Optional[float],
        Field(
            None,
            description='The lexical overlap between the two articles',
            title='Lexical overlap',
        ),
    ]


class OffsetStart(RootModel[Optional[int]]):
    root: Annotated[
        Optional[int],
        Field(None, description='Offset of the passage in the article text', ge=0),
    ] = None


class OffsetEnd(RootModel[Optional[int]]):
    root: Annotated[
        Optional[int],
        Field(None, description='Offset of the passage in the article text', ge=0),
    ] = None


class ConnectedCluster(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Annotated[str, Field(description='ID of the connected cluster')]


class Issue(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Annotated[str, Field(description='ID of the issue')]


class TextReusePassage(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Annotated[
        str,
        Field(
            description='ID of the text reuse passage',
            examples=['abc123'],
            pattern='^[a-zA-Z0-9-_@:]+$',
            title='Passage ID',
        ),
    ]
    article: Annotated[
        Article,
        Field(
            description='Details of the article the passage belongs to',
            title='Article details',
        ),
    ]
    textReuseCluster: Annotated[
        TextReuseCluster1,
        Field(
            description='Details of the cluster the passage belongs to',
            title='Cluster details',
        ),
    ]
    offsetStart: OffsetStart
    offsetEnd: OffsetEnd
    content: Annotated[str, Field(description='Textual content of the passage')]
    title: Annotated[
        str,
        Field(
            description='Title of the content item (article) where this passage was found'
        ),
    ]
    connectedClusters: Optional[Sequence[ConnectedCluster]] = None
    isFront: Annotated[Optional[bool], Field(None, description='TBD')]
    size: Annotated[Optional[int], Field(None, description='Size of the passage')]
    newspaper: Optional[Any] = None
    issue: Annotated[Optional[Issue], Field(None, description='Issue details')]
    date: Annotated[
        Optional[AwareDatetime],
        Field(
            None, description='Date of the item (article) where this passage was found'
        ),
    ]
    pageRegions: Annotated[
        Optional[Sequence[str]],
        Field(None, description='Bounding box of the passage in the page'),
    ]
    pageNumbers: Annotated[
        Sequence[int],
        Field(description='Numbers of the pages where the passage was found'),
    ]
    collections: Annotated[
        Sequence[str], Field(description='Collection IDs the passage belongs to')
    ]


class RelatedTopic(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    uid: Annotated[str, Field(description='The unique identifier of the related topic')]
    w: Annotated[float, Field(description='TODO')]
    avg: Annotated[Optional[float], Field(None, description='TODO')]


class TopicWord(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    w: Annotated[str, Field(description='Word')]
    p: Annotated[float, Field(description='TODO')]
    h: Annotated[Optional[Sequence[str]], Field(None, description='TODO')]


class UpdateCollectableItems(BaseModel):
    add: Annotated[
        Optional[Sequence[str]],
        Field(None, description='IDs of the items to add to the collection'),
    ]
    remove: Annotated[
        Optional[Sequence[str]],
        Field(None, description='IDs of the items to remove from the collection'),
    ]


class User(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: int
    username: str
    firstname: str
    lastname: str
    isStaff: bool
    isActive: bool
    isSuperuser: bool
    uid: str


class Solr(BaseModel):
    endpoints: Optional[Mapping[str, str]] = None


class Mysql(BaseModel):
    endpoint: Optional[str] = None


class ApiVersion(BaseModel):
    branch: Optional[str] = None
    revision: Optional[str] = None
    version: Optional[str] = None


class DocumentsDateSpan(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    start: Optional[AwareDatetime] = None
    end: Optional[AwareDatetime] = None


class Newspapers(BaseModel):
    name: Optional[str] = None


class VersionDetails(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    solr: Solr
    mysql: Mysql
    version: str
    apiVersion: ApiVersion
    documentsDateSpan: DocumentsDateSpan
    newspapers: Mapping[str, Newspapers]
    features: Mapping[str, Mapping[str, Any]]


class Image(BaseModel):
    value: str
    rank: str
    datatype: str


class WikidataEntityDetails(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    id: str
    type: str
    labels: Annotated[
        Mapping[str, str],
        Field(description='Labels of the entity. Key is the language code.'),
    ]
    descriptions: Annotated[
        Mapping[str, str],
        Field(description='Labels of the entity. Key is the language code.'),
    ]
    images: Sequence[Image]


class YearWeights(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    c: Annotated[Optional[float], Field(None, description='Number of content items')]
    a: Annotated[Optional[float], Field(None, description='Number of articles')]
    p: Annotated[Optional[float], Field(None, description='Number of pages')]
    i: Annotated[Optional[float], Field(None, description='Number of issues')]
    m: Annotated[
        Optional[float],
        Field(None, description='Number of images (with or without vectors)'),
    ]


class AuthenticationCreateResponse(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    accessToken: str
    authentication: Authentication
    user: User


class CollectableItemGroup(BaseModel):
    itemId: Annotated[
        Optional[str], Field(None, description='The id of the collectable item group')
    ]
    contentType: Annotated[
        Optional[Literal['A', 'E', 'P', 'I']],
        Field(
            None,
            description='Content type of the collectable item group: (A)rticle, (E)ntities, (P)ages, (I)ssues',
        ),
    ]
    collectionIds: Annotated[
        Optional[Sequence[str]], Field(None, description='Ids of the collections')
    ]
    searchQueries: Annotated[
        Optional[Sequence[str]], Field(None, description='Search queries')
    ]
    collections: Annotated[
        Optional[Sequence[Collection]], Field(None, description='Collection objects')
    ]
    latestDateAdded: Annotated[
        Optional[AwareDatetime],
        Field(None, description='The latest date added to the collectable item group'),
    ]


class EntityDetails(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    uid: Annotated[str, Field(description='Unique identifier of the entity')]
    name: Annotated[str, Field(description='Entity name')]
    type: Literal['person', 'location']
    countItems: Annotated[int, Field(description='TODO')]
    countMentions: Annotated[
        int, Field(description='Number of mentions of this entity in articles')
    ]
    wikidataId: Annotated[
        Optional[str], Field(None, description='ID of the entity in wikidata')
    ]
    wikidata: Optional[WikidataEntityDetails] = None


class Newspaper(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    uid: Annotated[str, Field(description='The unique identifier of the newspaper')]
    acronym: Annotated[str, Field(description='The acronym of the newspaper')]
    labels: Annotated[Sequence[str], Field(description='The labels of the newspaper')]
    languages: Annotated[
        Sequence[str],
        Field(description='Language codes of the languages used in the newspaper'),
    ]
    properties: Annotated[
        Optional[Sequence[NewspaperProperty]], Field(None, description='TODO')
    ]
    included: Annotated[bool, Field(description='TODO')]
    name: Annotated[str, Field(description='Title of the newspaper')]
    endYear: int
    startYear: int
    firstIssue: Optional[NewspaperIssue] = None
    lastIssue: Optional[NewspaperIssue] = None
    countArticles: Annotated[
        int, Field(description='The number of articles in the newspaper')
    ]
    countIssues: Annotated[
        int, Field(description='The number of issues in the newspaper')
    ]
    countPages: Annotated[
        int, Field(description='The number of pages in the newspaper')
    ]
    fetched: Annotated[Optional[bool], Field(None, description='TODO')]
    deltaYear: Annotated[
        int, Field(description='The number of years of the newspaper available')
    ]


class TextReuseClusterCompound(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    cluster: Optional[TextReuseCluster] = None
    textSample: str
    details: Optional[TextReuseClusterDetails] = None


class Topic(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    uid: Annotated[str, Field(description='The unique identifier of the topic')]
    language: Annotated[str, Field(description='The language code of the topic')]
    community: Annotated[Optional[str], Field(None, description='TODO')]
    pagerank: Annotated[Optional[float], Field(None, description='TODO')]
    degree: Annotated[Optional[float], Field(None, description='TODO')]
    x: Annotated[Optional[float], Field(None, description='TODO')]
    y: Annotated[Optional[float], Field(None, description='TODO')]
    relatedTopics: Optional[Sequence[RelatedTopic]] = None
    countItems: Annotated[Optional[float], Field(None, description='TODO')]
    excerpt: Annotated[Optional[Sequence[TopicWord]], Field(None, description='TODO')]
    words: Annotated[Optional[Sequence[TopicWord]], Field(None, description='TODO')]
    model: Annotated[
        Optional[str],
        Field(None, description='ID of the model used to generate the topic'),
    ]


class Year(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    uid: Annotated[
        Optional[int], Field(None, description='Numeric representation of the year')
    ]
    values: Optional[YearWeights] = None
    refs: Optional[YearWeights] = None


class ContentItemTopic(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    topic: Optional[Topic] = None
    relevance: Annotated[float, Field(description='TODO')]
    topicUid: Annotated[Optional[str], Field(None, description='TODO')]


class FindTextReuseClustersResponse(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    clusters: Sequence[TextReuseClusterCompound]
    info: Any


class SearchFacetBucket(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    count: Annotated[int, Field(description='Number of items in the bucket')]
    val: Annotated[str, Field(description="Value of the 'type' element")]
    uid: Annotated[
        Optional[str],
        Field(None, description="UID of the 'type' element. Same as 'val'"),
    ]
    item: Annotated[
        Optional[Union[Newspaper, Collection, Entity, Topic, Year]],
        Field(
            None,
            description='The item in the bucket. Particular objct schema depends on the facet type',
        ),
    ]


class ContentItem(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    uid: Annotated[str, Field(description='The unique identifier of the content item')]
    type: Annotated[
        str, Field(description='The type of the content item. NOTE: may be empty.')
    ]
    title: Annotated[str, Field(description='The title of the content item')]
    size: Annotated[
        int, Field(description='The size of the content item in characters')
    ]
    nbPages: Annotated[
        int, Field(description='The number of pages in this content item')
    ]
    pages: Sequence[Page]
    isCC: Annotated[bool, Field(description='TODO')]
    excerpt: Annotated[str, Field(description='The excerpt of the content item')]
    locations: Optional[Sequence[Entity]] = None
    persons: Optional[Sequence[Entity]] = None
    language: Annotated[
        Optional[str], Field(None, description='The language code of the content item')
    ]
    issue: Optional[NewspaperIssue] = None
    matches: Optional[Sequence[ContentItemMatch]] = None
    regions: Optional[Sequence[ContentItemRegion]] = None
    regionBreaks: Optional[Sequence[int]] = None
    contentLineBreaks: Optional[Sequence[int]] = None
    labels: Annotated[Sequence[Literal['article']], Field(description='TODO')]
    accessRight: Literal['na', 'OpenPrivate', 'Closed', 'OpenPublic']
    isFront: Annotated[Optional[bool], Field(None, description='TODO')]
    date: Optional[AwareDatetime] = None
    year: Annotated[int, Field(description='The year of the content item')]
    country: Annotated[
        Optional[str], Field(None, description='The country code of the content item')
    ]
    tags: Optional[Sequence[str]] = None
    collections: Optional[Union[Sequence[str], Sequence[Collection]]] = None
    newspaper: Optional[Newspaper] = None
    dataProvider: Optional[str] = None
    topics: Optional[Sequence[ContentItemTopic]] = None
    content: Annotated[
        Optional[str], Field(None, description='The content of the content item')
    ]
    mentions: Optional[Sequence[Mention]] = None
    v: Annotated[Optional[str], Field(None, description='TODO')]


class SearchFacet(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[str, Field(description='The type of facet')]
    numBuckets: Annotated[int, Field(description='The number of buckets in the facet')]
    buckets: Union[Sequence[SearchFacetBucket], Sequence[SearchFacetRangeBucket]]
    min: Annotated[Optional[Any], Field(None, description='TODO')]
    max: Annotated[Optional[Any], Field(None, description='TODO')]
    gap: Annotated[Optional[Any], Field(None, description='TODO')]
