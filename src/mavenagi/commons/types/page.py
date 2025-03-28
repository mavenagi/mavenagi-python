# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing_extensions
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class Page(UniversalBaseModel):
    number: int = pydantic.Field()
    """
    The page being returned, starts at 0
    """

    size: int = pydantic.Field()
    """
    The number of elements in this page
    """

    total_elements: typing_extensions.Annotated[int, FieldMetadata(alias="totalElements")] = pydantic.Field()
    """
    The total number of elements in the collection
    """

    total_pages: typing_extensions.Annotated[int, FieldMetadata(alias="totalPages")] = pydantic.Field()
    """
    The total number of pages in the collection
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
