# This file was auto-generated by Fern from our API Definition.

from .conversation_message_base import ConversationMessageBase
import typing_extensions
from ...commons.types.entity_id_base import EntityIdBase
from ...core.serialization import FieldMetadata
import pydantic
from .user_conversation_message_type import UserConversationMessageType
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class UserMessageBase(ConversationMessageBase):
    user_id: typing_extensions.Annotated[EntityIdBase, FieldMetadata(alias="userId")] = pydantic.Field()
    """
    ID that uniquely identifies the user that created this message
    """

    text: str = pydantic.Field()
    """
    The text of the message. Cannot be empty
    """

    user_message_type: typing_extensions.Annotated[UserConversationMessageType, FieldMetadata(alias="userMessageType")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
