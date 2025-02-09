"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    AsyncBaseClient,
    encode_param,
    to_encodable,
    default_request_options,
    RequestOptions,
    QueryParams,
    SyncBaseClient,
)
from wealthtech_api.types.data.source.realized_gain_loss.latest import params, models
import typing


class LatestClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        data: typing.Optional[params.GetDataSourceRealizedGainLossLatestBody] = None,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetDataSourceRealizedGainLossLatestResponse:
        """
        Returns a list of the most recent realized gain loss records as of the latest date reported by the custodian. Request body fields can be included in request body, or as query parameters for optional filtering.
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGetDataSourceRealizedGainLossLatestBody,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path="/data/source/realized-gain-loss/latest",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.GetDataSourceRealizedGainLossLatestResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncLatestClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        data: typing.Optional[params.GetDataSourceRealizedGainLossLatestBody] = None,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetDataSourceRealizedGainLossLatestResponse:
        """
        Returns a list of the most recent realized gain loss records as of the latest date reported by the custodian. Request body fields can be included in request body, or as query parameters for optional filtering.
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGetDataSourceRealizedGainLossLatestBody,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path="/data/source/realized-gain-loss/latest",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.GetDataSourceRealizedGainLossLatestResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
