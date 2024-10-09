# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
import typing_extensions
from ...core.serialization import FieldMetadata
from .action_form_field import ActionFormField


class BotResponse_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BotResponse_ActionForm(UniversalBaseModel):
    type: typing.Literal["actionForm"] = "actionForm"
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


BotResponse = typing.Union[BotResponse_Text, BotResponse_ActionForm]
