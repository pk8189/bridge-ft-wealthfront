"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostBillingFeeStructuresBodyTiersItem(typing_extensions.TypedDict):
    """
    No description specified
    """

    fee_structure_id: typing_extensions.NotRequired[int]
    id: typing_extensions.NotRequired[int]
    max_balance: typing_extensions.NotRequired[typing.Optional[float]]
    min_balance: typing_extensions.NotRequired[float]
    rate: typing_extensions.NotRequired[float]


class _SerializerPostBillingFeeStructuresBodyTiersItem(pydantic.BaseModel):
    """
    Serializer for PostBillingFeeStructuresBodyTiersItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    fee_structure_id: typing.Optional[int] = pydantic.Field(
        alias="fee_structure_id", default=None
    )
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    max_balance: typing.Optional[float] = pydantic.Field(
        alias="max_balance", default=None
    )
    min_balance: typing.Optional[float] = pydantic.Field(
        alias="min_balance", default=None
    )
    rate: typing.Optional[float] = pydantic.Field(alias="rate", default=None)


class FeeStructureTiersItem(typing_extensions.TypedDict):
    """
    No description specified
    """

    fee_structure_id: typing_extensions.NotRequired[int]
    id: typing_extensions.NotRequired[int]
    max_balance: typing_extensions.NotRequired[float]
    min_balance: typing_extensions.NotRequired[float]
    rate: typing_extensions.NotRequired[float]


class _SerializerFeeStructureTiersItem(pydantic.BaseModel):
    """
    Serializer for FeeStructureTiersItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    fee_structure_id: typing.Optional[int] = pydantic.Field(
        alias="fee_structure_id", default=None
    )
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    max_balance: typing.Optional[float] = pydantic.Field(
        alias="max_balance", default=None
    )
    min_balance: typing.Optional[float] = pydantic.Field(
        alias="min_balance", default=None
    )
    rate: typing.Optional[float] = pydantic.Field(alias="rate", default=None)


class PostBillingFeeStructuresBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    balance_type: typing_extensions.NotRequired[
        typing_extensions.Literal["E", "P", "C", "A"]
    ]
    calculation_type: typing_extensions.NotRequired[str]
    collection_type: typing_extensions.NotRequired[
        typing_extensions.Literal["F", "D", "G", "A", "T", "R"]
    ]
    created_by_user_id: typing_extensions.NotRequired[typing.Optional[int]]
    firm_id: typing_extensions.NotRequired[int]
    flat_dollar_fee: typing_extensions.NotRequired[typing.Optional[float]]
    flat_rate: typing_extensions.NotRequired[float]
    frequency: typing_extensions.NotRequired[typing_extensions.Literal["M", "Q"]]
    name: typing_extensions.NotRequired[str]
    quarter_cycle: typing_extensions.NotRequired[int]
    slug: typing_extensions.NotRequired[str]
    tiers: typing_extensions.NotRequired[
        typing.List[PostBillingFeeStructuresBodyTiersItem]
    ]


class _SerializerPostBillingFeeStructuresBody(pydantic.BaseModel):
    """
    Serializer for PostBillingFeeStructuresBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    balance_type: typing.Optional[typing_extensions.Literal["P", "A", "E", "C"]] = (
        pydantic.Field(alias="balance_type", default=None)
    )
    calculation_type: typing.Optional[str] = pydantic.Field(
        alias="calculation_type", default=None
    )
    collection_type: typing.Optional[
        typing_extensions.Literal["A", "D", "R", "T", "F", "G"]
    ] = pydantic.Field(alias="collection_type", default=None)
    created_by_user_id: typing.Optional[int] = pydantic.Field(
        alias="created_by_user_id", default=None
    )
    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    flat_dollar_fee: typing.Optional[float] = pydantic.Field(
        alias="flat_dollar_fee", default=None
    )
    flat_rate: typing.Optional[float] = pydantic.Field(alias="flat_rate", default=None)
    frequency: typing.Optional[typing_extensions.Literal["M", "Q"]] = pydantic.Field(
        alias="frequency", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    quarter_cycle: typing.Optional[int] = pydantic.Field(
        alias="quarter_cycle", default=None
    )
    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)
    tiers: typing.Optional[
        typing.List[_SerializerPostBillingFeeStructuresBodyTiersItem]
    ] = pydantic.Field(alias="tiers", default=None)


class FeeStructure(typing_extensions.TypedDict):
    """
    No description specified
    """

    balance_type: typing_extensions.NotRequired[
        typing_extensions.Literal["A", "P", "E", "C"]
    ]
    calculation_type: typing_extensions.NotRequired[str]
    collection_type: typing_extensions.NotRequired[
        typing_extensions.Literal["R", "D", "A", "T", "G", "F"]
    ]
    created_at_utc: typing_extensions.NotRequired[str]
    created_by_user_id: typing_extensions.NotRequired[int]
    firm_id: typing_extensions.NotRequired[int]
    flat_dollar_fee: typing_extensions.NotRequired[float]
    flat_rate: typing_extensions.NotRequired[float]
    frequency: typing_extensions.NotRequired[typing_extensions.Literal["M", "Q"]]
    id: typing_extensions.NotRequired[int]
    name: typing_extensions.NotRequired[str]
    quarter_cycle: typing_extensions.NotRequired[int]
    slug: typing_extensions.NotRequired[str]
    tiers: typing_extensions.NotRequired[typing.List[FeeStructureTiersItem]]
    updated_at_utc: typing_extensions.NotRequired[str]


class _SerializerFeeStructure(pydantic.BaseModel):
    """
    Serializer for FeeStructure handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    balance_type: typing.Optional[typing_extensions.Literal["E", "A", "P", "C"]] = (
        pydantic.Field(alias="balance_type", default=None)
    )
    calculation_type: typing.Optional[str] = pydantic.Field(
        alias="calculation_type", default=None
    )
    collection_type: typing.Optional[
        typing_extensions.Literal["G", "R", "D", "T", "A", "F"]
    ] = pydantic.Field(alias="collection_type", default=None)
    created_at_utc: typing.Optional[str] = pydantic.Field(
        alias="created_at_utc", default=None
    )
    created_by_user_id: typing.Optional[int] = pydantic.Field(
        alias="created_by_user_id", default=None
    )
    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    flat_dollar_fee: typing.Optional[float] = pydantic.Field(
        alias="flat_dollar_fee", default=None
    )
    flat_rate: typing.Optional[float] = pydantic.Field(alias="flat_rate", default=None)
    frequency: typing.Optional[typing_extensions.Literal["M", "Q"]] = pydantic.Field(
        alias="frequency", default=None
    )
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    quarter_cycle: typing.Optional[int] = pydantic.Field(
        alias="quarter_cycle", default=None
    )
    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)
    tiers: typing.Optional[typing.List[_SerializerFeeStructureTiersItem]] = (
        pydantic.Field(alias="tiers", default=None)
    )
    updated_at_utc: typing.Optional[str] = pydantic.Field(
        alias="updated_at_utc", default=None
    )
