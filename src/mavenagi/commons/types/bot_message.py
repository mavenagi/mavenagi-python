# This file was auto-generated by Fern from our API Definition.

from .conversation_message_base import ConversationMessageBase
import typing_extensions
from .entity_id import EntityId
from ...core.serialization import FieldMetadata
import pydantic
from .bot_conversation_message_type import BotConversationMessageType
import typing
from .bot_response import BotResponse
from .bot_response_metadata import BotResponseMetadata
from .bot_message_status import BotMessageStatus
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class BotMessage(ConversationMessageBase):
    conversation_message_id: typing_extensions.Annotated[EntityId, FieldMetadata(alias="conversationMessageId")] = (
        pydantic.Field()
    )
    """
    The ID that uniquely identifies this message within the conversation
    """

    bot_message_type: typing_extensions.Annotated[BotConversationMessageType, FieldMetadata(alias="botMessageType")]
    responses: typing.List[BotResponse]
    metadata: BotResponseMetadata
    status: BotMessageStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
