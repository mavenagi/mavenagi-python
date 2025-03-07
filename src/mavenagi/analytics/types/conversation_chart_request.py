# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...core.pydantic_utilities import UniversalBaseModel
import typing
import typing_extensions
from .conversation_group_by import ConversationGroupBy
from ...core.serialization import FieldMetadata
from .conversation_metric import ConversationMetric
from ...conversation.types.conversation_filter import ConversationFilter
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from .time_interval import TimeInterval


class ConversationChartRequest_PieChart(UniversalBaseModel):
    """
    Examples
    --------
    from mavenagi.analytics import (
        ConversationChartRequest_PieChart,
        ConversationGroupBy,
        ConversationMetric_Count,
    )
    from mavenagi.conversation import ConversationFilter

    ConversationChartRequest_PieChart(
        conversation_filter=ConversationFilter(
            languages=["en", "es"],
        ),
        group_by=ConversationGroupBy(
            field="Category",
        ),
        metric=ConversationMetric_Count(),
    )
    """

    type: typing.Literal["pieChart"] = "pieChart"
    group_by: typing_extensions.Annotated[ConversationGroupBy, FieldMetadata(alias="groupBy")]
    metric: ConversationMetric
    conversation_filter: typing_extensions.Annotated[
        typing.Optional[ConversationFilter], FieldMetadata(alias="conversationFilter")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConversationChartRequest_DateHistogram(UniversalBaseModel):
    """
    Examples
    --------
    from mavenagi.analytics import (
        ConversationChartRequest_PieChart,
        ConversationGroupBy,
        ConversationMetric_Count,
    )
    from mavenagi.conversation import ConversationFilter

    ConversationChartRequest_PieChart(
        conversation_filter=ConversationFilter(
            languages=["en", "es"],
        ),
        group_by=ConversationGroupBy(
            field="Category",
        ),
        metric=ConversationMetric_Count(),
    )
    """

    type: typing.Literal["dateHistogram"] = "dateHistogram"
    time_interval: typing_extensions.Annotated[TimeInterval, FieldMetadata(alias="timeInterval")]
    group_by: typing_extensions.Annotated[typing.Optional[ConversationGroupBy], FieldMetadata(alias="groupBy")] = None
    metric: ConversationMetric
    conversation_filter: typing_extensions.Annotated[
        typing.Optional[ConversationFilter], FieldMetadata(alias="conversationFilter")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConversationChartRequest_BarChart(UniversalBaseModel):
    """
    Examples
    --------
    from mavenagi.analytics import (
        ConversationChartRequest_PieChart,
        ConversationGroupBy,
        ConversationMetric_Count,
    )
    from mavenagi.conversation import ConversationFilter

    ConversationChartRequest_PieChart(
        conversation_filter=ConversationFilter(
            languages=["en", "es"],
        ),
        group_by=ConversationGroupBy(
            field="Category",
        ),
        metric=ConversationMetric_Count(),
    )
    """

    type: typing.Literal["barChart"] = "barChart"
    bar_definition: typing_extensions.Annotated[ConversationGroupBy, FieldMetadata(alias="barDefinition")]
    metric: ConversationMetric
    vertical_grouping: typing_extensions.Annotated[
        typing.Optional[ConversationGroupBy], FieldMetadata(alias="verticalGrouping")
    ] = None
    conversation_filter: typing_extensions.Annotated[
        typing.Optional[ConversationFilter], FieldMetadata(alias="conversationFilter")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


"""
from mavenagi.analytics import (
    ConversationChartRequest_PieChart,
    ConversationGroupBy,
    ConversationMetric_Count,
)
from mavenagi.conversation import ConversationFilter

ConversationChartRequest_PieChart(
    conversation_filter=ConversationFilter(
        languages=["en", "es"],
    ),
    group_by=ConversationGroupBy(
        field="Category",
    ),
    metric=ConversationMetric_Count(),
)
"""
ConversationChartRequest = typing.Union[
    ConversationChartRequest_PieChart, ConversationChartRequest_DateHistogram, ConversationChartRequest_BarChart
]
