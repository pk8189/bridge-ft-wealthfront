"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostReportingPrintableReportsCreateBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    account_ids: typing_extensions.NotRequired[typing.Optional[typing.List[int]]]
    end_date: typing_extensions.Required[str]
    exclude_portfolio_performance_summary: typing_extensions.NotRequired[bool]
    household_ids: typing_extensions.NotRequired[typing.Optional[typing.List[int]]]
    irr_performance: typing_extensions.NotRequired[bool]
    non_inception_performance_chart: typing_extensions.NotRequired[bool]
    portrait_pdf_orientation: typing_extensions.NotRequired[bool]
    start_date: typing_extensions.Required[str]
    sub_reports: typing_extensions.Required[typing.List[str]]


class _SerializerPostReportingPrintableReportsCreateBody(pydantic.BaseModel):
    """
    Serializer for PostReportingPrintableReportsCreateBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="account_ids", default=None
    )
    end_date: str = pydantic.Field(alias="end_date")
    exclude_portfolio_performance_summary: typing.Optional[bool] = pydantic.Field(
        alias="exclude_portfolio_performance_summary", default=None
    )
    household_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="household_ids", default=None
    )
    irr_performance: typing.Optional[bool] = pydantic.Field(
        alias="irr_performance", default=None
    )
    non_inception_performance_chart: typing.Optional[bool] = pydantic.Field(
        alias="non_inception_performance_chart", default=None
    )
    portrait_pdf_orientation: typing.Optional[bool] = pydantic.Field(
        alias="portrait_pdf_orientation", default=None
    )
    start_date: str = pydantic.Field(alias="start_date")
    sub_reports: typing.List[str] = pydantic.Field(alias="sub_reports")