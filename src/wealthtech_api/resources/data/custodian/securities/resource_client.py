"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    QueryParams,
    default_request_options,
    encode_param,
    SyncBaseClient,
    RequestOptions,
    AsyncBaseClient,
)
from wealthtech_api.resources.data.custodian.securities.get_compressed import (
    AsyncGetCompressedClient,
    GetCompressedClient,
)
from wealthtech_api.resources.data.custodian.securities.get_usd import (
    GetUsdClient,
    AsyncGetUsdClient,
)
from wealthtech_api.resources.data.custodian.securities.managed import (
    AsyncManagedClient,
    ManagedClient,
)
from wealthtech_api.resources.data.custodian.securities.search import (
    SearchClient,
    AsyncSearchClient,
)
from wealthtech_api.resources.data.custodian.securities.fetch import (
    FetchClient,
    AsyncFetchClient,
)
from wealthtech_api.resources.data.custodian.securities.filter import (
    AsyncFilterClient,
    FilterClient,
)
from wealthtech_api.resources.data.custodian.securities.reference import (
    ReferenceClient,
    AsyncReferenceClient,
)
import typing
from wealthtech_api.types.data.custodian.securities import models


class SecuritiesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.get_compressed = GetCompressedClient(base_client=self._base_client)
        self.get_usd = GetUsdClient(base_client=self._base_client)
        self.managed = ManagedClient(base_client=self._base_client)
        self.search = SearchClient(base_client=self._base_client)
        self.fetch = FetchClient(base_client=self._base_client)
        self.filter = FilterClient(base_client=self._base_client)
        self.reference = ReferenceClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def get(
        self,
        *,
        id: int,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetDataCustodianSecuritiesIdResponse:
        """
        Returns a single  security based on an ID
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
            path=f"/data/custodian/securities/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetDataCustodianSecuritiesIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetDataCustodianSecuritiesResponse:
        """
        Returns a list of securities
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
            path="/data/custodian/securities",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetDataCustodianSecuritiesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncSecuritiesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.get_compressed = AsyncGetCompressedClient(base_client=self._base_client)
        self.get_usd = AsyncGetUsdClient(base_client=self._base_client)
        self.managed = AsyncManagedClient(base_client=self._base_client)
        self.search = AsyncSearchClient(base_client=self._base_client)
        self.fetch = AsyncFetchClient(base_client=self._base_client)
        self.filter = AsyncFilterClient(base_client=self._base_client)
        self.reference = AsyncReferenceClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def get(
        self,
        *,
        id: int,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetDataCustodianSecuritiesIdResponse:
        """
        Returns a single  security based on an ID
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
            path=f"/data/custodian/securities/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetDataCustodianSecuritiesIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetDataCustodianSecuritiesResponse:
        """
        Returns a list of securities
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
            path="/data/custodian/securities",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetDataCustodianSecuritiesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)