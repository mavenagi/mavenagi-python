# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ...conversation.types.numeric_conversation_field import NumericConversationField
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class ConversationNumericMetric(UniversalBaseModel):
    target_field: typing_extensions.Annotated[NumericConversationField, FieldMetadata(alias="targetField")] = (
        pydantic.Field()
    )
    """
    Numeric field to apply the metric to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
