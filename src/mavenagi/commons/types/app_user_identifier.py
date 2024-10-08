# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
from .app_user_identifying_property_type import AppUserIdentifyingPropertyType
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class AppUserIdentifier(UniversalBaseModel):
    value: str = pydantic.Field()
    """
    The identifying property text
    """

    type: AppUserIdentifyingPropertyType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
