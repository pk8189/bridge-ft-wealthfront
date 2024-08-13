"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    default_request_options,
    SyncBaseClient,
    encode_param,
    AsyncBaseClient,
    QueryParams,
    to_encodable,
    RequestOptions,
)
from wealthtech_api.types.data.source.transactions.filter import models, params
import typing


class FilterClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: typing.Optional[params.PostDataSourceTransactionsFilterBody] = None,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        related: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostDataSourceTransactionsFilterResponse:
        """
        Returns a filtered list of transaction records
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        if related is not None:
            _query["related"] = encode_param(related, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostDataSourceTransactionsFilterBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/data/source/transactions/filter",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.PostDataSourceTransactionsFilterResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncFilterClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: typing.Optional[params.PostDataSourceTransactionsFilterBody] = None,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        related: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostDataSourceTransactionsFilterResponse:
        """
        Returns a filtered list of transaction records
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        if related is not None:
            _query["related"] = encode_param(related, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostDataSourceTransactionsFilterBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/data/source/transactions/filter",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.PostDataSourceTransactionsFilterResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
