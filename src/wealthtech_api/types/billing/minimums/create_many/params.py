"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostBillingMinimumsCreateManyBodyItem(typing_extensions.TypedDict):
    """
    No description specified
    """

    firm_id: typing_extensions.NotRequired[int]
    name: typing_extensions.NotRequired[str]
    value: typing_extensions.NotRequired[float]
    value_type: typing_extensions.NotRequired[typing_extensions.Literal["F", "P"]]


class _SerializerPostBillingMinimumsCreateManyBodyItem(pydantic.BaseModel):
    """
    Serializer for PostBillingMinimumsCreateManyBodyItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    value: typing.Optional[float] = pydantic.Field(alias="value", default=None)
    value_type: typing.Optional[typing_extensions.Literal["F", "P"]] = pydantic.Field(
        alias="value_type", default=None
    )
