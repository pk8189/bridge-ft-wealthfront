"""File Generated by Sideko (sideko.dev)"""

import io
import typing

import typing_extensions
import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class Account(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    acct_type: typing.Optional[str] = pydantic.Field(alias="acct_type", default=None)
    address_1: typing.Optional[str] = pydantic.Field(alias="address_1", default=None)
    address_2: typing.Optional[str] = pydantic.Field(alias="address_2", default=None)
    address_3: typing.Optional[str] = pydantic.Field(alias="address_3", default=None)
    advisor_code: typing.Optional[str] = pydantic.Field(
        alias="advisor_code", default=None
    )
    advisor_codes: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="advisor_codes", default=None
    )
    benchmarks_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="benchmarks_ids", default=None
    )
    billing_splits_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="billing_splits_ids", default=None
    )
    buy_securities_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="buy_securities_ids", default=None
    )
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    close_date: typing.Optional[str] = pydantic.Field(alias="close_date", default=None)
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    created_at_utc: typing.Optional[str] = pydantic.Field(
        alias="created_at_utc", default=None
    )
    custodian: typing.Optional[
        typing_extensions.Literal[
            "MLT", "IBK", "TIA", "DST", "FPR", "NFS", "PER", "SWB", "EGB", "APX"
        ]
    ] = pydantic.Field(alias="custodian", default=None)
    custodian_name: typing.Optional[str] = pydantic.Field(
        alias="custodian_name", default=None
    )
    display_name: typing.Optional[str] = pydantic.Field(
        alias="display_name", default=None
    )
    display_number: typing.Optional[str] = pydantic.Field(
        alias="display_number", default=None
    )
    do_not_buy_securities_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="do_not_buy_securities_ids", default=None
    )
    do_not_sell_securities_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="do_not_sell_securities_ids", default=None
    )
    entity_id: typing.Optional[str] = pydantic.Field(alias="entity_id", default=None)
    fee_structures_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="fee_structures_ids", default=None
    )
    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    first_billable_date: typing.Optional[str] = pydantic.Field(
        alias="first_billable_date", default=None
    )
    first_cost_basis_date: typing.Optional[str] = pydantic.Field(
        alias="first_cost_basis_date", default=None
    )
    first_funded_date: typing.Optional[str] = pydantic.Field(
        alias="first_funded_date", default=None
    )
    first_papered_date: typing.Optional[str] = pydantic.Field(
        alias="first_papered_date", default=None
    )
    first_performance_date: typing.Optional[str] = pydantic.Field(
        alias="first_performance_date", default=None
    )
    first_positions_date: typing.Optional[str] = pydantic.Field(
        alias="first_positions_date", default=None
    )
    first_quarantine_date: typing.Optional[str] = pydantic.Field(
        alias="first_quarantine_date", default=None
    )
    first_transactions_date: typing.Optional[str] = pydantic.Field(
        alias="first_transactions_date", default=None
    )
    has_custodian_name: typing.Optional[bool] = pydantic.Field(
        alias="has_custodian_name", default=None
    )
    household_id: typing.Optional[int] = pydantic.Field(
        alias="household_id", default=None
    )
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    inception_date: typing.Optional[str] = pydantic.Field(
        alias="inception_date", default=None
    )
    investment_model_id: typing.Optional[int] = pydantic.Field(
        alias="investment_model_id", default=None
    )
    is_account: typing.Optional[bool] = pydantic.Field(alias="is_account", default=None)
    is_active: typing.Optional[bool] = pydantic.Field(alias="is_active", default=None)
    is_closed: typing.Optional[bool] = pydantic.Field(alias="is_closed", default=None)
    is_custodian_billed: typing.Optional[bool] = pydantic.Field(
        alias="is_custodian_billed", default=None
    )
    is_direct_billed: typing.Optional[bool] = pydantic.Field(
        alias="is_direct_billed", default=None
    )
    is_household: typing.Optional[bool] = pydantic.Field(
        alias="is_household", default=None
    )
    is_tax_deferred: typing.Optional[bool] = pydantic.Field(
        alias="is_tax_deferred", default=None
    )
    is_taxable: typing.Optional[bool] = pydantic.Field(alias="is_taxable", default=None)
    last_cost_basis_date: typing.Optional[str] = pydantic.Field(
        alias="last_cost_basis_date", default=None
    )
    last_portfolio_data_date: typing.Optional[str] = pydantic.Field(
        alias="last_portfolio_data_date", default=None
    )
    last_positions_date: typing.Optional[str] = pydantic.Field(
        alias="last_positions_date", default=None
    )
    last_reporting_date: typing.Optional[str] = pydantic.Field(
        alias="last_reporting_date", default=None
    )
    last_transactions_date: typing.Optional[str] = pydantic.Field(
        alias="last_transactions_date", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    notes: typing.Optional[str] = pydantic.Field(alias="notes", default=None)
    number: typing.Optional[str] = pydantic.Field(alias="number", default=None)
    payment_source: typing.Optional[typing_extensions.Literal["D", "C"]] = (
        pydantic.Field(alias="payment_source", default=None)
    )
    required_cash: typing.Optional[float] = pydantic.Field(
        alias="required_cash", default=None
    )
    required_cash_frequency: typing.Optional[
        typing_extensions.Literal["O", "M", "Q"]
    ] = pydantic.Field(alias="required_cash_frequency", default=None)
    sell_securities_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="sell_securities_ids", default=None
    )
    short_name: typing.Optional[str] = pydantic.Field(alias="short_name", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    status: typing.Optional[
        typing_extensions.Literal["funded", "papered", "closed", "stale"]
    ] = pydantic.Field(alias="status", default=None)
    target_allocation_id: typing.Optional[int] = pydantic.Field(
        alias="target_allocation_id", default=None
    )
    tax_id_token: typing.Optional[str] = pydantic.Field(
        alias="tax_id_token", default=None
    )
    unsupervised_securities_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="unsupervised_securities_ids", default=None
    )
    updated_at_utc: typing.Optional[str] = pydantic.Field(
        alias="updated_at_utc", default=None
    )
    zip_code: typing.Optional[str] = pydantic.Field(alias="zip_code", default=None)


class PostAccountManagementAccountsFilterResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_page: typing.Optional[int] = pydantic.Field(
        alias="current_page", default=None
    )
    data: typing.Optional[typing.List[Account]] = pydantic.Field(
        alias="data", default=None
    )
    has_next: typing.Optional[bool] = pydantic.Field(alias="has_next", default=None)
    has_previous: typing.Optional[bool] = pydantic.Field(
        alias="has_previous", default=None
    )
    object: typing.Optional[str] = pydantic.Field(alias="object", default=None)
    page_size_limit: typing.Optional[int] = pydantic.Field(
        alias="page_size_limit", default=None
    )
    total_items: typing.Optional[int] = pydantic.Field(
        alias="total_items", default=None
    )
    total_pages: typing.Optional[int] = pydantic.Field(
        alias="total_pages", default=None
    )
