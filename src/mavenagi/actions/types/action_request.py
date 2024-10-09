# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from .action_base import ActionBase
from .precondition_group import PreconditionGroup
import typing_extensions
from ...commons.types.entity_id_base import EntityIdBase
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
from ...core.pydantic_utilities import update_forward_refs


class ActionRequest(ActionBase):
    """
    Examples
    --------
    from mavenagi.actions import (
        ActionRequest,
        Precondition_Group,
        Precondition_User,
    )
    from mavenagi.commons import EntityIdBase

    ActionRequest(
        action_id=EntityIdBase(
            reference_id="get-balance",
        ),
        name="Get the user's balance",
        description="This action calls an API to get the user's current balance.",
        user_interaction_required=False,
        user_form_parameters=[],
        precondition=Precondition_Group(
            operator="AND",
            preconditions=[
                Precondition_User(
                    key="userKey",
                ),
                Precondition_User(
                    key="userKey2",
                ),
            ],
        ),
    )
    """

    action_id: typing_extensions.Annotated[EntityIdBase, FieldMetadata(alias="actionId")] = pydantic.Field()
    """
    ID that uniquely identifies this action
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(PreconditionGroup, ActionRequest=ActionRequest)
