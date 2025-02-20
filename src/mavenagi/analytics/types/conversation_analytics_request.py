# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...conversation.types.conversation_filter import ConversationFilter
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ConversationAnalyticsRequest(UniversalBaseModel):
    conversation_filter: typing_extensions.Annotated[
        typing.Optional[ConversationFilter], FieldMetadata(alias="conversationFilter")
    ] = pydantic.Field(default=None)
    """
    Optional filter applied to refine the conversation data before processing.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
