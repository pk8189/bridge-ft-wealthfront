"""File Generated by Sideko (sideko.dev)"""

import pytest
from wealthtech_api import AsyncClient, Client
from wealthtech_api.types.reporting.report_settings.filter import models
from pydantic import TypeAdapter

# test sync & async methods (keep comment for code generation)


def test_create_200_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = client.reporting.report_settings.filter.create(
        pager_limit=123,
        pager_page=123,
        data={
            "account_summary": True,
            "appraisals": True,
            "asset_allocation_top_holdings": True,
            "benchmark_perf_summary": True,
            "buy_sells": True,
            "component": "advisor_defaults",
            "consolidated_summary": True,
            "deposits_withdrawals": True,
            "firm_id": 39,
            "id": 95,
            "income": True,
            "management_fees": True,
            "net_investment_chart": True,
            "performance_chart": True,
            "performance_summary": True,
            "portfolio_snapshot": False,
            "realized_gain_loss": True,
            "user_id": 123,
        },
    )
    adapter = TypeAdapter(models.PostReportingReportSettingsFilterResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_create_200_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = await client.reporting.report_settings.filter.create(
        pager_limit=123,
        pager_page=123,
        data={
            "account_summary": True,
            "appraisals": True,
            "asset_allocation_top_holdings": True,
            "benchmark_perf_summary": True,
            "buy_sells": True,
            "component": "advisor_defaults",
            "consolidated_summary": True,
            "deposits_withdrawals": True,
            "firm_id": 39,
            "id": 95,
            "income": True,
            "management_fees": True,
            "net_investment_chart": True,
            "performance_chart": True,
            "performance_summary": True,
            "portfolio_snapshot": False,
            "realized_gain_loss": True,
            "user_id": 123,
        },
    )
    adapter = TypeAdapter(models.PostReportingReportSettingsFilterResponse)
    adapter.validate_python(response)
