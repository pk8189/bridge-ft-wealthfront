"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostAnalyticsAumFilterBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    as_of_date: typing_extensions.NotRequired[str]
    firm_id: typing_extensions.NotRequired[int]
    frequency: typing_extensions.NotRequired[typing_extensions.Literal["M", "D"]]
    id: typing_extensions.NotRequired[int]
    total: typing_extensions.NotRequired[float]


class _SerializerPostAnalyticsAumFilterBody(pydantic.BaseModel):
    """
    Serializer for PostAnalyticsAumFilterBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    as_of_date: typing.Optional[str] = pydantic.Field(alias="as_of_date", default=None)
    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    frequency: typing.Optional[typing_extensions.Literal["M", "D"]] = pydantic.Field(
        alias="frequency", default=None
    )
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    total: typing.Optional[float] = pydantic.Field(alias="total", default=None)