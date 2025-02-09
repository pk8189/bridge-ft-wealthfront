"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostInvestmentManagementStrategiesCreateManyBodyItemSecurityAllocationsItem(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    security_id: typing_extensions.NotRequired[int]
    weight: typing_extensions.NotRequired[float]


class _SerializerPostInvestmentManagementStrategiesCreateManyBodyItemSecurityAllocationsItem(
    pydantic.BaseModel
):
    """
    Serializer for PostInvestmentManagementStrategiesCreateManyBodyItemSecurityAllocationsItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    security_id: typing.Optional[int] = pydantic.Field(
        alias="security_id", default=None
    )
    weight: typing.Optional[float] = pydantic.Field(alias="weight", default=None)


class PostInvestmentManagementStrategiesCreateManyBodyItem(typing_extensions.TypedDict):
    """
    No description specified
    """

    firm_id: typing_extensions.NotRequired[int]
    name: typing_extensions.NotRequired[str]
    security_allocations: typing_extensions.NotRequired[
        typing.List[
            PostInvestmentManagementStrategiesCreateManyBodyItemSecurityAllocationsItem
        ]
    ]


class _SerializerPostInvestmentManagementStrategiesCreateManyBodyItem(
    pydantic.BaseModel
):
    """
    Serializer for PostInvestmentManagementStrategiesCreateManyBodyItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    security_allocations: typing.Optional[
        typing.List[
            _SerializerPostInvestmentManagementStrategiesCreateManyBodyItemSecurityAllocationsItem
        ]
    ] = pydantic.Field(alias="security_allocations", default=None)
