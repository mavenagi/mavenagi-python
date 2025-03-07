# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .time_data_point import TimeDataPoint
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class TimeSeries(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the series, derived from the grouping field or percentile metric.
    """

    data: typing.List[TimeDataPoint] = pydantic.Field()
    """
    List of time-based data points for the series.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
