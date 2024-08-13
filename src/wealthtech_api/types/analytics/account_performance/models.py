"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class PostAnalyticsAccountPerformanceResponseItemFive(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_balance: typing.Optional[float] = pydantic.Field(
        alias="current_balance", default=None
    )
    entity_id: typing.Optional[int] = pydantic.Field(alias="entity_id", default=None)
    net_return: typing.Optional[float] = pydantic.Field(
        alias="net_return", default=None
    )


class PostAnalyticsAccountPerformanceResponseItemItd(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_balance: typing.Optional[float] = pydantic.Field(
        alias="current_balance", default=None
    )
    entity_id: typing.Optional[int] = pydantic.Field(alias="entity_id", default=None)
    net_return: typing.Optional[float] = pydantic.Field(
        alias="net_return", default=None
    )


class PostAnalyticsAccountPerformanceResponseItemItda(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_balance: typing.Optional[float] = pydantic.Field(
        alias="current_balance", default=None
    )
    entity_id: typing.Optional[int] = pydantic.Field(alias="entity_id", default=None)
    net_return: typing.Optional[float] = pydantic.Field(
        alias="net_return", default=None
    )


class PostAnalyticsAccountPerformanceResponseItemMtd(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_balance: typing.Optional[float] = pydantic.Field(
        alias="current_balance", default=None
    )
    entity_id: typing.Optional[int] = pydantic.Field(alias="entity_id", default=None)
    net_return: typing.Optional[float] = pydantic.Field(
        alias="net_return", default=None
    )


class PostAnalyticsAccountPerformanceResponseItemOne(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_balance: typing.Optional[float] = pydantic.Field(
        alias="current_balance", default=None
    )
    entity_id: typing.Optional[int] = pydantic.Field(alias="entity_id", default=None)
    net_return: typing.Optional[float] = pydantic.Field(
        alias="net_return", default=None
    )


class PostAnalyticsAccountPerformanceResponseItemQtd(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_balance: typing.Optional[float] = pydantic.Field(
        alias="current_balance", default=None
    )
    entity_id: typing.Optional[int] = pydantic.Field(alias="entity_id", default=None)
    net_return: typing.Optional[float] = pydantic.Field(
        alias="net_return", default=None
    )


class PostAnalyticsAccountPerformanceResponseItemThree(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_balance: typing.Optional[float] = pydantic.Field(
        alias="current_balance", default=None
    )
    entity_id: typing.Optional[int] = pydantic.Field(alias="entity_id", default=None)
    net_return: typing.Optional[float] = pydantic.Field(
        alias="net_return", default=None
    )


class PostAnalyticsAccountPerformanceResponseItemYtd(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_balance: typing.Optional[float] = pydantic.Field(
        alias="current_balance", default=None
    )
    entity_id: typing.Optional[int] = pydantic.Field(alias="entity_id", default=None)
    net_return: typing.Optional[float] = pydantic.Field(
        alias="net_return", default=None
    )


class PostAnalyticsAccountPerformanceResponseItem(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    five: typing.Optional[PostAnalyticsAccountPerformanceResponseItemFive] = (
        pydantic.Field(alias="five", default=None)
    )
    itd: typing.Optional[PostAnalyticsAccountPerformanceResponseItemItd] = (
        pydantic.Field(alias="itd", default=None)
    )
    itda: typing.Optional[PostAnalyticsAccountPerformanceResponseItemItda] = (
        pydantic.Field(alias="itda", default=None)
    )
    mtd: typing.Optional[PostAnalyticsAccountPerformanceResponseItemMtd] = (
        pydantic.Field(alias="mtd", default=None)
    )
    one: typing.Optional[PostAnalyticsAccountPerformanceResponseItemOne] = (
        pydantic.Field(alias="one", default=None)
    )
    qtd: typing.Optional[PostAnalyticsAccountPerformanceResponseItemQtd] = (
        pydantic.Field(alias="qtd", default=None)
    )
    three: typing.Optional[PostAnalyticsAccountPerformanceResponseItemThree] = (
        pydantic.Field(alias="three", default=None)
    )
    ytd: typing.Optional[PostAnalyticsAccountPerformanceResponseItemYtd] = (
        pydantic.Field(alias="ytd", default=None)
    )
