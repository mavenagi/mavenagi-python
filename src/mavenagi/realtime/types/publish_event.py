# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PublishEvent_Audio(UniversalBaseModel):
    """
    The input from the user to send through the WebSocket.
    """

    message_type: typing_extensions.Annotated[typing.Literal["audio"], FieldMetadata(alias="messageType")] = "audio"
    audio_content: typing_extensions.Annotated[str, FieldMetadata(alias="audioContent")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PublishEvent = PublishEvent_Audio
