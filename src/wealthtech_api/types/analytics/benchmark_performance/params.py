"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostAnalyticsBenchmarkPerformanceBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    benchmarks_ids: typing_extensions.NotRequired[typing.List[int]]
    end_date: typing_extensions.Required[str]
    start_date: typing_extensions.Required[str]


class _SerializerPostAnalyticsBenchmarkPerformanceBody(pydantic.BaseModel):
    """
    Serializer for PostAnalyticsBenchmarkPerformanceBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    benchmarks_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="benchmarks_ids", default=None
    )
    end_date: str = pydantic.Field(alias="end_date")
    start_date: str = pydantic.Field(alias="start_date")
