# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class BasePaginatedRequest(UniversalBaseModel):
    page: typing.Optional[int] = pydantic.Field(default=None)
    """
    Page number to return, defaults to 0
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The size of the page to return, defaults to 20
    """

    sort_desc: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="sortDesc")] = pydantic.Field(
        default=None
    )
    """
    Whether to sort descending, defaults to true
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
