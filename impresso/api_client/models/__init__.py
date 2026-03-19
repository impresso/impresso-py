"""Contains all the data models used in inputs/outputs"""

from .add_collectable_items_from_filters import AddCollectableItemsFromFilters
from .add_collectable_items_from_filters_namespace import AddCollectableItemsFromFiltersNamespace
from .admin_get_response import AdminGETResponse
from .admin_get_response_cache_counts import AdminGETResponseCacheCounts
from .admin_get_response_content_items_permissions_details import AdminGETResponseContentItemsPermissionsDetails
from .admin_get_response_images_permissions_details import AdminGETResponseImagesPermissionsDetails
from .admin_get_response_patch_result import AdminGETResponsePatchResult
from .admin_get_response_patch_result_cleared import AdminGETResponsePatchResultCleared
from .admin_get_response_user_accounts_item import AdminGETResponseUserAccountsItem
from .admin_get_response_well_known_computed_at import AdminGETResponseWellKnownComputedAt
from .admin_patch_request import AdminPatchRequest
from .admin_patch_request_action import AdminPatchRequestAction
from .authentication_create_request import AuthenticationCreateRequest
from .authentication_create_request_strategy import AuthenticationCreateRequestStrategy
from .authentication_response import AuthenticationResponse
from .authentication_response_authentication import AuthenticationResponseAuthentication
from .authentication_response_authentication_payload import AuthenticationResponseAuthenticationPayload
from .authentication_response_user import AuthenticationResponseUser
from .base_find_response import BaseFindResponse
from .base_find_response_pagination import BaseFindResponsePagination
from .collectable_item_group import CollectableItemGroup
from .collectable_item_group_content_type import CollectableItemGroupContentType
from .collectable_items_updated_response import CollectableItemsUpdatedResponse
from .collection import Collection
from .collection_access_level import CollectionAccessLevel
from .collection_remove_response import CollectionRemoveResponse
from .collection_remove_response_params import CollectionRemoveResponseParams
from .collection_remove_response_params_status import CollectionRemoveResponseParamsStatus
from .collection_remove_response_task import CollectionRemoveResponseTask
from .content_item import ContentItem
from .content_item_access_bitmaps import ContentItemAccessBitmaps
from .content_item_access_rights import ContentItemAccessRights
from .content_item_access_rights_copyright import ContentItemAccessRightsCopyright
from .content_item_access_rights_data_domain import ContentItemAccessRightsDataDomain
from .content_item_audio import ContentItemAudio
from .content_item_audio_locator import ContentItemAudioLocator
from .content_item_audio_record import ContentItemAudioRecord
from .content_item_image import ContentItemImage
from .content_item_mention import ContentItemMention
from .content_item_meta import ContentItemMeta
from .content_item_meta_source_medium import ContentItemMetaSourceMedium
from .content_item_meta_source_type import ContentItemMetaSourceType
from .content_item_named_entity import ContentItemNamedEntity
from .content_item_page import ContentItemPage
from .content_item_semantic_enrichments import ContentItemSemanticEnrichments
from .content_item_semantic_enrichments_mentions import ContentItemSemanticEnrichmentsMentions
from .content_item_semantic_enrichments_named_entities import ContentItemSemanticEnrichmentsNamedEntities
from .content_item_text import ContentItemText
from .content_item_text_document_type import ContentItemTextDocumentType
from .content_item_text_item_type import ContentItemTextItemType
from .content_item_text_match import ContentItemTextMatch
from .content_item_topic import ContentItemTopic
from .data_provider import DataProvider
from .data_provider_names_item import DataProviderNamesItem
from .entity import Entity
from .entity_details import EntityDetails
from .entity_details_type import EntityDetailsType
from .error import Error
from .experiment_info import ExperimentInfo
from .facet_with_label import FacetWithLabel
from .filter_ import Filter
from .filter_context import FilterContext
from .filter_op import FilterOp
from .filter_precision import FilterPrecision
from .find_collections_base_find_response import FindCollectionsBaseFindResponse
from .find_collections_base_find_response_pagination import FindCollectionsBaseFindResponsePagination
from .find_collections_order_by import FindCollectionsOrderBy
from .find_data_providers_base_find_response import FindDataProvidersBaseFindResponse
from .find_data_providers_base_find_response_pagination import FindDataProvidersBaseFindResponsePagination
from .find_entities_base_find_response import FindEntitiesBaseFindResponse
from .find_entities_base_find_response_pagination import FindEntitiesBaseFindResponsePagination
from .find_entities_order_by import FindEntitiesOrderBy
from .find_experiments_base_find_response import FindExperimentsBaseFindResponse
from .find_experiments_base_find_response_pagination import FindExperimentsBaseFindResponsePagination
from .find_images_base_find_response import FindImagesBaseFindResponse
from .find_images_base_find_response_pagination import FindImagesBaseFindResponsePagination
from .find_images_order_by import FindImagesOrderBy
from .find_media_sources_base_find_response import FindMediaSourcesBaseFindResponse
from .find_media_sources_base_find_response_pagination import FindMediaSourcesBaseFindResponsePagination
from .find_media_sources_order_by import FindMediaSourcesOrderBy
from .find_media_sources_type import FindMediaSourcesType
from .find_text_reuse_clusters_base_find_response import FindTextReuseClustersBaseFindResponse
from .find_text_reuse_clusters_base_find_response_pagination import FindTextReuseClustersBaseFindResponsePagination
from .find_text_reuse_clusters_order_by import FindTextReuseClustersOrderBy
from .find_text_reuse_clusters_response import FindTextReuseClustersResponse
from .find_text_reuse_clusters_response_text_reuse_cluster_compound import (
    FindTextReuseClustersResponseTextReuseClusterCompound,
)
from .find_text_reuse_clusters_response_text_reuse_cluster_compound_text_reuse_cluster import (
    FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseCluster,
)
from .find_text_reuse_clusters_response_text_reuse_cluster_compound_text_reuse_cluster_details import (
    FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetails,
)
from .find_text_reuse_clusters_response_text_reuse_cluster_compound_text_reuse_cluster_details_facets_item import (
    FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsFacetsItem,
)
from .find_text_reuse_clusters_response_text_reuse_cluster_compound_text_reuse_cluster_details_facets_item_buckets_item import (
    FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsFacetsItemBucketsItem,
)
from .find_text_reuse_clusters_response_text_reuse_cluster_compound_text_reuse_cluster_details_resolution import (
    FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsResolution,
)
from .find_text_reuse_clusters_response_text_reuse_cluster_compound_text_reuse_cluster_time_coverage import (
    FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterTimeCoverage,
)
from .find_text_reuse_passages_base_find_response import FindTextReusePassagesBaseFindResponse
from .find_text_reuse_passages_base_find_response_pagination import FindTextReusePassagesBaseFindResponsePagination
from .find_text_reuse_passages_order_by import FindTextReusePassagesOrderBy
from .find_topics_base_find_response import FindTopicsBaseFindResponse
from .find_topics_base_find_response_pagination import FindTopicsBaseFindResponsePagination
from .find_topics_order_by import FindTopicsOrderBy
from .freeform import Freeform
from .full_version_details import FullVersionDetails
from .full_version_details_api_version import FullVersionDetailsApiVersion
from .full_version_details_documents_date_span import FullVersionDetailsDocumentsDateSpan
from .full_version_details_features import FullVersionDetailsFeatures
from .full_version_details_features_additional_property import FullVersionDetailsFeaturesAdditionalProperty
from .full_version_details_mysql import FullVersionDetailsMysql
from .full_version_details_newspapers import FullVersionDetailsNewspapers
from .full_version_details_newspapers_additional_property import FullVersionDetailsNewspapersAdditionalProperty
from .full_version_details_partner_institutions_item import FullVersionDetailsPartnerInstitutionsItem
from .full_version_details_partner_institutions_item_names_item import (
    FullVersionDetailsPartnerInstitutionsItemNamesItem,
)
from .full_version_details_solr import FullVersionDetailsSolr
from .full_version_details_solr_endpoints import FullVersionDetailsSolrEndpoints
from .get_images_facet_base_find_response import GetImagesFacetBaseFindResponse
from .get_images_facet_base_find_response_pagination import GetImagesFacetBaseFindResponsePagination
from .get_images_facet_id import GetImagesFacetId
from .get_images_facet_order_by import GetImagesFacetOrderBy
from .get_search_facet_base_find_response import GetSearchFacetBaseFindResponse
from .get_search_facet_base_find_response_pagination import GetSearchFacetBaseFindResponsePagination
from .get_search_facet_id import GetSearchFacetId
from .get_search_facet_order_by import GetSearchFacetOrderBy
from .get_tr_clusters_facet_base_find_response import GetTrClustersFacetBaseFindResponse
from .get_tr_clusters_facet_base_find_response_pagination import GetTrClustersFacetBaseFindResponsePagination
from .get_tr_clusters_facet_id import GetTrClustersFacetId
from .get_tr_clusters_facet_order_by import GetTrClustersFacetOrderBy
from .get_tr_passages_facet_base_find_response import GetTrPassagesFacetBaseFindResponse
from .get_tr_passages_facet_base_find_response_pagination import GetTrPassagesFacetBaseFindResponsePagination
from .get_tr_passages_facet_id import GetTrPassagesFacetId
from .get_tr_passages_facet_order_by import GetTrPassagesFacetOrderBy
from .iiif_content_item_page_details import IIIFContentItemPageDetails
from .image import Image
from .image_image_types import ImageImageTypes
from .image_media_source_ref import ImageMediaSourceRef
from .image_media_source_ref_type import ImageMediaSourceRefType
from .impresso_embedding_response import ImpressoEmbeddingResponse
from .impresso_image_embedding_request import ImpressoImageEmbeddingRequest
from .impresso_image_embedding_request_search_target import ImpressoImageEmbeddingRequestSearchTarget
from .impresso_named_entity_recognition_entity import ImpressoNamedEntityRecognitionEntity
from .impresso_named_entity_recognition_entity_confidence import ImpressoNamedEntityRecognitionEntityConfidence
from .impresso_named_entity_recognition_entity_offset import ImpressoNamedEntityRecognitionEntityOffset
from .impresso_named_entity_recognition_entity_type import ImpressoNamedEntityRecognitionEntityType
from .impresso_named_entity_recognition_entity_wikidata import ImpressoNamedEntityRecognitionEntityWikidata
from .impresso_named_entity_recognition_request import ImpressoNamedEntityRecognitionRequest
from .impresso_named_entity_recognition_request_method import ImpressoNamedEntityRecognitionRequestMethod
from .impresso_named_entity_recognition_response import ImpressoNamedEntityRecognitionResponse
from .impresso_text_embedding_request import ImpressoTextEmbeddingRequest
from .impresso_text_embedding_request_search_target import ImpressoTextEmbeddingRequestSearchTarget
from .interact_with_experiment_body import InteractWithExperimentBody
from .media_source import MediaSource
from .media_source_properties_item import MediaSourcePropertiesItem
from .media_source_totals import MediaSourceTotals
from .media_source_type import MediaSourceType
from .new_collection_request import NewCollectionRequest
from .new_collection_request_access_level import NewCollectionRequestAccessLevel
from .partner import Partner
from .search_base_find_response import SearchBaseFindResponse
from .search_base_find_response_pagination import SearchBaseFindResponsePagination
from .search_facet_bucket import SearchFacetBucket
from .search_order_by import SearchOrderBy
from .text_reuse_cluster import TextReuseCluster
from .text_reuse_cluster_time_coverage import TextReuseClusterTimeCoverage
from .text_reuse_passage import TextReusePassage
from .text_reuse_passage_offset import TextReusePassageOffset
from .topic import Topic
from .topic_word import TopicWord
from .update_collectable_items_request import UpdateCollectableItemsRequest
from .version_details import VersionDetails
from .wikidata_location import WikidataLocation
from .wikidata_location_coordinates import WikidataLocationCoordinates
from .wikidata_location_descriptions import WikidataLocationDescriptions
from .wikidata_location_labels import WikidataLocationLabels
from .wikidata_location_type import WikidataLocationType
from .wikidata_person import WikidataPerson
from .wikidata_person_descriptions import WikidataPersonDescriptions
from .wikidata_person_labels import WikidataPersonLabels
from .wikidata_person_type import WikidataPersonType
from .word_match import WordMatch
from .year import Year
from .year_weights import YearWeights

__all__ = (
    "AddCollectableItemsFromFilters",
    "AddCollectableItemsFromFiltersNamespace",
    "AdminGETResponse",
    "AdminGETResponseCacheCounts",
    "AdminGETResponseContentItemsPermissionsDetails",
    "AdminGETResponseImagesPermissionsDetails",
    "AdminGETResponsePatchResult",
    "AdminGETResponsePatchResultCleared",
    "AdminGETResponseUserAccountsItem",
    "AdminGETResponseWellKnownComputedAt",
    "AdminPatchRequest",
    "AdminPatchRequestAction",
    "AuthenticationCreateRequest",
    "AuthenticationCreateRequestStrategy",
    "AuthenticationResponse",
    "AuthenticationResponseAuthentication",
    "AuthenticationResponseAuthenticationPayload",
    "AuthenticationResponseUser",
    "BaseFindResponse",
    "BaseFindResponsePagination",
    "CollectableItemGroup",
    "CollectableItemGroupContentType",
    "CollectableItemsUpdatedResponse",
    "Collection",
    "CollectionAccessLevel",
    "CollectionRemoveResponse",
    "CollectionRemoveResponseParams",
    "CollectionRemoveResponseParamsStatus",
    "CollectionRemoveResponseTask",
    "ContentItem",
    "ContentItemAccessBitmaps",
    "ContentItemAccessRights",
    "ContentItemAccessRightsCopyright",
    "ContentItemAccessRightsDataDomain",
    "ContentItemAudio",
    "ContentItemAudioLocator",
    "ContentItemAudioRecord",
    "ContentItemImage",
    "ContentItemMention",
    "ContentItemMeta",
    "ContentItemMetaSourceMedium",
    "ContentItemMetaSourceType",
    "ContentItemNamedEntity",
    "ContentItemPage",
    "ContentItemSemanticEnrichments",
    "ContentItemSemanticEnrichmentsMentions",
    "ContentItemSemanticEnrichmentsNamedEntities",
    "ContentItemText",
    "ContentItemTextDocumentType",
    "ContentItemTextItemType",
    "ContentItemTextMatch",
    "ContentItemTopic",
    "DataProvider",
    "DataProviderNamesItem",
    "Entity",
    "EntityDetails",
    "EntityDetailsType",
    "Error",
    "ExperimentInfo",
    "FacetWithLabel",
    "Filter",
    "FilterContext",
    "FilterOp",
    "FilterPrecision",
    "FindCollectionsBaseFindResponse",
    "FindCollectionsBaseFindResponsePagination",
    "FindCollectionsOrderBy",
    "FindDataProvidersBaseFindResponse",
    "FindDataProvidersBaseFindResponsePagination",
    "FindEntitiesBaseFindResponse",
    "FindEntitiesBaseFindResponsePagination",
    "FindEntitiesOrderBy",
    "FindExperimentsBaseFindResponse",
    "FindExperimentsBaseFindResponsePagination",
    "FindImagesBaseFindResponse",
    "FindImagesBaseFindResponsePagination",
    "FindImagesOrderBy",
    "FindMediaSourcesBaseFindResponse",
    "FindMediaSourcesBaseFindResponsePagination",
    "FindMediaSourcesOrderBy",
    "FindMediaSourcesType",
    "FindTextReuseClustersBaseFindResponse",
    "FindTextReuseClustersBaseFindResponsePagination",
    "FindTextReuseClustersOrderBy",
    "FindTextReuseClustersResponse",
    "FindTextReuseClustersResponseTextReuseClusterCompound",
    "FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseCluster",
    "FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetails",
    "FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsFacetsItem",
    "FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsFacetsItemBucketsItem",
    "FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterDetailsResolution",
    "FindTextReuseClustersResponseTextReuseClusterCompoundTextReuseClusterTimeCoverage",
    "FindTextReusePassagesBaseFindResponse",
    "FindTextReusePassagesBaseFindResponsePagination",
    "FindTextReusePassagesOrderBy",
    "FindTopicsBaseFindResponse",
    "FindTopicsBaseFindResponsePagination",
    "FindTopicsOrderBy",
    "Freeform",
    "FullVersionDetails",
    "FullVersionDetailsApiVersion",
    "FullVersionDetailsDocumentsDateSpan",
    "FullVersionDetailsFeatures",
    "FullVersionDetailsFeaturesAdditionalProperty",
    "FullVersionDetailsMysql",
    "FullVersionDetailsNewspapers",
    "FullVersionDetailsNewspapersAdditionalProperty",
    "FullVersionDetailsPartnerInstitutionsItem",
    "FullVersionDetailsPartnerInstitutionsItemNamesItem",
    "FullVersionDetailsSolr",
    "FullVersionDetailsSolrEndpoints",
    "GetImagesFacetBaseFindResponse",
    "GetImagesFacetBaseFindResponsePagination",
    "GetImagesFacetId",
    "GetImagesFacetOrderBy",
    "GetSearchFacetBaseFindResponse",
    "GetSearchFacetBaseFindResponsePagination",
    "GetSearchFacetId",
    "GetSearchFacetOrderBy",
    "GetTrClustersFacetBaseFindResponse",
    "GetTrClustersFacetBaseFindResponsePagination",
    "GetTrClustersFacetId",
    "GetTrClustersFacetOrderBy",
    "GetTrPassagesFacetBaseFindResponse",
    "GetTrPassagesFacetBaseFindResponsePagination",
    "GetTrPassagesFacetId",
    "GetTrPassagesFacetOrderBy",
    "IIIFContentItemPageDetails",
    "Image",
    "ImageImageTypes",
    "ImageMediaSourceRef",
    "ImageMediaSourceRefType",
    "ImpressoEmbeddingResponse",
    "ImpressoImageEmbeddingRequest",
    "ImpressoImageEmbeddingRequestSearchTarget",
    "ImpressoNamedEntityRecognitionEntity",
    "ImpressoNamedEntityRecognitionEntityConfidence",
    "ImpressoNamedEntityRecognitionEntityOffset",
    "ImpressoNamedEntityRecognitionEntityType",
    "ImpressoNamedEntityRecognitionEntityWikidata",
    "ImpressoNamedEntityRecognitionRequest",
    "ImpressoNamedEntityRecognitionRequestMethod",
    "ImpressoNamedEntityRecognitionResponse",
    "ImpressoTextEmbeddingRequest",
    "ImpressoTextEmbeddingRequestSearchTarget",
    "InteractWithExperimentBody",
    "MediaSource",
    "MediaSourcePropertiesItem",
    "MediaSourceTotals",
    "MediaSourceType",
    "NewCollectionRequest",
    "NewCollectionRequestAccessLevel",
    "Partner",
    "SearchBaseFindResponse",
    "SearchBaseFindResponsePagination",
    "SearchFacetBucket",
    "SearchOrderBy",
    "TextReuseCluster",
    "TextReuseClusterTimeCoverage",
    "TextReusePassage",
    "TextReusePassageOffset",
    "Topic",
    "TopicWord",
    "UpdateCollectableItemsRequest",
    "VersionDetails",
    "WikidataLocation",
    "WikidataLocationCoordinates",
    "WikidataLocationDescriptions",
    "WikidataLocationLabels",
    "WikidataLocationType",
    "WikidataPerson",
    "WikidataPersonDescriptions",
    "WikidataPersonLabels",
    "WikidataPersonType",
    "WordMatch",
    "Year",
    "YearWeights",
)
