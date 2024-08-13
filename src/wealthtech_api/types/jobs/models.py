"""File Generated by Sideko (sideko.dev)"""

import io
import typing

import typing_extensions
import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class Job(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at_utc: typing.Optional[str] = pydantic.Field(
        alias="created_at_utc", default=None
    )
    created_by_id: typing.Optional[int] = pydantic.Field(
        alias="created_by_id", default=None
    )
    created_dt_utc: typing.Optional[str] = pydantic.Field(
        alias="created_dt_utc", default=None
    )
    current_step: typing.Optional[int] = pydantic.Field(
        alias="current_step", default=None
    )
    email_notification: typing.Optional[str] = pydantic.Field(
        alias="email_notification", default=None
    )
    email_notification_dt_utc: typing.Optional[str] = pydantic.Field(
        alias="email_notification_dt_utc", default=None
    )
    failed_dt_utc: typing.Optional[str] = pydantic.Field(
        alias="failed_dt_utc", default=None
    )
    finished_dt_utc: typing.Optional[str] = pydantic.Field(
        alias="finished_dt_utc", default=None
    )
    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    is_failed: typing.Optional[bool] = pydantic.Field(alias="is_failed", default=None)
    is_finished: typing.Optional[bool] = pydantic.Field(
        alias="is_finished", default=None
    )
    is_revoked: typing.Optional[bool] = pydantic.Field(alias="is_revoked", default=None)
    is_running: typing.Optional[bool] = pydantic.Field(alias="is_running", default=None)
    job_type: typing.Optional[typing_extensions.Literal["pdfrp", "db", "b"]] = (
        pydantic.Field(alias="job_type", default=None)
    )
    last_updated_dt_utc: typing.Optional[str] = pydantic.Field(
        alias="last_updated_dt_utc", default=None
    )
    num_steps: typing.Optional[int] = pydantic.Field(alias="num_steps", default=None)
    queued_dt_utc: typing.Optional[str] = pydantic.Field(
        alias="queued_dt_utc", default=None
    )
    started_dt_utc: typing.Optional[str] = pydantic.Field(
        alias="started_dt_utc", default=None
    )
    updated_at_utc: typing.Optional[str] = pydantic.Field(
        alias="updated_at_utc", default=None
    )


class GetJobsIdResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_page: typing.Optional[int] = pydantic.Field(
        alias="current_page", default=None
    )
    data: typing.Optional[Job] = pydantic.Field(alias="data", default=None)
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


class GetJobsResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_page: typing.Optional[int] = pydantic.Field(
        alias="current_page", default=None
    )
    data: typing.Optional[typing.List[Job]] = pydantic.Field(alias="data", default=None)
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
