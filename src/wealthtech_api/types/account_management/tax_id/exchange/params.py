"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostAccountManagementTaxIdExchangeBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    tax_id_tokens: typing_extensions.NotRequired[typing.List[str]]


class _SerializerPostAccountManagementTaxIdExchangeBody(pydantic.BaseModel):
    """
    Serializer for PostAccountManagementTaxIdExchangeBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tax_id_tokens: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="tax_id_tokens", default=None
    )