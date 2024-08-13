"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    RequestOptions,
    default_request_options,
    SyncBaseClient,
    AsyncBaseClient,
    to_encodable,
)
from wealthtech_api.types.analytics.account_performance import models, params
import typing


class AccountPerformanceClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: typing.Optional[params.PostAnalyticsAccountPerformanceBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.PostAnalyticsAccountPerformanceResponseItem]:
        """
        Fetch Account Performance for a list of Account IDs
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostAnalyticsAccountPerformanceBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/analytics/account-performance",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=typing.List[models.PostAnalyticsAccountPerformanceResponseItem],
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAccountPerformanceClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: typing.Optional[params.PostAnalyticsAccountPerformanceBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.PostAnalyticsAccountPerformanceResponseItem]:
        """
        Fetch Account Performance for a list of Account IDs
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostAnalyticsAccountPerformanceBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/analytics/account-performance",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=typing.List[models.PostAnalyticsAccountPerformanceResponseItem],
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)