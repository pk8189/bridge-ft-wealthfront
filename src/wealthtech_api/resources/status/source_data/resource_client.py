"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    default_request_options,
    to_encodable,
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
)
from wealthtech_api.types.status.source_data import models, params
import typing


class SourceDataClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: typing.Optional[params.PostStatusSourceDataBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostStatusSourceDataResponse:
        """
        Status of source data ingestion. TDA availability status is applicable prior to Sept. 2, 2023.
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostStatusSourceDataBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/status/source-data",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostStatusSourceDataResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncSourceDataClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: typing.Optional[params.PostStatusSourceDataBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostStatusSourceDataResponse:
        """
        Status of source data ingestion. TDA availability status is applicable prior to Sept. 2, 2023.
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostStatusSourceDataBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/status/source-data",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostStatusSourceDataResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
