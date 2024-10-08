# This file was auto-generated by Fern from our API Definition.

from .base_knowledge_document import BaseKnowledgeDocument
import typing_extensions
from ...commons.types.entity_id_base import EntityIdBase
from ...core.serialization import FieldMetadata
import pydantic
from .knowledge_document_content_type import KnowledgeDocumentContentType
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class KnowledgeDocumentRequest(BaseKnowledgeDocument):
    """
    Examples
    --------
    from mavenagi.commons import EntityIdBase
    from mavenagi.knowledge import KnowledgeDocumentRequest

    KnowledgeDocumentRequest(
        knowledge_document_id=EntityIdBase(
            reference_id="getting-started",
        ),
        content_type="MARKDOWN",
        content="## Getting started\\nThis is a getting started guide for the help center.",
        title="Getting started",
    )
    """

    knowledge_document_id: typing_extensions.Annotated[EntityIdBase, FieldMetadata(alias="knowledgeDocumentId")] = (
        pydantic.Field()
    )
    """
    ID that uniquely identifies this knowledge document within its knowledge base
    """

    content_type: typing_extensions.Annotated[KnowledgeDocumentContentType, FieldMetadata(alias="contentType")]
    content: str = pydantic.Field()
    """
    The content of the document. Not shown directly to users. May be provided in HTML or markdown. HTML will be converted to markdown automatically. Images are not currently supported and will be ignored.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
