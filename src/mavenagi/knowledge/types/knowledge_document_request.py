# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...commons.types.entity_id_base import EntityIdBase
from ...core.datetime_utils import serialize_datetime
from .base_knowledge_document import BaseKnowledgeDocument
from .knowledge_document_content_type import KnowledgeDocumentContentType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class KnowledgeDocumentRequest(BaseKnowledgeDocument):
    """
    from mavenagi import EntityIdBase, KnowledgeDocumentRequest

    KnowledgeDocumentRequest(
        knowledge_document_id=EntityIdBase(
            reference_id="getting-started",
        ),
        content_type="MARKDOWN",
        content="## Getting started\\nThis is a getting started guide for the help center.",
        title="Getting started",
    )
    """

    knowledge_document_id: EntityIdBase = pydantic.Field(alias="knowledgeDocumentId")
    """
    ID that uniquely identifies this knowledge document within its knowledge base
    """

    content_type: KnowledgeDocumentContentType = pydantic.Field(alias="contentType")
    content: str = pydantic.Field()
    """
    The content of the document. Not shown directly to users. May be provided in HTML or markdown. HTML will be converted to markdown automatically. Images are not currently supported and will be ignored.
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