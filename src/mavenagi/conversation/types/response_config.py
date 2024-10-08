# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .capability import Capability
import pydantic
import typing_extensions
from ...core.serialization import FieldMetadata
from .response_length import ResponseLength
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ResponseConfig(UniversalBaseModel):
    capabilities: typing.List[Capability] = pydantic.Field()
    """
    List of capabilities supported by the caller. Defaults to all. Only the markdown capability is supported at this time. If not provided, responses will be plain text.
    """

    is_copilot: typing_extensions.Annotated[bool, FieldMetadata(alias="isCopilot")] = pydantic.Field()
    """
    Whether the response is for an human agent (true) or an end user (false). Defaults to false.
    """

    response_length: typing_extensions.Annotated[ResponseLength, FieldMetadata(alias="responseLength")] = (
        pydantic.Field()
    )
    """
    The desired response length. Defaults to ResponseLength.MEDIUM.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
