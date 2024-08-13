"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostBillingAssetAdjustmentsDeleteManyBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    ids: typing_extensions.NotRequired[typing.List[int]]


class _SerializerPostBillingAssetAdjustmentsDeleteManyBody(pydantic.BaseModel):
    """
    Serializer for PostBillingAssetAdjustmentsDeleteManyBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ids: typing.Optional[typing.List[int]] = pydantic.Field(alias="ids", default=None)
