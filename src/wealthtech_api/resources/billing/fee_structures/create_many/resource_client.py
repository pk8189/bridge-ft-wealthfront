"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    SyncBaseClient,
    RequestOptions,
    encode_param,
    default_request_options,
    AsyncBaseClient,
    to_encodable,
    QueryParams,
)
import typing
from wealthtech_api.types.billing.fee_structures.create_many import params, models


class CreateManyClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: typing.List[params.PostBillingFeeStructuresCreateManyBodyItem],
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostBillingFeeStructuresCreateManyResponse:
        """
        Returns a list of created Fee Structures
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        _json = to_encodable(
            item=data,
            dump_with=typing.List[
                params._SerializerPostBillingFeeStructuresCreateManyBodyItem
            ],
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/billing/fee-structures/create-many",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.PostBillingFeeStructuresCreateManyResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncCreateManyClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: typing.List[params.PostBillingFeeStructuresCreateManyBodyItem],
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostBillingFeeStructuresCreateManyResponse:
        """
        Returns a list of created Fee Structures
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        _json = to_encodable(
            item=data,
            dump_with=typing.List[
                params._SerializerPostBillingFeeStructuresCreateManyBodyItem
            ],
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/billing/fee-structures/create-many",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.PostBillingFeeStructuresCreateManyResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)