"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    RequestOptions,
    AsyncBaseClient,
    default_request_options,
    encode_param,
    SyncBaseClient,
    QueryParams,
)
from wealthtech_api.resources.data.source.lots.latest import (
    LatestClient,
    AsyncLatestClient,
)
from wealthtech_api.resources.data.source.lots.filter import (
    AsyncFilterClient,
    FilterClient,
)
import typing
from wealthtech_api.types.data.source.lots import models


class LotsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.latest = LatestClient(base_client=self._base_client)
        self.filter = FilterClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def get(
        self,
        *,
        id: int,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetDataSourceLotsIdResponse:
        """
        Returns a lot record based on its ID
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
            path=f"/data/source/lots/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetDataSourceLotsIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        reported_date: str,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        related: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetDataSourceLotsResponse:
        """
        Returns a list of lots
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["reported_date"] = encode_param(reported_date, False)
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        if related is not None:
            _query["related"] = encode_param(related, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path="/data/source/lots",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetDataSourceLotsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncLotsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.latest = AsyncLatestClient(base_client=self._base_client)
        self.filter = AsyncFilterClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def get(
        self,
        *,
        id: int,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetDataSourceLotsIdResponse:
        """
        Returns a lot record based on its ID
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
            path=f"/data/source/lots/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetDataSourceLotsIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        reported_date: str,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        related: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetDataSourceLotsResponse:
        """
        Returns a list of lots
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["reported_date"] = encode_param(reported_date, False)
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        if related is not None:
            _query["related"] = encode_param(related, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path="/data/source/lots",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetDataSourceLotsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
