# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ...commons.types.entity_id_base import EntityIdBase
from ...core.serialization import FieldMetadata
import pydantic
import typing
from .attachment import Attachment
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class AskRequest(UniversalBaseModel):
    """
    Examples
    --------
    from mavenagi.commons import EntityIdBase
    from mavenagi.conversation import AskRequest, Attachment

    AskRequest(
        conversation_message_id=EntityIdBase(
            reference_id="message-1",
        ),
        user_id=EntityIdBase(
            reference_id="user-1",
        ),
        text="How do I reset my password?",
        attachments=[
            Attachment(
                type="image/png",
                content="iVBORw0KGgo...",
            )
        ],
    )
    """

    conversation_message_id: typing_extensions.Annotated[EntityIdBase, FieldMetadata(alias="conversationMessageId")] = (
        pydantic.Field()
    )
    """
    Externally supplied ID to uniquely identify this message within the conversation
    """

    user_id: typing_extensions.Annotated[EntityIdBase, FieldMetadata(alias="userId")] = pydantic.Field()
    """
    Externally supplied ID to uniquely identify the user that created this message
    """

    text: str = pydantic.Field()
    """
    The text of the message
    """

    attachments: typing.Optional[typing.List[Attachment]] = pydantic.Field(default=None)
    """
    The attachments to the message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
