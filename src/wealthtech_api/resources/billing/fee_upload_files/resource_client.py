"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    AsyncBaseClient,
    QueryParams,
    default_request_options,
    RequestOptions,
    SyncBaseClient,
    encode_param,
)
from wealthtech_api.resources.billing.fee_upload_files.download import (
    AsyncDownloadClient,
    DownloadClient,
)
from wealthtech_api.resources.billing.fee_upload_files.filter import (
    FilterClient,
    AsyncFilterClient,
)
import typing
from wealthtech_api.types.billing.fee_upload_files import models


class FeeUploadFilesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.download = DownloadClient(base_client=self._base_client)
        self.filter = FilterClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def get(
        self,
        *,
        id: int,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBillingFeeUploadFilesIdResponse:
        """
        Returns the fee upload file record for the provided ID.
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
            path=f"/billing/fee-upload-files/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetBillingFeeUploadFilesIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBillingFeeUploadFilesResponse:
        """
        Return an enveloped list of fee upload files generated by your application.
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
            path="/billing/fee-upload-files",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetBillingFeeUploadFilesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncFeeUploadFilesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.download = AsyncDownloadClient(base_client=self._base_client)
        self.filter = AsyncFilterClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def get(
        self,
        *,
        id: int,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBillingFeeUploadFilesIdResponse:
        """
        Returns the fee upload file record for the provided ID.
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
            path=f"/billing/fee-upload-files/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetBillingFeeUploadFilesIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBillingFeeUploadFilesResponse:
        """
        Return an enveloped list of fee upload files generated by your application.
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
            path="/billing/fee-upload-files",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetBillingFeeUploadFilesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
