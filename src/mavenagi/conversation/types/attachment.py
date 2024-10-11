# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class Attachment(UniversalBaseModel):
    type: str = pydantic.Field()
    """
    The mime-type of the attachment. Supported types are {image/jpeg, image/jpg, image/png, image/gif, image/webp}.
    """

    content: str = pydantic.Field()
    """
    The attachment data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow