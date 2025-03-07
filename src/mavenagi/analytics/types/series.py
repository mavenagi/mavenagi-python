# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .labeled_point import LabeledPoint
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class Series(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    The name of the series, derived from the grouping field.
    If the metric is a percentile, the name represents the percentile value.
    """

    data: typing.List[LabeledPoint] = pydantic.Field()
    """
    List of labeled data points for the series.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
