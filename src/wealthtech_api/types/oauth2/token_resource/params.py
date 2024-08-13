"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostOauth2TokenBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    grant_type: typing_extensions.Required[str]


class _SerializerPostOauth2TokenBody(pydantic.BaseModel):
    """
    Serializer for PostOauth2TokenBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    grant_type: str = pydantic.Field(alias="grant_type")