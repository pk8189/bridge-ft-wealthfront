"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostBillingReportsBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    billing_date: typing_extensions.NotRequired[str]
    create_invoices: typing_extensions.NotRequired[bool]
    email_notification: typing_extensions.NotRequired[bool]
    firm_id: typing_extensions.Required[int]
    group_ids: typing_extensions.NotRequired[typing.Optional[typing.List[int]]]
    is_invoice_by_client: typing_extensions.Required[bool]
    period_type: typing_extensions.Required[typing_extensions.Literal["E", "S"]]


class _SerializerPostBillingReportsBody(pydantic.BaseModel):
    """
    Serializer for PostBillingReportsBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    billing_date: typing.Optional[str] = pydantic.Field(
        alias="billing_date", default=None
    )
    create_invoices: typing.Optional[bool] = pydantic.Field(
        alias="create_invoices", default=None
    )
    email_notification: typing.Optional[bool] = pydantic.Field(
        alias="email_notification", default=None
    )
    firm_id: int = pydantic.Field(alias="firm_id")
    group_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="group_ids", default=None
    )
    is_invoice_by_client: bool = pydantic.Field(alias="is_invoice_by_client")
    period_type: typing_extensions.Literal["S", "E"] = pydantic.Field(
        alias="period_type"
    )
