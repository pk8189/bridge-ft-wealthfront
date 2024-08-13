"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostAccountManagementAccountsFilterBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    acct_type: typing_extensions.NotRequired[str]
    advisor_code: typing_extensions.NotRequired[str]
    city: typing_extensions.NotRequired[str]
    close_date: typing_extensions.NotRequired[typing.Optional[str]]
    custodian: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "NFS", "SWB", "IBK", "PER", "EGB", "FPR", "DST", "MLT", "TIA", "APX"
        ]
    ]
    firm_id: typing_extensions.NotRequired[int]
    household_id: typing_extensions.NotRequired[int]
    id: typing_extensions.NotRequired[int]
    inception_date: typing_extensions.NotRequired[typing.Optional[str]]
    is_tax_deferred: typing_extensions.NotRequired[typing.Optional[bool]]
    is_taxable: typing_extensions.NotRequired[typing.Optional[bool]]
    name: typing_extensions.NotRequired[str]
    number: typing_extensions.NotRequired[str]
    payment_source: typing_extensions.NotRequired[typing_extensions.Literal["D", "C"]]
    status: typing_extensions.NotRequired[
        typing_extensions.Literal["funded", "papered", "stale", "closed"]
    ]
    zip_code: typing_extensions.NotRequired[str]


class _SerializerPostAccountManagementAccountsFilterBody(pydantic.BaseModel):
    """
    Serializer for PostAccountManagementAccountsFilterBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acct_type: typing.Optional[str] = pydantic.Field(alias="acct_type", default=None)
    advisor_code: typing.Optional[str] = pydantic.Field(
        alias="advisor_code", default=None
    )
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    close_date: typing.Optional[str] = pydantic.Field(alias="close_date", default=None)
    custodian: typing.Optional[
        typing_extensions.Literal[
            "FPR", "IBK", "NFS", "PER", "APX", "EGB", "MLT", "TIA", "SWB", "DST"
        ]
    ] = pydantic.Field(alias="custodian", default=None)
    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    household_id: typing.Optional[int] = pydantic.Field(
        alias="household_id", default=None
    )
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    inception_date: typing.Optional[str] = pydantic.Field(
        alias="inception_date", default=None
    )
    is_tax_deferred: typing.Optional[bool] = pydantic.Field(
        alias="is_tax_deferred", default=None
    )
    is_taxable: typing.Optional[bool] = pydantic.Field(alias="is_taxable", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    number: typing.Optional[str] = pydantic.Field(alias="number", default=None)
    payment_source: typing.Optional[typing_extensions.Literal["C", "D"]] = (
        pydantic.Field(alias="payment_source", default=None)
    )
    status: typing.Optional[
        typing_extensions.Literal["funded", "papered", "closed", "stale"]
    ] = pydantic.Field(alias="status", default=None)
    zip_code: typing.Optional[str] = pydantic.Field(alias="zip_code", default=None)