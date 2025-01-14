"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostReportingTargetAllocationsCreateManyBodyItemCoefficientsItem(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    class_tag_id: typing_extensions.NotRequired[typing.Optional[int]]
    mac: typing_extensions.NotRequired[str]
    negative_tolerance: typing_extensions.NotRequired[float]
    positive_tolerance: typing_extensions.NotRequired[float]
    weight: typing_extensions.NotRequired[float]


class _SerializerPostReportingTargetAllocationsCreateManyBodyItemCoefficientsItem(
    pydantic.BaseModel
):
    """
    Serializer for PostReportingTargetAllocationsCreateManyBodyItemCoefficientsItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    class_tag_id: typing.Optional[int] = pydantic.Field(
        alias="class_tag_id", default=None
    )
    mac: typing.Optional[str] = pydantic.Field(alias="mac", default=None)
    negative_tolerance: typing.Optional[float] = pydantic.Field(
        alias="negative_tolerance", default=None
    )
    positive_tolerance: typing.Optional[float] = pydantic.Field(
        alias="positive_tolerance", default=None
    )
    weight: typing.Optional[float] = pydantic.Field(alias="weight", default=None)


class PostReportingTargetAllocationsCreateManyBodyItem(typing_extensions.TypedDict):
    """
    No description specified
    """

    coefficients: typing_extensions.NotRequired[
        typing.List[PostReportingTargetAllocationsCreateManyBodyItemCoefficientsItem]
    ]
    firm_id: typing_extensions.NotRequired[int]
    name: typing_extensions.NotRequired[str]
    slug: typing_extensions.NotRequired[str]


class _SerializerPostReportingTargetAllocationsCreateManyBodyItem(pydantic.BaseModel):
    """
    Serializer for PostReportingTargetAllocationsCreateManyBodyItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    coefficients: typing.Optional[
        typing.List[
            _SerializerPostReportingTargetAllocationsCreateManyBodyItemCoefficientsItem
        ]
    ] = pydantic.Field(alias="coefficients", default=None)
    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)
