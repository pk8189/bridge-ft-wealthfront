"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostAnalyticsAumByAccountBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    account_ids: typing_extensions.Required[typing.List[int]]
    as_of_date: typing_extensions.NotRequired[str]


class _SerializerPostAnalyticsAumByAccountBody(pydantic.BaseModel):
    """
    Serializer for PostAnalyticsAumByAccountBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_ids: typing.List[int] = pydantic.Field(alias="account_ids")
    as_of_date: typing.Optional[str] = pydantic.Field(alias="as_of_date", default=None)
