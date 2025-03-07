# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import typing_extensions
import datetime as dt
from ...core.serialization import FieldMetadata
from ...commons.types.feedback_type import FeedbackType
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class FeedbackFilter(UniversalBaseModel):
    search: typing.Optional[str] = None
    created_after: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="createdAfter")] = None
    created_before: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="createdBefore")] = (
        None
    )
    types: typing.Optional[typing.List[FeedbackType]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
