# This file was auto-generated by Fern from our API Definition.

from .group_by_base import GroupByBase
from ...conversation.types.feedback_field import FeedbackField
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class FeedbackGroupBy(GroupByBase):
    field: FeedbackField = pydantic.Field()
    """
    Field used for data grouping.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
