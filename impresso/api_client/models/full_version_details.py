from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.full_version_details_api_version import FullVersionDetailsApiVersion
    from ..models.full_version_details_documents_date_span import FullVersionDetailsDocumentsDateSpan
    from ..models.full_version_details_features import FullVersionDetailsFeatures
    from ..models.full_version_details_mysql import FullVersionDetailsMysql
    from ..models.full_version_details_newspapers import FullVersionDetailsNewspapers
    from ..models.full_version_details_partner_institutions_item import FullVersionDetailsPartnerInstitutionsItem
    from ..models.full_version_details_solr import FullVersionDetailsSolr


T = TypeVar("T", bound="FullVersionDetails")


@_attrs_define
class FullVersionDetails:
    """Version of the API. Contains information about the current version of the API, features, etc.

    Attributes:
        solr (FullVersionDetailsSolr):
        mysql (FullVersionDetailsMysql):
        version (str):
        api_version (FullVersionDetailsApiVersion):
        documents_date_span (FullVersionDetailsDocumentsDateSpan):
        newspapers (FullVersionDetailsNewspapers):
        features (FullVersionDetailsFeatures):
        partner_institutions (Union[Unset, List['FullVersionDetailsPartnerInstitutionsItem']]):
    """

    solr: "FullVersionDetailsSolr"
    mysql: "FullVersionDetailsMysql"
    version: str
    api_version: "FullVersionDetailsApiVersion"
    documents_date_span: "FullVersionDetailsDocumentsDateSpan"
    newspapers: "FullVersionDetailsNewspapers"
    features: "FullVersionDetailsFeatures"
    partner_institutions: Union[Unset, List["FullVersionDetailsPartnerInstitutionsItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        solr = self.solr.to_dict()

        mysql = self.mysql.to_dict()

        version = self.version

        api_version = self.api_version.to_dict()

        documents_date_span = self.documents_date_span.to_dict()

        newspapers = self.newspapers.to_dict()

        features = self.features.to_dict()

        partner_institutions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.partner_institutions, Unset):
            partner_institutions = []
            for partner_institutions_item_data in self.partner_institutions:
                partner_institutions_item = partner_institutions_item_data.to_dict()
                partner_institutions.append(partner_institutions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "solr": solr,
                "mysql": mysql,
                "version": version,
                "apiVersion": api_version,
                "documentsDateSpan": documents_date_span,
                "newspapers": newspapers,
                "features": features,
            }
        )
        if partner_institutions is not UNSET:
            field_dict["partnerInstitutions"] = partner_institutions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.full_version_details_api_version import FullVersionDetailsApiVersion
        from ..models.full_version_details_documents_date_span import FullVersionDetailsDocumentsDateSpan
        from ..models.full_version_details_features import FullVersionDetailsFeatures
        from ..models.full_version_details_mysql import FullVersionDetailsMysql
        from ..models.full_version_details_newspapers import FullVersionDetailsNewspapers
        from ..models.full_version_details_partner_institutions_item import FullVersionDetailsPartnerInstitutionsItem
        from ..models.full_version_details_solr import FullVersionDetailsSolr

        d = src_dict.copy()
        solr = FullVersionDetailsSolr.from_dict(d.pop("solr"))

        mysql = FullVersionDetailsMysql.from_dict(d.pop("mysql"))

        version = d.pop("version")

        api_version = FullVersionDetailsApiVersion.from_dict(d.pop("apiVersion"))

        documents_date_span = FullVersionDetailsDocumentsDateSpan.from_dict(d.pop("documentsDateSpan"))

        newspapers = FullVersionDetailsNewspapers.from_dict(d.pop("newspapers"))

        features = FullVersionDetailsFeatures.from_dict(d.pop("features"))

        partner_institutions = []
        _partner_institutions = d.pop("partnerInstitutions", UNSET)
        for partner_institutions_item_data in _partner_institutions or []:
            partner_institutions_item = FullVersionDetailsPartnerInstitutionsItem.from_dict(
                partner_institutions_item_data
            )

            partner_institutions.append(partner_institutions_item)

        full_version_details = cls(
            solr=solr,
            mysql=mysql,
            version=version,
            api_version=api_version,
            documents_date_span=documents_date_span,
            newspapers=newspapers,
            features=features,
            partner_institutions=partner_institutions,
        )

        return full_version_details
