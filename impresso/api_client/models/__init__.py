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
from .article_access_right import ArticleAccessRight
from .article_labels_item import ArticleLabelsItem
from .article_match import ArticleMatch
from .article_mentions_item import ArticleMentionsItem
from .article_region import ArticleRegion
from .article_topic import ArticleTopic
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
from .filter_ import Filter
from .filter_context import FilterContext
from .filter_op import FilterOp
from .filter_precision import FilterPrecision
from .find_articles_order_by import FindArticlesOrderBy
from .find_articles_resolve import FindArticlesResolve
from .find_articles_response_200 import FindArticlesResponse200
from .find_articles_response_200_info import FindArticlesResponse200Info
from .find_collections_order_by import FindCollectionsOrderBy
from .find_collections_response_200 import FindCollectionsResponse200
from .find_collections_response_200_info import FindCollectionsResponse200Info
from .find_newspapers_order_by import FindNewspapersOrderBy
from .find_newspapers_response_200 import FindNewspapersResponse200
from .find_newspapers_response_200_info import FindNewspapersResponse200Info
from .find_search_facets_facets_item import FindSearchFacetsFacetsItem
from .find_search_facets_group_by import FindSearchFacetsGroupBy
from .find_search_facets_order_by import FindSearchFacetsOrderBy
from .find_search_facets_range_include import FindSearchFacetsRangeInclude
from .find_search_facets_response_200 import FindSearchFacetsResponse200
from .find_search_facets_response_200_info import FindSearchFacetsResponse200Info
from .find_text_reuse_clusters_order_by import FindTextReuseClustersOrderBy
from .find_text_reuse_clusters_response import FindTextReuseClustersResponse
from .find_text_reuse_passages_addons import FindTextReusePassagesAddons
from .find_text_reuse_passages_group_by import FindTextReusePassagesGroupBy
from .find_text_reuse_passages_order_by import FindTextReusePassagesOrderBy
from .find_text_reuse_passages_response_200 import FindTextReusePassagesResponse200
from .find_text_reuse_passages_response_200_info import FindTextReusePassagesResponse200Info
from .find_tr_clusters_facets_facets_item import FindTrClustersFacetsFacetsItem
from .find_tr_clusters_facets_group_by import FindTrClustersFacetsGroupBy
from .find_tr_clusters_facets_order_by import FindTrClustersFacetsOrderBy
from .find_tr_clusters_facets_range_include import FindTrClustersFacetsRangeInclude
from .find_tr_clusters_facets_response_200 import FindTrClustersFacetsResponse200
from .find_tr_clusters_facets_response_200_info import FindTrClustersFacetsResponse200Info
from .find_tr_passages_facets_facets_item import FindTrPassagesFacetsFacetsItem
from .find_tr_passages_facets_group_by import FindTrPassagesFacetsGroupBy
from .find_tr_passages_facets_order_by import FindTrPassagesFacetsOrderBy
from .find_tr_passages_facets_range_include import FindTrPassagesFacetsRangeInclude
from .find_tr_passages_facets_response_200 import FindTrPassagesFacetsResponse200
from .find_tr_passages_facets_response_200_info import FindTrPassagesFacetsResponse200Info
from .get_search_facet_group_by import GetSearchFacetGroupBy
from .get_search_facet_id import GetSearchFacetId
from .get_search_facet_order_by import GetSearchFacetOrderBy
from .get_search_facet_range_include import GetSearchFacetRangeInclude
from .get_tr_clusters_facet_group_by import GetTrClustersFacetGroupBy
from .get_tr_clusters_facet_id import GetTrClustersFacetId
from .get_tr_clusters_facet_order_by import GetTrClustersFacetOrderBy
from .get_tr_clusters_facet_range_include import GetTrClustersFacetRangeInclude
from .get_tr_passages_facet_group_by import GetTrPassagesFacetGroupBy
from .get_tr_passages_facet_id import GetTrPassagesFacetId
from .get_tr_passages_facet_order_by import GetTrPassagesFacetOrderBy
from .get_tr_passages_facet_range_include import GetTrPassagesFacetRangeInclude
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
from .search_facet import SearchFacet
from .search_facet_bucket import SearchFacetBucket
from .search_facet_range_bucket import SearchFacetRangeBucket
from .search_facets import SearchFacets
from .search_group_by import SearchGroupBy
from .search_order_by import SearchOrderBy
from .search_response_200 import SearchResponse200
from .search_response_200_info import SearchResponse200Info
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
from .text_reuse_passage_connected_clusters_item import TextReusePassageConnectedClustersItem
from .text_reuse_passage_issue import TextReusePassageIssue
from .topic import Topic
from .topic_related_topics_item import TopicRelatedTopicsItem
from .topic_word import TopicWord
from .user import User
from .year import Year
from .year_weights import YearWeights

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
    "ArticleAccessRight",
    "ArticleLabelsItem",
    "ArticleMatch",
    "ArticleMentionsItem",
    "ArticleRegion",
    "ArticleTopic",
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
    "Filter",
    "FilterContext",
    "FilterOp",
    "FilterPrecision",
    "FindArticlesOrderBy",
    "FindArticlesResolve",
    "FindArticlesResponse200",
    "FindArticlesResponse200Info",
    "FindCollectionsOrderBy",
    "FindCollectionsResponse200",
    "FindCollectionsResponse200Info",
    "FindNewspapersOrderBy",
    "FindNewspapersResponse200",
    "FindNewspapersResponse200Info",
    "FindSearchFacetsFacetsItem",
    "FindSearchFacetsGroupBy",
    "FindSearchFacetsOrderBy",
    "FindSearchFacetsRangeInclude",
    "FindSearchFacetsResponse200",
    "FindSearchFacetsResponse200Info",
    "FindTextReuseClustersOrderBy",
    "FindTextReuseClustersResponse",
    "FindTextReusePassagesAddons",
    "FindTextReusePassagesGroupBy",
    "FindTextReusePassagesOrderBy",
    "FindTextReusePassagesResponse200",
    "FindTextReusePassagesResponse200Info",
    "FindTrClustersFacetsFacetsItem",
    "FindTrClustersFacetsGroupBy",
    "FindTrClustersFacetsOrderBy",
    "FindTrClustersFacetsRangeInclude",
    "FindTrClustersFacetsResponse200",
    "FindTrClustersFacetsResponse200Info",
    "FindTrPassagesFacetsFacetsItem",
    "FindTrPassagesFacetsGroupBy",
    "FindTrPassagesFacetsOrderBy",
    "FindTrPassagesFacetsRangeInclude",
    "FindTrPassagesFacetsResponse200",
    "FindTrPassagesFacetsResponse200Info",
    "GetSearchFacetGroupBy",
    "GetSearchFacetId",
    "GetSearchFacetOrderBy",
    "GetSearchFacetRangeInclude",
    "GetTrClustersFacetGroupBy",
    "GetTrClustersFacetId",
    "GetTrClustersFacetOrderBy",
    "GetTrClustersFacetRangeInclude",
    "GetTrPassagesFacetGroupBy",
    "GetTrPassagesFacetId",
    "GetTrPassagesFacetOrderBy",
    "GetTrPassagesFacetRangeInclude",
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
    "SearchFacet",
    "SearchFacetBucket",
    "SearchFacetRangeBucket",
    "SearchFacets",
    "SearchGroupBy",
    "SearchOrderBy",
    "SearchResponse200",
    "SearchResponse200Info",
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
    "TextReusePassageConnectedClustersItem",
    "TextReusePassageIssue",
    "Topic",
    "TopicRelatedTopicsItem",
    "TopicWord",
    "User",
    "Year",
    "YearWeights",
)
