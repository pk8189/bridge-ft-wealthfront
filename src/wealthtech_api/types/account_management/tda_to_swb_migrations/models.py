"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class GetAccountManagementTdaToSwbMigrationsResponseDataItem(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_id: typing.Optional[int] = pydantic.Field(alias="account_id", default=None)
    schwab_account_number: typing.Optional[str] = pydantic.Field(
        alias="schwab_account_number", default=None
    )
    schwab_master_number: typing.Optional[str] = pydantic.Field(
        alias="schwab_master_number", default=None
    )
    tda_account_number: typing.Optional[str] = pydantic.Field(
        alias="tda_account_number", default=None
    )
    tda_rep_code: typing.Optional[str] = pydantic.Field(
        alias="tda_rep_code", default=None
    )


class GetAccountManagementTdaToSwbMigrationsResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_page: typing.Optional[int] = pydantic.Field(
        alias="current_page", default=None
    )
    data: typing.Optional[
        typing.List[GetAccountManagementTdaToSwbMigrationsResponseDataItem]
    ] = pydantic.Field(alias="data", default=None)
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
