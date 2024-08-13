"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostReportingBenchmarksBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    firm_id: typing_extensions.NotRequired[int]
    name: typing_extensions.NotRequired[str]
    slug: typing_extensions.NotRequired[str]


class _SerializerPostReportingBenchmarksBody(pydantic.BaseModel):
    """
    Serializer for PostReportingBenchmarksBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)


class BenchmarkCoefficients(typing_extensions.TypedDict):
    """
    Coefficients associated with this benchmark
    """

    benchmark_id: typing_extensions.NotRequired[int]
    id: typing_extensions.NotRequired[int]
    index_id: typing_extensions.NotRequired[int]
    weight: typing_extensions.NotRequired[str]


class _SerializerBenchmarkCoefficients(pydantic.BaseModel):
    """
    Serializer for BenchmarkCoefficients handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    benchmark_id: typing.Optional[int] = pydantic.Field(
        alias="benchmark_id", default=None
    )
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    index_id: typing.Optional[int] = pydantic.Field(alias="index_id", default=None)
    weight: typing.Optional[str] = pydantic.Field(alias="weight", default=None)


class Benchmark(typing_extensions.TypedDict):
    """
    No description specified
    """

    coefficients: typing_extensions.NotRequired[BenchmarkCoefficients]
    created_at_utc: typing_extensions.NotRequired[str]
    firm_id: typing_extensions.NotRequired[int]
    id: typing_extensions.NotRequired[int]
    name: typing_extensions.NotRequired[str]
    slug: typing_extensions.NotRequired[str]
    updated_at_utc: typing_extensions.NotRequired[str]


class _SerializerBenchmark(pydantic.BaseModel):
    """
    Serializer for Benchmark handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    coefficients: typing.Optional[_SerializerBenchmarkCoefficients] = pydantic.Field(
        alias="coefficients", default=None
    )
    created_at_utc: typing.Optional[str] = pydantic.Field(
        alias="created_at_utc", default=None
    )
    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)
    updated_at_utc: typing.Optional[str] = pydantic.Field(
        alias="updated_at_utc", default=None
    )
