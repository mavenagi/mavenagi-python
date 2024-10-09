# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
from .event_trigger_type import EventTriggerType
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class EventTriggerBase(UniversalBaseModel):
    description: str = pydantic.Field()
    """
    The description of what the event trigger does, shown in the Maven Dashboard
    """

    type: EventTriggerType = pydantic.Field()
    """
    The type of event trigger this app wishes to handle
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
