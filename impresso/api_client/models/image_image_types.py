from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageImageTypes")


@_attrs_define
class ImageImageTypes:
    """
    Attributes:
        visual_content (Union[Unset, str]): Whether the content is an image or not.
        technique (Union[Unset, str]): Determines if the image is a photograph.
        communication_goal (Union[Unset, str]): Purpose or communicative function of the image.
        visual_content_type (Union[Unset, str]): Classification of the visual content.
    """

    visual_content: Union[Unset, str] = UNSET
    technique: Union[Unset, str] = UNSET
    communication_goal: Union[Unset, str] = UNSET
    visual_content_type: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        visual_content = self.visual_content

        technique = self.technique

        communication_goal = self.communication_goal

        visual_content_type = self.visual_content_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if visual_content is not UNSET:
            field_dict["visualContent"] = visual_content
        if technique is not UNSET:
            field_dict["technique"] = technique
        if communication_goal is not UNSET:
            field_dict["communicationGoal"] = communication_goal
        if visual_content_type is not UNSET:
            field_dict["visualContentType"] = visual_content_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        visual_content = d.pop("visualContent", UNSET)

        technique = d.pop("technique", UNSET)

        communication_goal = d.pop("communicationGoal", UNSET)

        visual_content_type = d.pop("visualContentType", UNSET)

        image_image_types = cls(
            visual_content=visual_content,
            technique=technique,
            communication_goal=communication_goal,
            visual_content_type=visual_content_type,
        )

        return image_image_types
