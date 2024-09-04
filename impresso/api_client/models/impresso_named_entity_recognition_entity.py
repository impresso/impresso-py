from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.impresso_named_entity_recognition_entity_type import ImpressoNamedEntityRecognitionEntityType

if TYPE_CHECKING:
    from ..models.impresso_named_entity_recognition_entity_confidence import (
        ImpressoNamedEntityRecognitionEntityConfidence,
    )
    from ..models.impresso_named_entity_recognition_entity_offset import ImpressoNamedEntityRecognitionEntityOffset


T = TypeVar("T", bound="ImpressoNamedEntityRecognitionEntity")


@_attrs_define
class ImpressoNamedEntityRecognitionEntity:
    """Impresso NER entity

    Attributes:
        id (str): ID of the entity
        type (ImpressoNamedEntityRecognitionEntityType): Type of the entity
        surface_form (str): Surface form of the entity
        offset (ImpressoNamedEntityRecognitionEntityOffset):
        is_type_nested (bool): Whether the entity type is nested
        confidence (ImpressoNamedEntityRecognitionEntityConfidence):
    """

    id: str
    type: ImpressoNamedEntityRecognitionEntityType
    surface_form: str
    offset: "ImpressoNamedEntityRecognitionEntityOffset"
    is_type_nested: bool
    confidence: "ImpressoNamedEntityRecognitionEntityConfidence"

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        surface_form = self.surface_form

        offset = self.offset.to_dict()

        is_type_nested = self.is_type_nested

        confidence = self.confidence.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "type": type,
                "surfaceForm": surface_form,
                "offset": offset,
                "isTypeNested": is_type_nested,
                "confidence": confidence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.impresso_named_entity_recognition_entity_confidence import (
            ImpressoNamedEntityRecognitionEntityConfidence,
        )
        from ..models.impresso_named_entity_recognition_entity_offset import ImpressoNamedEntityRecognitionEntityOffset

        d = src_dict.copy()
        id = d.pop("id")

        type = ImpressoNamedEntityRecognitionEntityType(d.pop("type"))

        surface_form = d.pop("surfaceForm")

        offset = ImpressoNamedEntityRecognitionEntityOffset.from_dict(d.pop("offset"))

        is_type_nested = d.pop("isTypeNested")

        confidence = ImpressoNamedEntityRecognitionEntityConfidence.from_dict(d.pop("confidence"))

        impresso_named_entity_recognition_entity = cls(
            id=id,
            type=type,
            surface_form=surface_form,
            offset=offset,
            is_type_nested=is_type_nested,
            confidence=confidence,
        )

        return impresso_named_entity_recognition_entity
