# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
import typing_extensions
from ...conversation.types.conversation_field import ConversationField
from ...core.serialization import FieldMetadata


class Metric_Count(UniversalBaseModel):
    """
    Defines the metric to be calculated for a column or chart.
    Only numeric fields are supported, except for Count and DistinctCount, which can be applied to any field.
    """

    type: typing.Literal["count"] = "count"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Metric_Sum(UniversalBaseModel):
    """
    Defines the metric to be calculated for a column or chart.
    Only numeric fields are supported, except for Count and DistinctCount, which can be applied to any field.
    """

    type: typing.Literal["sum"] = "sum"
    target_field: typing_extensions.Annotated[ConversationField, FieldMetadata(alias="targetField")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Metric_Average(UniversalBaseModel):
    """
    Defines the metric to be calculated for a column or chart.
    Only numeric fields are supported, except for Count and DistinctCount, which can be applied to any field.
    """

    type: typing.Literal["average"] = "average"
    target_field: typing_extensions.Annotated[ConversationField, FieldMetadata(alias="targetField")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Metric_Min(UniversalBaseModel):
    """
    Defines the metric to be calculated for a column or chart.
    Only numeric fields are supported, except for Count and DistinctCount, which can be applied to any field.
    """

    type: typing.Literal["min"] = "min"
    target_field: typing_extensions.Annotated[ConversationField, FieldMetadata(alias="targetField")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Metric_Max(UniversalBaseModel):
    """
    Defines the metric to be calculated for a column or chart.
    Only numeric fields are supported, except for Count and DistinctCount, which can be applied to any field.
    """

    type: typing.Literal["max"] = "max"
    target_field: typing_extensions.Annotated[ConversationField, FieldMetadata(alias="targetField")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Metric_Percentile(UniversalBaseModel):
    """
    Defines the metric to be calculated for a column or chart.
    Only numeric fields are supported, except for Count and DistinctCount, which can be applied to any field.
    """

    type: typing.Literal["percentile"] = "percentile"
    percentiles: typing.List[float]
    target_field: typing_extensions.Annotated[ConversationField, FieldMetadata(alias="targetField")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Metric_Median(UniversalBaseModel):
    """
    Defines the metric to be calculated for a column or chart.
    Only numeric fields are supported, except for Count and DistinctCount, which can be applied to any field.
    """

    type: typing.Literal["median"] = "median"
    target_field: typing_extensions.Annotated[ConversationField, FieldMetadata(alias="targetField")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Metric_DistinctCount(UniversalBaseModel):
    """
    Defines the metric to be calculated for a column or chart.
    Only numeric fields are supported, except for Count and DistinctCount, which can be applied to any field.
    """

    type: typing.Literal["distinctCount"] = "distinctCount"
    target_field: typing_extensions.Annotated[ConversationField, FieldMetadata(alias="targetField")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Metric = typing.Union[
    Metric_Count,
    Metric_Sum,
    Metric_Average,
    Metric_Min,
    Metric_Max,
    Metric_Percentile,
    Metric_Median,
    Metric_DistinctCount,
]
