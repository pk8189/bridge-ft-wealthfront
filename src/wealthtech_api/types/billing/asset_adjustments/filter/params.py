"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostBillingAssetAdjustmentsFilterBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    adjustment_type: typing_extensions.NotRequired[typing_extensions.Literal["i", "e"]]
    firm_id: typing_extensions.NotRequired[int]
    id: typing_extensions.NotRequired[int]
    level: typing_extensions.NotRequired[typing_extensions.Literal["f", "a"]]
    name: typing_extensions.NotRequired[str]
    security_ids: typing_extensions.NotRequired[typing.List[int]]
    slug: typing_extensions.NotRequired[str]


class _SerializerPostBillingAssetAdjustmentsFilterBody(pydantic.BaseModel):
    """
    Serializer for PostBillingAssetAdjustmentsFilterBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    adjustment_type: typing.Optional[typing_extensions.Literal["e", "i"]] = (
        pydantic.Field(alias="adjustment_type", default=None)
    )
    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    level: typing.Optional[typing_extensions.Literal["a", "f"]] = pydantic.Field(
        alias="level", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    security_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="security_ids", default=None
    )
    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)