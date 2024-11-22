# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ...core.serialization import FieldMetadata
import typing
from .action_form_field import ActionFormField
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class BotActionFormResponse(UniversalBaseModel):
    """
    This response should be rendered as a form which users can submit. Upon submission call the submit action form API.
    """

    id: str
    form_label: typing_extensions.Annotated[str, FieldMetadata(alias="formLabel")]
    fields: typing.List[ActionFormField]
    submit_label: typing_extensions.Annotated[str, FieldMetadata(alias="submitLabel")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
