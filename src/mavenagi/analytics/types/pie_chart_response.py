# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .series import Series
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class PieChartResponse(UniversalBaseModel):
    series: Series = pydantic.Field()
    """
    The dataset for the pie chart.
    Each slice in the pie chart is represented as a data point with a name and a corresponding y-value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
