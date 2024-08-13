"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    QueryParams,
    default_request_options,
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    encode_param,
)
import typing
from wealthtech_api.types.data.custodian.securities.get_usd import models


class GetUsdClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetDataCustodianSecuritiesGetUsdResponse:
        """
        Returns the first security object where the issue_type_code is 1
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path="/data/custodian/securities/get-usd",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetDataCustodianSecuritiesGetUsdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncGetUsdClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetDataCustodianSecuritiesGetUsdResponse:
        """
        Returns the first security object where the issue_type_code is 1
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path="/data/custodian/securities/get-usd",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetDataCustodianSecuritiesGetUsdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
