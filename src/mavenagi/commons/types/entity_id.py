# This file was auto-generated by Fern from our API Definition.

from .entity_id_without_agent import EntityIdWithoutAgent
import typing_extensions
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class EntityId(EntityIdWithoutAgent):
    """
    A fully specified object ID, unique across the entire system.
    """

    organization_id: typing_extensions.Annotated[str, FieldMetadata(alias="organizationId")] = pydantic.Field()
    """
    The ID of the organization that this object belongs to
    """

    agent_id: typing_extensions.Annotated[str, FieldMetadata(alias="agentId")] = pydantic.Field()
    """
    The ID of the agent that this object belongs to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
