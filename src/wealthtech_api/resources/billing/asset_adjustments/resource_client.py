"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    RequestOptions,
    QueryParams,
    encode_param,
    to_encodable,
    AsyncBaseClient,
    SyncBaseClient,
    default_request_options,
)
from wealthtech_api.resources.billing.asset_adjustments.create_many import (
    AsyncCreateManyClient,
    CreateManyClient,
)
from wealthtech_api.resources.billing.asset_adjustments.delete_many import (
    AsyncDeleteManyClient,
    DeleteManyClient,
)
from wealthtech_api.resources.billing.asset_adjustments.filter import (
    AsyncFilterClient,
    FilterClient,
)
import typing
from wealthtech_api.types.billing.asset_adjustments import params, models


class AssetAdjustmentsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.create_many = CreateManyClient(base_client=self._base_client)
        self.delete_many = DeleteManyClient(base_client=self._base_client)
        self.filter = FilterClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def put_by_id(
        self,
        *,
        data: params.AssetAdjustment,
        id: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PutBillingAssetAdjustmentsIdResponse:
        """
        Provide an asset adjustment to update. Then entire asset adjustment object **must** be provided to the `PUT` request.

        **Editable Fields:**
        - `name`
        - `adjustment_type`
        - `level`
        - `security_ids`
        - `weight`

        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerAssetAdjustment)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PUT",
            path=f"/billing/asset-adjustments/{id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PutBillingAssetAdjustmentsIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def put(
        self,
        *,
        data: typing.List[params.AssetAdjustment],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PutBillingAssetAdjustmentsResponse:
        """
        Provide a list of asset adjustments to update. Then entire asset adjustment object **must** be provided to the `PUT` request.

        **Editable Fields:**
        - `name`
        - `adjustment_type`
        - `level`
        - `security_ids`
        - `weight`

        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=typing.List[params._SerializerAssetAdjustment]
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PUT",
            path="/billing/asset-adjustments",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PutBillingAssetAdjustmentsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def create(
        self,
        *,
        data: params.PostBillingAssetAdjustmentsBody,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostBillingAssetAdjustmentsResponse:
        """
        Returns a created Asset Adjustment
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostBillingAssetAdjustmentsBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/billing/asset-adjustments",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.PostBillingAssetAdjustmentsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: int,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBillingAssetAdjustmentsIdResponse:
        """
        Returns an Asset Adjustment based on a single ID
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
            path=f"/billing/asset-adjustments/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetBillingAssetAdjustmentsIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBillingAssetAdjustmentsResponse:
        """
        Returns a list of Asset Adjustments within the data field
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
            path="/billing/asset-adjustments",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetBillingAssetAdjustmentsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def delete(
        self,
        *,
        id: int,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Delete:
        """
        Returns the "OK" message and a json object with the id  of item deleted, if deletion was successful
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
            method="DELETE",
            path=f"/billing/asset-adjustments/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Delete,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAssetAdjustmentsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.create_many = AsyncCreateManyClient(base_client=self._base_client)
        self.delete_many = AsyncDeleteManyClient(base_client=self._base_client)
        self.filter = AsyncFilterClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def put_by_id(
        self,
        *,
        data: params.AssetAdjustment,
        id: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PutBillingAssetAdjustmentsIdResponse:
        """
        Provide an asset adjustment to update. Then entire asset adjustment object **must** be provided to the `PUT` request.

        **Editable Fields:**
        - `name`
        - `adjustment_type`
        - `level`
        - `security_ids`
        - `weight`

        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerAssetAdjustment)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PUT",
            path=f"/billing/asset-adjustments/{id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PutBillingAssetAdjustmentsIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def put(
        self,
        *,
        data: typing.List[params.AssetAdjustment],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PutBillingAssetAdjustmentsResponse:
        """
        Provide a list of asset adjustments to update. Then entire asset adjustment object **must** be provided to the `PUT` request.

        **Editable Fields:**
        - `name`
        - `adjustment_type`
        - `level`
        - `security_ids`
        - `weight`

        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=typing.List[params._SerializerAssetAdjustment]
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PUT",
            path="/billing/asset-adjustments",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PutBillingAssetAdjustmentsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def create(
        self,
        *,
        data: params.PostBillingAssetAdjustmentsBody,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostBillingAssetAdjustmentsResponse:
        """
        Returns a created Asset Adjustment
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostBillingAssetAdjustmentsBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/billing/asset-adjustments",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.PostBillingAssetAdjustmentsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: int,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBillingAssetAdjustmentsIdResponse:
        """
        Returns an Asset Adjustment based on a single ID
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
            path=f"/billing/asset-adjustments/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetBillingAssetAdjustmentsIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBillingAssetAdjustmentsResponse:
        """
        Returns a list of Asset Adjustments within the data field
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
            path="/billing/asset-adjustments",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetBillingAssetAdjustmentsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def delete(
        self,
        *,
        id: int,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Delete:
        """
        Returns the "OK" message and a json object with the id  of item deleted, if deletion was successful
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
            method="DELETE",
            path=f"/billing/asset-adjustments/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Delete,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)