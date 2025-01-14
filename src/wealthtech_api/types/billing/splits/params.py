"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostBillingSplitsBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    firm_id: typing_extensions.NotRequired[int]
    name: typing_extensions.NotRequired[str]
    percentage: typing_extensions.NotRequired[float]
    splitter_name: typing_extensions.NotRequired[str]
    splitter_slug: typing_extensions.NotRequired[str]


class _SerializerPostBillingSplitsBody(pydantic.BaseModel):
    """
    Serializer for PostBillingSplitsBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    percentage: typing.Optional[float] = pydantic.Field(
        alias="percentage", default=None
    )
    splitter_name: typing.Optional[str] = pydantic.Field(
        alias="splitter_name", default=None
    )
    splitter_slug: typing.Optional[str] = pydantic.Field(
        alias="splitter_slug", default=None
    )


class SplitItem(typing_extensions.TypedDict):
    """
    No description specified
    """

    created_at_utc: typing_extensions.NotRequired[str]
    firm_id: typing_extensions.NotRequired[int]
    id: typing_extensions.NotRequired[int]
    name: typing_extensions.NotRequired[str]
    percentage: typing_extensions.NotRequired[float]
    splitter_name: typing_extensions.NotRequired[str]
    splitter_slug: typing_extensions.NotRequired[str]
    updated_at_utc: typing_extensions.NotRequired[str]


class _SerializerSplitItem(pydantic.BaseModel):
    """
    Serializer for SplitItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    created_at_utc: typing.Optional[str] = pydantic.Field(
        alias="created_at_utc", default=None
    )
    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    percentage: typing.Optional[float] = pydantic.Field(
        alias="percentage", default=None
    )
    splitter_name: typing.Optional[str] = pydantic.Field(
        alias="splitter_name", default=None
    )
    splitter_slug: typing.Optional[str] = pydantic.Field(
        alias="splitter_slug", default=None
    )
    updated_at_utc: typing.Optional[str] = pydantic.Field(
        alias="updated_at_utc", default=None
    )


class PutBillingSplitsIdBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    created_at_utc: typing_extensions.NotRequired[str]
    firm_id: typing_extensions.NotRequired[int]
    id: typing_extensions.NotRequired[int]
    name: typing_extensions.NotRequired[str]
    percentage: typing_extensions.NotRequired[float]
    splitter_name: typing_extensions.NotRequired[str]
    splitter_slug: typing_extensions.NotRequired[str]
    updated_at_utc: typing_extensions.NotRequired[str]


class _SerializerPutBillingSplitsIdBody(pydantic.BaseModel):
    """
    Serializer for PutBillingSplitsIdBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    created_at_utc: typing.Optional[str] = pydantic.Field(
        alias="created_at_utc", default=None
    )
    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    percentage: typing.Optional[float] = pydantic.Field(
        alias="percentage", default=None
    )
    splitter_name: typing.Optional[str] = pydantic.Field(
        alias="splitter_name", default=None
    )
    splitter_slug: typing.Optional[str] = pydantic.Field(
        alias="splitter_slug", default=None
    )
    updated_at_utc: typing.Optional[str] = pydantic.Field(
        alias="updated_at_utc", default=None
    )
