# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from .knowledge_base_properties import KnowledgeBaseProperties
from ...commons.types.precondition_group import PreconditionGroup
import typing_extensions
from ...commons.types.entity_id import EntityId
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
from ...core.pydantic_utilities import update_forward_refs


class KnowledgeBaseResponse(KnowledgeBaseProperties):
    """
    Examples
    --------
    from mavenagi.commons import EntityId
    from mavenagi.knowledge import KnowledgeBaseResponse

    KnowledgeBaseResponse(
        knowledge_base_id=EntityId(
            reference_id="help-center",
            app_id="readme",
            organization_id="acme",
            agent_id="support",
            type="KNOWLEDGE_BASE",
        ),
        name="Help center",
        type="API",
    )
    """

    knowledge_base_id: typing_extensions.Annotated[EntityId, FieldMetadata(alias="knowledgeBaseId")] = pydantic.Field()
    """
    ID that uniquely identifies this knowledge base
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(PreconditionGroup, KnowledgeBaseResponse=KnowledgeBaseResponse)
