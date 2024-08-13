"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostStatusSourceDataBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    as_of_date: typing_extensions.NotRequired[str]


class _SerializerPostStatusSourceDataBody(pydantic.BaseModel):
    """
    Serializer for PostStatusSourceDataBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    as_of_date: typing.Optional[str] = pydantic.Field(alias="as_of_date", default=None)