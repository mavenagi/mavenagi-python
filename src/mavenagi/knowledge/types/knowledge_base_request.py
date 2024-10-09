# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...commons.types.entity_id_base import EntityIdBase
from ...core.datetime_utils import serialize_datetime
from .knowledge_base_properties import KnowledgeBaseProperties

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class KnowledgeBaseRequest(KnowledgeBaseProperties):
    """
    from mavenagi import EntityIdBase, KnowledgeBaseRequest

    KnowledgeBaseRequest(
        knowledge_base_id=EntityIdBase(
            reference_id="help-center",
        ),
        name="Help center",
        type="API",
    )
    """

    knowledge_base_id: EntityIdBase = pydantic.Field(alias="knowledgeBaseId")
    """
    ID that uniquely identifies this knowledge base
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
