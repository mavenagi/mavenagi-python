# This file was auto-generated by Fern from our API Definition.

from ...commons.types.feedback_base import FeedbackBase
import typing_extensions
from ...commons.types.entity_id_base import EntityIdBase
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class FeedbackRequest(FeedbackBase):
    feedback_id: typing_extensions.Annotated[EntityIdBase, FieldMetadata(alias="feedbackId")] = pydantic.Field()
    """
    The ID that uniquely identifies this feedback
    """

    conversation_id: typing_extensions.Annotated[EntityIdBase, FieldMetadata(alias="conversationId")] = pydantic.Field()
    """
    The ID that uniquely identifies the the conversation the feedback is about
    """

    conversation_message_id: typing_extensions.Annotated[EntityIdBase, FieldMetadata(alias="conversationMessageId")] = (
        pydantic.Field()
    )
    """
    The ID that uniquely identifies the message within the conversation the feedback is about
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
