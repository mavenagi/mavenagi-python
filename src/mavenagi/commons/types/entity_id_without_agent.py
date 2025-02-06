# This file was auto-generated by Fern from our API Definition.

from .entity_id_base import EntityIdBase
from .entity_type import EntityType
import pydantic
import typing_extensions
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class EntityIdWithoutAgent(EntityIdBase):
    """
    The organizationId and agentId are inferred from the context.
    """

    type: EntityType = pydantic.Field()
    """
    The object type
    """

    app_id: typing_extensions.Annotated[str, FieldMetadata(alias="appId")] = pydantic.Field()
    """
    The ID of the application that created this object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
