# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ...commons.types.action_form_field import ActionFormField
from ...commons.types.chart_spec_schema import ChartSpecSchema
from ...commons.types.source import Source
from ...commons.types.entity_id import EntityId
from ...commons.types.error_message import ErrorMessage


class StreamResponse_Text(UniversalBaseModel):
    event_type: typing_extensions.Annotated[typing.Literal["text"], FieldMetadata(alias="eventType")] = "text"
    contents: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamResponse_Action(UniversalBaseModel):
    event_type: typing_extensions.Annotated[typing.Literal["action"], FieldMetadata(alias="eventType")] = "action"
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


class StreamResponse_Chart(UniversalBaseModel):
    event_type: typing_extensions.Annotated[typing.Literal["chart"], FieldMetadata(alias="eventType")] = "chart"
    label: str
    spec_schema: typing_extensions.Annotated[ChartSpecSchema, FieldMetadata(alias="specSchema")]
    spec: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamResponse_Metadata(UniversalBaseModel):
    event_type: typing_extensions.Annotated[typing.Literal["metadata"], FieldMetadata(alias="eventType")] = "metadata"
    followup_questions: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="followupQuestions")]
    sources: typing.List[Source]
    language: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamResponse_Start(UniversalBaseModel):
    event_type: typing_extensions.Annotated[typing.Literal["start"], FieldMetadata(alias="eventType")] = "start"
    conversation_message_id: typing_extensions.Annotated[EntityId, FieldMetadata(alias="conversationMessageId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamResponse_End(UniversalBaseModel):
    event_type: typing_extensions.Annotated[typing.Literal["end"], FieldMetadata(alias="eventType")] = "end"
    error: typing.Optional[ErrorMessage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


StreamResponse = typing.Union[
    StreamResponse_Text,
    StreamResponse_Action,
    StreamResponse_Chart,
    StreamResponse_Metadata,
    StreamResponse_Start,
    StreamResponse_End,
]
