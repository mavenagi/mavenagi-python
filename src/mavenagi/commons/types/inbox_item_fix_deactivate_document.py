# This file was auto-generated by Fern from our API Definition.

from .inbox_item_fix_base import InboxItemFixBase
import typing_extensions
from .document_information import DocumentInformation
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class InboxItemFixDeactivateDocument(InboxItemFixBase):
    document_information: typing_extensions.Annotated[
        DocumentInformation, FieldMetadata(alias="documentInformation")
    ] = pydantic.Field()
    """
    Information about the document associated with this fix.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
