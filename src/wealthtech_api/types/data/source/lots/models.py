"""File Generated by Sideko (sideko.dev)"""

import io
import typing

import typing_extensions
import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class SourceLot(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    abs_adjusted_cost_basis: typing.Optional[float] = pydantic.Field(
        alias="abs_adjusted_cost_basis", default=None
    )
    abs_cost_basis: typing.Optional[float] = pydantic.Field(
        alias="abs_cost_basis", default=None
    )
    abs_current_units: typing.Optional[float] = pydantic.Field(
        alias="abs_current_units", default=None
    )
    abs_current_value: typing.Optional[float] = pydantic.Field(
        alias="abs_current_value", default=None
    )
    abs_current_value_reported: typing.Optional[float] = pydantic.Field(
        alias="abs_current_value_reported", default=None
    )
    abs_current_value_unit_price: typing.Optional[float] = pydantic.Field(
        alias="abs_current_value_unit_price", default=None
    )
    abs_current_value_unit_price_reported: typing.Optional[float] = pydantic.Field(
        alias="abs_current_value_unit_price_reported", default=None
    )
    abs_original_open_units: typing.Optional[float] = pydantic.Field(
        alias="abs_original_open_units", default=None
    )
    account_id: typing.Optional[int] = pydantic.Field(alias="account_id", default=None)
    account_number: typing.Optional[str] = pydantic.Field(
        alias="account_number", default=None
    )
    certified: typing.Optional[bool] = pydantic.Field(alias="certified", default=None)
    cost_basis_fully_known: typing.Optional[bool] = pydantic.Field(
        alias="cost_basis_fully_known", default=None
    )
    cost_basis_fully_known_reported: typing.Optional[bool] = pydantic.Field(
        alias="cost_basis_fully_known_reported", default=None
    )
    created_at_utc: typing.Optional[str] = pydantic.Field(
        alias="created_at_utc", default=None
    )
    direction: typing.Optional[typing_extensions.Literal["S", "L"]] = pydantic.Field(
        alias="direction", default=None
    )
    disallowed_loss_amount: typing.Optional[float] = pydantic.Field(
        alias="disallowed_loss_amount", default=None
    )
    feed_code: typing.Optional[str] = pydantic.Field(alias="feed_code", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    lot_identifier: typing.Optional[str] = pydantic.Field(
        alias="lot_identifier", default=None
    )
    lot_selection_method: typing.Optional[str] = pydantic.Field(
        alias="lot_selection_method", default=None
    )
    original_data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="original_data", default=None
    )
    original_open_date: typing.Optional[str] = pydantic.Field(
        alias="original_open_date", default=None
    )
    realized_gain_loss_reported: typing.Optional[float] = pydantic.Field(
        alias="realized_gain_loss_reported", default=None
    )
    reported_date: typing.Optional[str] = pydantic.Field(
        alias="reported_date", default=None
    )
    security_id: typing.Optional[int] = pydantic.Field(
        alias="security_id", default=None
    )
    source: typing.Optional[
        typing_extensions.Literal[
            "DST",
            "TDA (Available prior to Sept. 2, 2023)",
            "EGB",
            "FPR",
            "APX",
            "NFS",
            "IBK",
            "PER",
            "SWB",
            "MLT",
            "TIA",
        ]
    ] = pydantic.Field(alias="source", default=None)
    source_security_cusip: typing.Optional[str] = pydantic.Field(
        alias="source_security_cusip", default=None
    )
    source_security_symbol: typing.Optional[str] = pydantic.Field(
        alias="source_security_symbol", default=None
    )
    unrealized_gain_loss: typing.Optional[float] = pydantic.Field(
        alias="unrealized_gain_loss", default=None
    )
    unrealized_gain_loss_reported: typing.Optional[float] = pydantic.Field(
        alias="unrealized_gain_loss_reported", default=None
    )
    wash_sale: typing.Optional[bool] = pydantic.Field(alias="wash_sale", default=None)


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
            "DST", "PER", "FPR", "IBK", "MLT", "APX", "TIA", "NFS", "EGB", "SWB"
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
        typing_extensions.Literal["M", "O", "Q"]
    ] = pydantic.Field(alias="required_cash_frequency", default=None)
    sell_securities_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="sell_securities_ids", default=None
    )
    short_name: typing.Optional[str] = pydantic.Field(alias="short_name", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    status: typing.Optional[
        typing_extensions.Literal["stale", "papered", "funded", "closed"]
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


class Security(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bond_rating: typing.Optional[str] = pydantic.Field(
        alias="bond_rating", default=None
    )
    broad_code: typing.Optional[str] = pydantic.Field(alias="broad_code", default=None)
    created_at_utc: typing.Optional[str] = pydantic.Field(
        alias="created_at_utc", default=None
    )
    cusip: typing.Optional[str] = pydantic.Field(alias="cusip", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    expiration_date: typing.Optional[str] = pydantic.Field(
        alias="expiration_date", default=None
    )
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    identifier: typing.Optional[str] = pydantic.Field(alias="identifier", default=None)
    issue_type: typing.Optional[str] = pydantic.Field(alias="issue_type", default=None)
    issue_type_code: typing.Optional[int] = pydantic.Field(
        alias="issue_type_code", default=None
    )
    master_asset_class: typing.Optional[
        typing_extensions.Literal["DT", "EQ", "MX", "UC", "CE", "CA", "CR", "ETF"]
    ] = pydantic.Field(alias="master_asset_class", default=None)
    maturity_date: typing.Optional[str] = pydantic.Field(
        alias="maturity_date", default=None
    )
    prefixed_identifier: typing.Optional[typing_extensions.Literal["C", "S"]] = (
        pydantic.Field(alias="prefixed_identifier", default=None)
    )
    security_type: typing.Optional[
        typing_extensions.Literal[
            "Crypto",
            "Unknown",
            "Mutual Fund",
            "ETF",
            "Bond",
            "Fund",
            "Alternative",
            "Stock",
            "Cash Equivalent",
            "Cash",
            "Option",
        ]
    ] = pydantic.Field(alias="security_type", default=None)
    sic_code: typing.Optional[str] = pydantic.Field(alias="sic_code", default=None)
    symbol_field: typing.Optional[str] = pydantic.Field(alias="symbol", default=None)
    updated_at_utc: typing.Optional[str] = pydantic.Field(
        alias="updated_at_utc", default=None
    )


class GetDataSourceLotsIdResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_page: typing.Optional[int] = pydantic.Field(
        alias="current_page", default=None
    )
    data: typing.Optional[SourceLot] = pydantic.Field(alias="data", default=None)
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


class GetDataSourceLotsResponseRelatedAccounts(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_id: typing.Optional[Account] = pydantic.Field(
        alias="account_id", default=None
    )


class GetDataSourceLotsResponseRelatedSecurities(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    security_id: typing.Optional[Security] = pydantic.Field(
        alias="security_id", default=None
    )


class GetDataSourceLotsResponseRelated(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    accounts: typing.Optional[GetDataSourceLotsResponseRelatedAccounts] = (
        pydantic.Field(alias="accounts", default=None)
    )
    securities: typing.Optional[GetDataSourceLotsResponseRelatedSecurities] = (
        pydantic.Field(alias="securities", default=None)
    )


class GetDataSourceLotsResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_page: typing.Optional[int] = pydantic.Field(
        alias="current_page", default=None
    )
    data: typing.Optional[typing.List[SourceLot]] = pydantic.Field(
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
    related: typing.Optional[GetDataSourceLotsResponseRelated] = pydantic.Field(
        alias="related", default=None
    )
    total_items: typing.Optional[int] = pydantic.Field(
        alias="total_items", default=None
    )
    total_pages: typing.Optional[int] = pydantic.Field(
        alias="total_pages", default=None
    )
