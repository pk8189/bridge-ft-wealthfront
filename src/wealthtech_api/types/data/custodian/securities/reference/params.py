"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostDataCustodianSecuritiesReferenceBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    reported_date: typing_extensions.Required[str]


class _SerializerPostDataCustodianSecuritiesReferenceBody(pydantic.BaseModel):
    """
    Serializer for PostDataCustodianSecuritiesReferenceBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    reported_date: str = pydantic.Field(alias="reported_date")
