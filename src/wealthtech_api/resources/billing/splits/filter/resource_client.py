"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    RequestOptions,
    to_encodable,
    QueryParams,
    AsyncBaseClient,
    encode_param,
    default_request_options,
    SyncBaseClient,
)
from wealthtech_api.types.billing.splits.filter import models, params
import typing


class FilterClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: typing.Optional[params.PostBillingSplitsFilterBody] = None,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostBillingSplitsFilterResponse:
        """
        Returns a filtered list of Billing Splits
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostBillingSplitsFilterBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/billing/splits/filter",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.PostBillingSplitsFilterResponse,
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
        data: typing.Optional[params.PostBillingSplitsFilterBody] = None,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostBillingSplitsFilterResponse:
        """
        Returns a filtered list of Billing Splits
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostBillingSplitsFilterBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/billing/splits/filter",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.PostBillingSplitsFilterResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
