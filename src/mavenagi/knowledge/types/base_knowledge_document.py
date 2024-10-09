# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class BaseKnowledgeDocument(pydantic.BaseModel):
    title: str = pydantic.Field()
    """
    The title of the document. Will be shown as part of answers.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the document. Should be visible to end users. Will be shown as part of answers. Not used for crawling.
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    The document language. Must be a valid ISO 639-1 language code.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(alias="createdAt", default=None)
    """
    The time at which this document was created.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(alias="updatedAt", default=None)
    """
    The time at which this document was last modified.
    """

    author: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the author who created this document.
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