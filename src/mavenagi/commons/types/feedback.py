# This file was auto-generated by Fern from our API Definition.

from .feedback_base import FeedbackBase
import typing_extensions
from .entity_id import EntityId
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class Feedback(FeedbackBase):
    """
    Examples
    --------
    from mavenagi.commons import EntityId, Feedback

    Feedback(
        feedback_id=EntityId(
            reference_id="feedback-0",
            app_id="myapp",
            organization_id="acme",
            agent_id="support",
            type="FEEDBACK",
        ),
        conversation_id=EntityId(
            reference_id="conversation-0",
            app_id="myapp",
            organization_id="acme",
            agent_id="support",
            type="CONVERSATION",
        ),
        conversation_message_id=EntityId(
            reference_id="message-1",
            app_id="myapp",
            organization_id="acme",
            agent_id="support",
            type="CONVERSATION_MESSAGE",
        ),
        type="THUMBS_UP",
        text="Great answer!",
    )
    """

    feedback_id: typing_extensions.Annotated[EntityId, FieldMetadata(alias="feedbackId")] = pydantic.Field()
    """
    The ID of the piece of feedback
    """

    conversation_id: typing_extensions.Annotated[EntityId, FieldMetadata(alias="conversationId")] = pydantic.Field()
    """
    The ID of the conversation the feedback is about
    """

    conversation_message_id: typing_extensions.Annotated[EntityId, FieldMetadata(alias="conversationMessageId")] = (
        pydantic.Field()
    )
    """
    The ID of the conversation message the feedback is about
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
