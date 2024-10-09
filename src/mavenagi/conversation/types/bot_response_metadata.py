# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
from .source import Source
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class BotResponseMetadata(UniversalBaseModel):
    followup_questions: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="followupQuestions")]
    sources: typing.List[Source]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
