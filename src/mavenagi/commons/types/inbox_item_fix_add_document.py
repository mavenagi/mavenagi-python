# This file was auto-generated by Fern from our API Definition.

from .inbox_item_fix_base import InboxItemFixBase
import typing_extensions
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class InboxItemFixAddDocument(InboxItemFixBase):
    suggested_text_title: typing_extensions.Annotated[str, FieldMetadata(alias="suggestedTextTitle")] = pydantic.Field()
    """
    Suggested document title if the fix type is ADD_DOCUMENT.
    """

    suggested_text: typing_extensions.Annotated[str, FieldMetadata(alias="suggestedText")] = pydantic.Field()
    """
    Suggested document text if the fix type is ADD_DOCUMENT.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
