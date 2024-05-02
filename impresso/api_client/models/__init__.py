"""Contains all the data models used in inputs/outputs"""

from .api_version import APIVersion
from .api_version_api_version import APIVersionApiVersion
from .api_version_documents_date_span import APIVersionDocumentsDateSpan
from .api_version_features import APIVersionFeatures
from .api_version_features_additional_property import APIVersionFeaturesAdditionalProperty
from .api_version_mysql import APIVersionMysql
from .api_version_newspapers import APIVersionNewspapers
from .api_version_newspapers_additional_property import APIVersionNewspapersAdditionalProperty
from .api_version_solr import APIVersionSolr
from .api_version_solr_endpoints import APIVersionSolrEndpoints
from .article import Article
from .authentication_create_request import AuthenticationCreateRequest
from .authentication_create_request_strategy import AuthenticationCreateRequestStrategy
from .authentication_response import AuthenticationResponse
from .authentication_response_authentication import AuthenticationResponseAuthentication
from .authentication_response_authentication_payload import AuthenticationResponseAuthenticationPayload
from .base_find import BaseFind
from .base_find_info import BaseFindInfo
from .base_user import BaseUser
from .collectable_item_group import CollectableItemGroup
from .collectable_item_group_content_type import CollectableItemGroupContentType
from .collection import Collection
from .entity import Entity
from .error import Error
from .error_data import ErrorData
from .filter_ import Filter
from .filter_context import FilterContext
from .filter_op import FilterOp
from .filter_precision import FilterPrecision
from .get_articles_filters import GetArticlesFilters
from .get_articles_filters_type import GetArticlesFiltersType
from .get_articles_order_by import GetArticlesOrderBy
from .get_articles_resolve import GetArticlesResolve
from .get_articles_response_200 import GetArticlesResponse200
from .get_articles_response_200_info import GetArticlesResponse200Info
from .get_collections_order_by import GetCollectionsOrderBy
from .get_collections_response_200 import GetCollectionsResponse200
from .get_collections_response_200_info import GetCollectionsResponse200Info
from .get_newspapers_order_by import GetNewspapersOrderBy
from .get_newspapers_response_200 import GetNewspapersResponse200
from .get_newspapers_response_200_info import GetNewspapersResponse200Info
from .get_search_facets import GetSearchFacets
from .get_search_group_by import GetSearchGroupBy
from .get_search_order_by import GetSearchOrderBy
from .get_search_response_200 import GetSearchResponse200
from .get_search_response_200_info import GetSearchResponse200Info
from .get_text_reuse_clusters_order_by import GetTextReuseClustersOrderBy
from .get_text_reuse_clusters_response_200 import GetTextReuseClustersResponse200
from .get_text_reuse_clusters_response_200_info import GetTextReuseClustersResponse200Info
from .get_text_reuse_passages_addons import GetTextReusePassagesAddons
from .get_text_reuse_passages_groupby import GetTextReusePassagesGroupby
from .get_text_reuse_passages_order_by import GetTextReusePassagesOrderBy
from .get_text_reuse_passages_response_200 import GetTextReusePassagesResponse200
from .get_text_reuse_passages_response_200_info import GetTextReusePassagesResponse200Info
from .new_collection import NewCollection
from .newspaper import Newspaper
from .newspaper_issue import NewspaperIssue
from .newspaper_property import NewspaperProperty
from .page import Page
from .page_regions_item import PageRegionsItem
from .remove_collection_response import RemoveCollectionResponse
from .remove_collection_response_params import RemoveCollectionResponseParams
from .remove_collection_response_params_status import RemoveCollectionResponseParamsStatus
from .remove_collection_response_task import RemoveCollectionResponseTask
from .text_reuse_cluster import TextReuseCluster
from .text_reuse_cluster_compound import TextReuseClusterCompound
from .text_reuse_cluster_details import TextReuseClusterDetails
from .text_reuse_cluster_details_facets_item import TextReuseClusterDetailsFacetsItem
from .text_reuse_cluster_details_facets_item_buckets_item import TextReuseClusterDetailsFacetsItemBucketsItem
from .text_reuse_cluster_details_resolution import TextReuseClusterDetailsResolution
from .text_reuse_cluster_time_coverage import TextReuseClusterTimeCoverage
from .text_reuse_passage import TextReusePassage
from .text_reuse_passage_article_details import TextReusePassageArticleDetails
from .text_reuse_passage_cluster_details import TextReusePassageClusterDetails
from .text_reuse_passage_connected_clusters import TextReusePassageConnectedClusters
from .text_reuse_passage_issue import TextReusePassageIssue
from .text_reuse_passage_newspaper import TextReusePassageNewspaper
from .user import User

__all__ = (
    "APIVersion",
    "APIVersionApiVersion",
    "APIVersionDocumentsDateSpan",
    "APIVersionFeatures",
    "APIVersionFeaturesAdditionalProperty",
    "APIVersionMysql",
    "APIVersionNewspapers",
    "APIVersionNewspapersAdditionalProperty",
    "APIVersionSolr",
    "APIVersionSolrEndpoints",
    "Article",
    "AuthenticationCreateRequest",
    "AuthenticationCreateRequestStrategy",
    "AuthenticationResponse",
    "AuthenticationResponseAuthentication",
    "AuthenticationResponseAuthenticationPayload",
    "BaseFind",
    "BaseFindInfo",
    "BaseUser",
    "CollectableItemGroup",
    "CollectableItemGroupContentType",
    "Collection",
    "Entity",
    "Error",
    "ErrorData",
    "Filter",
    "FilterContext",
    "FilterOp",
    "FilterPrecision",
    "GetArticlesFilters",
    "GetArticlesFiltersType",
    "GetArticlesOrderBy",
    "GetArticlesResolve",
    "GetArticlesResponse200",
    "GetArticlesResponse200Info",
    "GetCollectionsOrderBy",
    "GetCollectionsResponse200",
    "GetCollectionsResponse200Info",
    "GetNewspapersOrderBy",
    "GetNewspapersResponse200",
    "GetNewspapersResponse200Info",
    "GetSearchFacets",
    "GetSearchGroupBy",
    "GetSearchOrderBy",
    "GetSearchResponse200",
    "GetSearchResponse200Info",
    "GetTextReuseClustersOrderBy",
    "GetTextReuseClustersResponse200",
    "GetTextReuseClustersResponse200Info",
    "GetTextReusePassagesAddons",
    "GetTextReusePassagesGroupby",
    "GetTextReusePassagesOrderBy",
    "GetTextReusePassagesResponse200",
    "GetTextReusePassagesResponse200Info",
    "NewCollection",
    "Newspaper",
    "NewspaperIssue",
    "NewspaperProperty",
    "Page",
    "PageRegionsItem",
    "RemoveCollectionResponse",
    "RemoveCollectionResponseParams",
    "RemoveCollectionResponseParamsStatus",
    "RemoveCollectionResponseTask",
    "TextReuseCluster",
    "TextReuseClusterCompound",
    "TextReuseClusterDetails",
    "TextReuseClusterDetailsFacetsItem",
    "TextReuseClusterDetailsFacetsItemBucketsItem",
    "TextReuseClusterDetailsResolution",
    "TextReuseClusterTimeCoverage",
    "TextReusePassage",
    "TextReusePassageArticleDetails",
    "TextReusePassageClusterDetails",
    "TextReusePassageConnectedClusters",
    "TextReusePassageIssue",
    "TextReusePassageNewspaper",
    "User",
)
