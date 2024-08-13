"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class GetDataSourceLotsLatestBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    abs_acquisition_quantity: typing_extensions.NotRequired[float]
    abs_adjusted_cost_basis: typing_extensions.NotRequired[float]
    abs_cost_basis: typing_extensions.NotRequired[float]
    abs_current_market_value: typing_extensions.NotRequired[float]
    abs_current_quantity: typing_extensions.NotRequired[float]
    account_id: typing_extensions.NotRequired[int]
    account_ids: typing_extensions.NotRequired[typing.List[int]]
    account_number: typing_extensions.NotRequired[str]
    acquisition_date: typing_extensions.NotRequired[str]
    advisor_code: typing_extensions.NotRequired[str]
    certified: typing_extensions.NotRequired[bool]
    created_at_utc: typing_extensions.NotRequired[str]
    direction: typing_extensions.NotRequired[typing_extensions.Literal["S", "L"]]
    disallowed_loss_amount: typing_extensions.NotRequired[bool]
    fully_known: typing_extensions.NotRequired[bool]
    id: typing_extensions.NotRequired[int]
    lot_identifier: typing_extensions.NotRequired[str]
    lot_selection_method: typing_extensions.NotRequired[str]
    reported_date: typing_extensions.NotRequired[str]
    security_id: typing_extensions.NotRequired[int]
    source: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "APX",
            "EGB",
            "PER",
            "NFS",
            "IBK",
            "SWB",
            "FPR",
            "DST",
            "TDA (Available prior to Sept. 2, 2023)",
            "TIA",
            "MLT",
        ]
    ]
    source_security_cusip: typing_extensions.NotRequired[str]
    source_security_symbol: typing_extensions.NotRequired[str]
    unrealized_gain_loss: typing_extensions.NotRequired[float]
    wash_sale: typing_extensions.NotRequired[bool]


class _SerializerGetDataSourceLotsLatestBody(pydantic.BaseModel):
    """
    Serializer for GetDataSourceLotsLatestBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    abs_acquisition_quantity: typing.Optional[float] = pydantic.Field(
        alias="abs_acquisition_quantity", default=None
    )
    abs_adjusted_cost_basis: typing.Optional[float] = pydantic.Field(
        alias="abs_adjusted_cost_basis", default=None
    )
    abs_cost_basis: typing.Optional[float] = pydantic.Field(
        alias="abs_cost_basis", default=None
    )
    abs_current_market_value: typing.Optional[float] = pydantic.Field(
        alias="abs_current_market_value", default=None
    )
    abs_current_quantity: typing.Optional[float] = pydantic.Field(
        alias="abs_current_quantity", default=None
    )
    account_id: typing.Optional[int] = pydantic.Field(alias="account_id", default=None)
    account_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="account_ids", default=None
    )
    account_number: typing.Optional[str] = pydantic.Field(
        alias="account_number", default=None
    )
    acquisition_date: typing.Optional[str] = pydantic.Field(
        alias="acquisition_date", default=None
    )
    advisor_code: typing.Optional[str] = pydantic.Field(
        alias="advisor_code", default=None
    )
    certified: typing.Optional[bool] = pydantic.Field(alias="certified", default=None)
    created_at_utc: typing.Optional[str] = pydantic.Field(
        alias="created_at_utc", default=None
    )
    direction: typing.Optional[typing_extensions.Literal["S", "L"]] = pydantic.Field(
        alias="direction", default=None
    )
    disallowed_loss_amount: typing.Optional[bool] = pydantic.Field(
        alias="disallowed_loss_amount", default=None
    )
    fully_known: typing.Optional[bool] = pydantic.Field(
        alias="fully_known", default=None
    )
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    lot_identifier: typing.Optional[str] = pydantic.Field(
        alias="lot_identifier", default=None
    )
    lot_selection_method: typing.Optional[str] = pydantic.Field(
        alias="lot_selection_method", default=None
    )
    reported_date: typing.Optional[str] = pydantic.Field(
        alias="reported_date", default=None
    )
    security_id: typing.Optional[int] = pydantic.Field(
        alias="security_id", default=None
    )
    source: typing.Optional[
        typing_extensions.Literal[
            "PER",
            "MLT",
            "DST",
            "TIA",
            "EGB",
            "IBK",
            "APX",
            "FPR",
            "NFS",
            "SWB",
            "TDA (Available prior to Sept. 2, 2023)",
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
    wash_sale: typing.Optional[bool] = pydantic.Field(alias="wash_sale", default=None)