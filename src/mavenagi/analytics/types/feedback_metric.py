# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
import typing_extensions
from ...conversation.types.feedback_field import FeedbackField
from ...core.serialization import FieldMetadata


class FeedbackMetric_Count(UniversalBaseModel):
    """
    Defines the metric to be calculated for a column or chart.
    """

    type: typing.Literal["count"] = "count"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FeedbackMetric_DistinctCount(UniversalBaseModel):
    """
    Defines the metric to be calculated for a column or chart.
    """

    type: typing.Literal["distinctCount"] = "distinctCount"
    target_field: typing_extensions.Annotated[FeedbackField, FieldMetadata(alias="targetField")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


FeedbackMetric = typing.Union[FeedbackMetric_Count, FeedbackMetric_DistinctCount]
