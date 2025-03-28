# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...core.pydantic_utilities import UniversalBaseModel
import typing
import typing_extensions
from ...core.serialization import FieldMetadata
from .entity_id import EntityId
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from .document_information import DocumentInformation
from .knowledge_base_information import KnowledgeBaseInformation


class InboxItemFix_AddDocument(UniversalBaseModel):
    type: typing.Literal["addDocument"] = "addDocument"
    suggested_text_title: typing_extensions.Annotated[str, FieldMetadata(alias="suggestedTextTitle")]
    suggested_text: typing_extensions.Annotated[str, FieldMetadata(alias="suggestedText")]
    id: EntityId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InboxItemFix_DeactivateDocument(UniversalBaseModel):
    type: typing.Literal["deactivateDocument"] = "deactivateDocument"
    document_information: typing_extensions.Annotated[DocumentInformation, FieldMetadata(alias="documentInformation")]
    id: EntityId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InboxItemFix_DeactivateKnowledgeBase(UniversalBaseModel):
    type: typing.Literal["deactivateKnowledgeBase"] = "deactivateKnowledgeBase"
    knowledge_base: typing_extensions.Annotated[KnowledgeBaseInformation, FieldMetadata(alias="knowledgeBase")]
    id: EntityId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


InboxItemFix = typing.Union[
    InboxItemFix_AddDocument, InboxItemFix_DeactivateDocument, InboxItemFix_DeactivateKnowledgeBase
]
