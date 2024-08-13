"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    SyncBaseClient,
    encode_param,
    QueryParams,
    default_request_options,
    AsyncBaseClient,
    RequestOptions,
)
from wealthtech_api.resources.reporting.printable_reports.create import (
    AsyncCreateClient,
    CreateClient,
)
from wealthtech_api.resources.reporting.printable_reports.delete_many import (
    AsyncDeleteManyClient,
    DeleteManyClient,
)
from wealthtech_api.resources.reporting.printable_reports.download import (
    DownloadClient,
    AsyncDownloadClient,
)
from wealthtech_api.resources.reporting.printable_reports.filter import (
    FilterClient,
    AsyncFilterClient,
)
import typing
from wealthtech_api.types.reporting.printable_reports import models


class PrintableReportsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.create = CreateClient(base_client=self._base_client)
        self.delete_many = DeleteManyClient(base_client=self._base_client)
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
    ) -> models.GetReportingPrintableReportsIdResponse:
        """
        Returns a Printable Report based on a single ID
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
            path=f"/reporting/printable-reports/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetReportingPrintableReportsIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetReportingPrintableReportsResponse:
        """
        Returns a list of Printable Reports within the data field
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
            path="/reporting/printable-reports",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetReportingPrintableReportsResponse,
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
            path=f"/reporting/printable-reports/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Delete,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncPrintableReportsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.create = AsyncCreateClient(base_client=self._base_client)
        self.delete_many = AsyncDeleteManyClient(base_client=self._base_client)
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
    ) -> models.GetReportingPrintableReportsIdResponse:
        """
        Returns a Printable Report based on a single ID
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
            path=f"/reporting/printable-reports/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetReportingPrintableReportsIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetReportingPrintableReportsResponse:
        """
        Returns a list of Printable Reports within the data field
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
            path="/reporting/printable-reports",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetReportingPrintableReportsResponse,
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
            path=f"/reporting/printable-reports/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Delete,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
