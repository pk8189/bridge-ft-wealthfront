"""File Generated by Sideko (sideko.dev)"""

import io
import typing

import typing_extensions
import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class RoiRequest(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    advisor_codes: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="advisor_codes", default=None
    )
    cc_emails: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="cc_emails", default=None
    )
    created_at_utc: typing.Optional[str] = pydantic.Field(
        alias="created_at_utc", default=None
    )
    custodian: typing.Optional[
        typing_extensions.Literal["IBK", "PER", "EGB", "MLT"]
    ] = pydantic.Field(alias="custodian", default=None)
    firm_name: typing.Optional[str] = pydantic.Field(alias="firm_name", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    owner_name: typing.Optional[str] = pydantic.Field(alias="owner_name", default=None)
    reply_to_emails: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="reply_to_emails", default=None
    )
    sender_name: typing.Optional[str] = pydantic.Field(
        alias="sender_name", default=None
    )
    status: typing.Optional[typing_extensions.Literal["Sent", "Error"]] = (
        pydantic.Field(alias="status", default=None)
    )
    updated_at_utc: typing.Optional[str] = pydantic.Field(
        alias="updated_at_utc", default=None
    )
