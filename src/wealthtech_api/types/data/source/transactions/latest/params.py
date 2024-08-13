"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class GetDataSourceTransactionsLatestBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    account_id: typing_extensions.NotRequired[int]
    account_ids: typing_extensions.NotRequired[typing.List[int]]
    account_number: typing_extensions.NotRequired[str]
    category: typing_extensions.NotRequired[
        typing_extensions.Literal["xfr", "oth", "inc", "trd", "crp"]
    ]
    classification: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "rec",
            "del",
            "jnl",
            "dep",
            "inc",
            "int",
            "oth",
            "exp",
            "dvr",
            "div",
            "chg",
            "stc",
            "spl",
            "btc",
            "mfe",
            "sto",
            "tax",
            "wth",
            "bto",
        ]
    ]
    feed_code: typing_extensions.NotRequired[str]
    id: typing_extensions.NotRequired[int]
    reported_date: typing_extensions.NotRequired[str]
    security_id: typing_extensions.NotRequired[int]
    source: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "FPR",
            "IBK",
            "EGB",
            "TDA (Available prior to Sept. 2, 2023)",
            "TIA",
            "PER",
            "MLT",
            "SWB",
            "APX",
            "NFS",
            "DST",
        ]
    ]
    source_security_cusip: typing_extensions.NotRequired[str]
    source_security_symbol: typing_extensions.NotRequired[str]
    source_transaction_code: typing_extensions.NotRequired[str]
    trade_settle_ind: typing_extensions.NotRequired[typing_extensions.Literal["S", "T"]]
    transaction_date: typing_extensions.NotRequired[str]


class _SerializerGetDataSourceTransactionsLatestBody(pydantic.BaseModel):
    """
    Serializer for GetDataSourceTransactionsLatestBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_id: typing.Optional[int] = pydantic.Field(alias="account_id", default=None)
    account_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="account_ids", default=None
    )
    account_number: typing.Optional[str] = pydantic.Field(
        alias="account_number", default=None
    )
    category: typing.Optional[
        typing_extensions.Literal["crp", "trd", "xfr", "inc", "oth"]
    ] = pydantic.Field(alias="category", default=None)
    classification: typing.Optional[
        typing_extensions.Literal[
            "chg",
            "sto",
            "stc",
            "inc",
            "dvr",
            "div",
            "oth",
            "dep",
            "btc",
            "bto",
            "exp",
            "int",
            "tax",
            "rec",
            "del",
            "wth",
            "spl",
            "jnl",
            "mfe",
        ]
    ] = pydantic.Field(alias="classification", default=None)
    feed_code: typing.Optional[str] = pydantic.Field(alias="feed_code", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    reported_date: typing.Optional[str] = pydantic.Field(
        alias="reported_date", default=None
    )
    security_id: typing.Optional[int] = pydantic.Field(
        alias="security_id", default=None
    )
    source: typing.Optional[
        typing_extensions.Literal[
            "DST",
            "NFS",
            "SWB",
            "FPR",
            "IBK",
            "PER",
            "EGB",
            "MLT",
            "TIA",
            "TDA (Available prior to Sept. 2, 2023)",
            "APX",
        ]
    ] = pydantic.Field(alias="source", default=None)
    source_security_cusip: typing.Optional[str] = pydantic.Field(
        alias="source_security_cusip", default=None
    )
    source_security_symbol: typing.Optional[str] = pydantic.Field(
        alias="source_security_symbol", default=None
    )
    source_transaction_code: typing.Optional[str] = pydantic.Field(
        alias="source_transaction_code", default=None
    )
    trade_settle_ind: typing.Optional[typing_extensions.Literal["T", "S"]] = (
        pydantic.Field(alias="trade_settle_ind", default=None)
    )
    transaction_date: typing.Optional[str] = pydantic.Field(
        alias="transaction_date", default=None
    )