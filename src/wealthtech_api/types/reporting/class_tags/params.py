"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostReportingClassTagsBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    firm_id: typing_extensions.NotRequired[int]
    name: typing_extensions.NotRequired[str]


class _SerializerPostReportingClassTagsBody(pydantic.BaseModel):
    """
    Serializer for PostReportingClassTagsBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)


class ClassificationTag(typing_extensions.TypedDict):
    """
    No description specified
    """

    created_at_utc: typing_extensions.NotRequired[str]
    created_dt_utc: typing_extensions.NotRequired[str]
    firm_id: typing_extensions.NotRequired[int]
    id: typing_extensions.NotRequired[int]
    name: typing_extensions.NotRequired[str]
    updated_at_utc: typing_extensions.NotRequired[str]


class _SerializerClassificationTag(pydantic.BaseModel):
    """
    Serializer for ClassificationTag handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    created_at_utc: typing.Optional[str] = pydantic.Field(
        alias="created_at_utc", default=None
    )
    created_dt_utc: typing.Optional[str] = pydantic.Field(
        alias="created_dt_utc", default=None
    )
    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    updated_at_utc: typing.Optional[str] = pydantic.Field(
        alias="updated_at_utc", default=None
    )
