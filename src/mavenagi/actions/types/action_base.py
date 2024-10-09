# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .action_parameter import ActionParameter
from .precondition import Precondition

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ActionBase(pydantic.BaseModel):
    name: str = pydantic.Field()
    """
    The name of the action. This is displayed to the end user as part of forms when user interaction is required. It is also used to help Maven decide if the action is relevant to a conversation.
    """

    description: str = pydantic.Field()
    """
    The description of the action. This helps Maven decide if the action is relevant to a conversation and is not displayed directly to the end user.
    """

    user_interaction_required: bool = pydantic.Field(alias="userInteractionRequired")
    """
    Whether the action requires user interaction to execute. If false, and all of the required action parameters are known, the LLM may call the action automatically. If true, an conversations ask call will return a BotActionFormResponse which must be submitted by an API caller. API callers must display a button with the buttonName label to confirm the user's intent.
    """

    button_name: typing.Optional[str] = pydantic.Field(alias="buttonName", default=None)
    """
    When user interaction is required, the name of the button that is shown to the end user to confirm execution of the action
    """

    precondition: typing.Optional[Precondition] = pydantic.Field(default=None)
    """
    The preconditions that must be met for an action to be relevant to a conversation. Can be used to restrict actions to certain types of users.
    """

    user_form_parameters: typing.List[ActionParameter] = pydantic.Field(alias="userFormParameters")
    """
    The parameters that the action uses as input. An action will only be executed when all of the required parameters are provided. During execution, actions all have access to the full Conversation and User objects. Parameter values may be inferred from the user's conversation by the LLM.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
