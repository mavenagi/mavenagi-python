# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...commons.types.entity_id import EntityId
from ...core.datetime_utils import serialize_datetime
from .base_knowledge_document import BaseKnowledgeDocument

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class KnowledgeDocumentResponse(BaseKnowledgeDocument):
    """
    from mavenagi import EntityId, KnowledgeDocumentResponse

    KnowledgeDocumentResponse(
        knowledge_document_id=EntityId(
            reference_id="getting-started",
            app_id="readme",
            organization_id="acme",
            agent_id="support",
            type="KNOWLEDGE_DOCUMENT",
        ),
        content="## Getting started This is a getting started guide for the help center.",
        title="Getting started",
    )
    """

    knowledge_document_id: EntityId = pydantic.Field(alias="knowledgeDocumentId")
    """
    ID that uniquely identifies this knowledge document within its knowledge base
    """

    content: str = pydantic.Field()
    """
    The content of the document in markdown format. Not shown directly to users.
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
