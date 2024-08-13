"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    default_request_options,
    encode_param,
    RequestOptions,
    SyncBaseClient,
    AsyncBaseClient,
    QueryParams,
)
from wealthtech_api.resources.account_management.tda_to_swb_migrations.filter import (
    AsyncFilterClient,
    FilterClient,
)
import typing
from wealthtech_api.types.account_management.tda_to_swb_migrations import models


class TdaToSwbMigrationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.filter = FilterClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetAccountManagementTdaToSwbMigrationsResponse:
        """
        Retrieve the list of all your TDA Accounts which are subjected to be migrated to Schwab.
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
            path="/account-management/tda-to-swb-migrations",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetAccountManagementTdaToSwbMigrationsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncTdaToSwbMigrationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.filter = AsyncFilterClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetAccountManagementTdaToSwbMigrationsResponse:
        """
        Retrieve the list of all your TDA Accounts which are subjected to be migrated to Schwab.
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
            path="/account-management/tda-to-swb-migrations",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetAccountManagementTdaToSwbMigrationsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)