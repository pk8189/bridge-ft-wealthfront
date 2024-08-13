"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    encode_param,
    default_request_options,
    QueryParams,
    to_encodable,
)
from wealthtech_api.types.reporting.asset_classifications.delete_many import (
    models,
    params,
)
import typing


class DeleteManyClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.PostReportingAssetClassificationsDeleteManyBody,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostReportingAssetClassificationsDeleteManyResponse:
        """
        Returns the "OK" message and a json object with the number of items deleted, if deletion was successful
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerPostReportingAssetClassificationsDeleteManyBody,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/reporting/asset-classifications/delete-many",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.PostReportingAssetClassificationsDeleteManyResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncDeleteManyClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.PostReportingAssetClassificationsDeleteManyBody,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostReportingAssetClassificationsDeleteManyResponse:
        """
        Returns the "OK" message and a json object with the number of items deleted, if deletion was successful
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerPostReportingAssetClassificationsDeleteManyBody,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/reporting/asset-classifications/delete-many",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.PostReportingAssetClassificationsDeleteManyResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
