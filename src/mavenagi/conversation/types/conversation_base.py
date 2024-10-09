# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .response_config import ResponseConfig

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ConversationBase(pydantic.BaseModel):
    response_config: typing.Optional[ResponseConfig] = pydantic.Field(alias="responseConfig", default=None)
    """
    Optional configurations for responses to this conversation
    """

    subject: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subject of the conversation
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The url of the conversation
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(alias="createdAt", default=None)
    """
    The date and time the conversation was created
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(alias="updatedAt", default=None)
    """
    The date and time the conversation was last updated
    """

    tags: typing.Optional[typing.Set[str]] = pydantic.Field(default=None)
    """
    The tags of the conversation. Used for filtering in Agent Designer.
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    The metadata of the conversation.
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