# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ...core.serialization import FieldMetadata
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class SubmitActionFormRequest(UniversalBaseModel):
    action_form_id: typing_extensions.Annotated[str, FieldMetadata(alias="actionFormId")]
    parameters: typing.Dict[str, typing.Optional[typing.Any]] = pydantic.Field()
    """
    Map of parameter IDs to values provided by the user. All required action fields must be provided.
    """

    transient_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="transientData")
    ] = pydantic.Field(default=None)
    """
    Transient data which the Maven platform will not persist. This data will only be forwarded to actions taken. For example, one may put in user tokens as transient data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
