"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class Household(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    benchmarks_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="benchmarks_ids", default=None
    )
    close_date: typing.Optional[str] = pydantic.Field(alias="close_date", default=None)
    created_at_utc: typing.Optional[str] = pydantic.Field(
        alias="created_at_utc", default=None
    )
    entity_id: typing.Optional[str] = pydantic.Field(alias="entity_id", default=None)
    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    first_account_reporting_date: typing.Optional[str] = pydantic.Field(
        alias="first_account_reporting_date", default=None
    )
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    inception_date: typing.Optional[str] = pydantic.Field(
        alias="inception_date", default=None
    )
    is_account: typing.Optional[bool] = pydantic.Field(alias="is_account", default=None)
    is_household: typing.Optional[bool] = pydantic.Field(
        alias="is_household", default=None
    )
    last_account_reporting_date: typing.Optional[str] = pydantic.Field(
        alias="last_account_reporting_date", default=None
    )
    last_reporting_date: typing.Optional[str] = pydantic.Field(
        alias="last_reporting_date", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    opening_date: typing.Optional[str] = pydantic.Field(
        alias="opening_date", default=None
    )
    short_name: typing.Optional[str] = pydantic.Field(alias="short_name", default=None)
    status: typing.Optional[str] = pydantic.Field(alias="status", default=None)
    updated_at_utc: typing.Optional[str] = pydantic.Field(
        alias="updated_at_utc", default=None
    )


class GetReportingHouseholdsIdResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_page: typing.Optional[int] = pydantic.Field(
        alias="current_page", default=None
    )
    data: typing.Optional[Household] = pydantic.Field(alias="data", default=None)
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


class PostReportingHouseholdsResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_page: typing.Optional[int] = pydantic.Field(
        alias="current_page", default=None
    )
    data: typing.Optional[Household] = pydantic.Field(alias="data", default=None)
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


class PutReportingHouseholdsResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_page: typing.Optional[int] = pydantic.Field(
        alias="current_page", default=None
    )
    data: typing.Optional[typing.List[Household]] = pydantic.Field(
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


class PutReportingHouseholdsIdResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_page: typing.Optional[int] = pydantic.Field(
        alias="current_page", default=None
    )
    data: typing.Optional[Household] = pydantic.Field(alias="data", default=None)
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


class GetReportingHouseholdsResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_page: typing.Optional[int] = pydantic.Field(
        alias="current_page", default=None
    )
    data: typing.Optional[typing.List[Household]] = pydantic.Field(
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
