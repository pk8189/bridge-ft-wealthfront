"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostBillingFeeUploadFilesFilterBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    end_date: typing_extensions.NotRequired[str]
    firm_id: typing_extensions.NotRequired[int]
    id: typing_extensions.NotRequired[int]
    num_accounts: typing_extensions.NotRequired[int]
    num_custodians: typing_extensions.NotRequired[int]
    num_files: typing_extensions.NotRequired[int]
    num_households: typing_extensions.NotRequired[typing.Optional[int]]
    total_annual_debit: typing_extensions.NotRequired[typing.Optional[float]]
    total_period_debit: typing_extensions.NotRequired[typing.Optional[float]]


class _SerializerPostBillingFeeUploadFilesFilterBody(pydantic.BaseModel):
    """
    Serializer for PostBillingFeeUploadFilesFilterBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    end_date: typing.Optional[str] = pydantic.Field(alias="end_date", default=None)
    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    num_accounts: typing.Optional[int] = pydantic.Field(
        alias="num_accounts", default=None
    )
    num_custodians: typing.Optional[int] = pydantic.Field(
        alias="num_custodians", default=None
    )
    num_files: typing.Optional[int] = pydantic.Field(alias="num_files", default=None)
    num_households: typing.Optional[int] = pydantic.Field(
        alias="num_households", default=None
    )
    total_annual_debit: typing.Optional[float] = pydantic.Field(
        alias="total_annual_debit", default=None
    )
    total_period_debit: typing.Optional[float] = pydantic.Field(
        alias="total_period_debit", default=None
    )