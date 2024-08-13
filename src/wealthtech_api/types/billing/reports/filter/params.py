"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostBillingReportsFilterBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    annual_debit: typing_extensions.NotRequired[float]
    annual_fee: typing_extensions.NotRequired[float]
    aum_on_billing_date: typing_extensions.NotRequired[float]
    billing_date: typing_extensions.NotRequired[str]
    created_date: typing_extensions.NotRequired[str]
    created_invoices: typing_extensions.NotRequired[bool]
    custodian_billed_period_debit: typing_extensions.NotRequired[float]
    direct_billed_period_debit: typing_extensions.NotRequired[typing.Optional[float]]
    fee_upload_file_id: typing_extensions.NotRequired[typing.Optional[int]]
    firm_id: typing_extensions.NotRequired[int]
    firm_share: typing_extensions.NotRequired[float]
    firm_share_annualized: typing_extensions.NotRequired[float]
    id: typing_extensions.NotRequired[int]
    n_accounts: typing_extensions.NotRequired[int]
    n_fee_structures: typing_extensions.NotRequired[int]
    n_groups: typing_extensions.NotRequired[int]
    n_splits: typing_extensions.NotRequired[int]
    period_debit: typing_extensions.NotRequired[float]
    run_date: typing_extensions.NotRequired[str]
    snapshot_date: typing_extensions.NotRequired[str]
    split_payout: typing_extensions.NotRequired[typing.Optional[float]]
    split_payout_annualized: typing_extensions.NotRequired[typing.Optional[float]]
    total_balance: typing_extensions.NotRequired[float]


class _SerializerPostBillingReportsFilterBody(pydantic.BaseModel):
    """
    Serializer for PostBillingReportsFilterBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    annual_debit: typing.Optional[float] = pydantic.Field(
        alias="annual_debit", default=None
    )
    annual_fee: typing.Optional[float] = pydantic.Field(
        alias="annual_fee", default=None
    )
    aum_on_billing_date: typing.Optional[float] = pydantic.Field(
        alias="aum_on_billing_date", default=None
    )
    billing_date: typing.Optional[str] = pydantic.Field(
        alias="billing_date", default=None
    )
    created_date: typing.Optional[str] = pydantic.Field(
        alias="created_date", default=None
    )
    created_invoices: typing.Optional[bool] = pydantic.Field(
        alias="created_invoices", default=None
    )
    custodian_billed_period_debit: typing.Optional[float] = pydantic.Field(
        alias="custodian_billed_period_debit", default=None
    )
    direct_billed_period_debit: typing.Optional[float] = pydantic.Field(
        alias="direct_billed_period_debit", default=None
    )
    fee_upload_file_id: typing.Optional[int] = pydantic.Field(
        alias="fee_upload_file_id", default=None
    )
    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    firm_share: typing.Optional[float] = pydantic.Field(
        alias="firm_share", default=None
    )
    firm_share_annualized: typing.Optional[float] = pydantic.Field(
        alias="firm_share_annualized", default=None
    )
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    n_accounts: typing.Optional[int] = pydantic.Field(alias="n_accounts", default=None)
    n_fee_structures: typing.Optional[int] = pydantic.Field(
        alias="n_fee_structures", default=None
    )
    n_groups: typing.Optional[int] = pydantic.Field(alias="n_groups", default=None)
    n_splits: typing.Optional[int] = pydantic.Field(alias="n_splits", default=None)
    period_debit: typing.Optional[float] = pydantic.Field(
        alias="period_debit", default=None
    )
    run_date: typing.Optional[str] = pydantic.Field(alias="run_date", default=None)
    snapshot_date: typing.Optional[str] = pydantic.Field(
        alias="snapshot_date", default=None
    )
    split_payout: typing.Optional[float] = pydantic.Field(
        alias="split_payout", default=None
    )
    split_payout_annualized: typing.Optional[float] = pydantic.Field(
        alias="split_payout_annualized", default=None
    )
    total_balance: typing.Optional[float] = pydantic.Field(
        alias="total_balance", default=None
    )