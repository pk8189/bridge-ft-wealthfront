"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    encode_param,
    to_encodable,
    RequestOptions,
    QueryParams,
    SyncBaseClient,
    AsyncBaseClient,
    default_request_options,
)
from wealthtech_api.types.reporting.printable_reports.create import params, models
import typing


class CreateClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: typing.Optional[params.PostReportingPrintableReportsCreateBody] = None,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostReportingPrintableReportsCreateResponse:
        """
        Starts a Background Job for PDF Reporting and returns the created Background Job Instance

        **Available Sub Reports**
           - `account_summary`
           - `allocation_and_performance_summary`
           - `appraisals`
           - `appraisals_wo_cost_basis`
           - `asset_allocation_top_holdings`
           - `benchmark_perf_summary`
           - `buy_sells`
           - `consolidated_summary`
           - `deposits_withdrawals`
           - `household_performance_attribution`
           - `income`
           - `management_fees`
           - `net_investment_chart`
           - `performance_summary`
           - `performance_chart`
           - `portfolio_snapshot`
           - `realized_gain_loss`
           - `risk_return_chart`
           - `security_performance`
           - `target_vs_actual_allocation`

        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerPostReportingPrintableReportsCreateBody,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/reporting/printable-reports/create",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.PostReportingPrintableReportsCreateResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncCreateClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: typing.Optional[params.PostReportingPrintableReportsCreateBody] = None,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostReportingPrintableReportsCreateResponse:
        """
        Starts a Background Job for PDF Reporting and returns the created Background Job Instance

        **Available Sub Reports**
           - `account_summary`
           - `allocation_and_performance_summary`
           - `appraisals`
           - `appraisals_wo_cost_basis`
           - `asset_allocation_top_holdings`
           - `benchmark_perf_summary`
           - `buy_sells`
           - `consolidated_summary`
           - `deposits_withdrawals`
           - `household_performance_attribution`
           - `income`
           - `management_fees`
           - `net_investment_chart`
           - `performance_summary`
           - `performance_chart`
           - `portfolio_snapshot`
           - `realized_gain_loss`
           - `risk_return_chart`
           - `security_performance`
           - `target_vs_actual_allocation`

        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerPostReportingPrintableReportsCreateBody,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/reporting/printable-reports/create",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.PostReportingPrintableReportsCreateResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
