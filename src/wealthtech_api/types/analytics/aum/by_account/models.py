"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class PostAnalyticsAumByAccountResponseValuesItem(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_id: typing.Optional[int] = pydantic.Field(alias="account_id", default=None)
    aum: typing.Optional[float] = pydantic.Field(alias="aum", default=None)


class PostAnalyticsAumByAccountResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    as_of_date: typing.Optional[str] = pydantic.Field(alias="as_of_date", default=None)
    total_aum: typing.Optional[float] = pydantic.Field(alias="total_aum", default=None)
    values: typing.Optional[
        typing.List[PostAnalyticsAumByAccountResponseValuesItem]
    ] = pydantic.Field(alias="values", default=None)
