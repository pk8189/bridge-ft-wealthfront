"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class AssetClassification(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    class_tag_id: typing.Optional[int] = pydantic.Field(
        alias="class_tag_id", default=None
    )
    created_at_utc: typing.Optional[str] = pydantic.Field(
        alias="created_at_utc", default=None
    )
    created_by_user_id: typing.Optional[int] = pydantic.Field(
        alias="created_by_user_id", default=None
    )
    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    security_id: typing.Optional[int] = pydantic.Field(
        alias="security_id", default=None
    )
    updated_at_utc: typing.Optional[str] = pydantic.Field(
        alias="updated_at_utc", default=None
    )


class PostReportingAssetClassificationsFilterResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_page: typing.Optional[int] = pydantic.Field(
        alias="current_page", default=None
    )
    data: typing.Optional[typing.List[AssetClassification]] = pydantic.Field(
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
