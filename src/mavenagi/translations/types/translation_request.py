# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing_extensions
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class TranslationRequest(UniversalBaseModel):
    """
    Examples
    --------
    from mavenagi.translations import TranslationRequest

    TranslationRequest(
        text="Hello world",
        target_language="es",
    )
    """

    text: str = pydantic.Field()
    """
    The text to translate
    """

    target_language: typing_extensions.Annotated[str, FieldMetadata(alias="targetLanguage")] = pydantic.Field()
    """
    The target language to translate to, in ISO 639-1 code format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow