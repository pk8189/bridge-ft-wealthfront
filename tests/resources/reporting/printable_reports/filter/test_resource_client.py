"""File Generated by Sideko (sideko.dev)"""

import pytest
from wealthtech_api import AsyncClient, Client
from wealthtech_api.types.reporting.printable_reports.filter import models
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
    response = client.reporting.printable_reports.filter.create(
        pager_limit=123,
        pager_page=123,
        data={
            "account_id": 123,
            "client_accessible": False,
            "created_by_user_id": 8882,
            "dt_utc": "0001-01-01T00:00:00Z",
            "end_date": "2022-08-31",
            "error_message": "string",
            "firm_id": 39,
            "frequency": "string",
            "household_id": 27585,
            "id": 1290371,
            "report_date": "2022-08-31",
            "size_bytes": 115805,
            "start_date": "2022-08-01",
            "state": "0",
            "timestamp_utc": 1660575976,
        },
    )
    adapter = TypeAdapter(models.PostReportingPrintableReportsFilterResponse)
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
    response = await client.reporting.printable_reports.filter.create(
        pager_limit=123,
        pager_page=123,
        data={
            "account_id": 123,
            "client_accessible": False,
            "created_by_user_id": 8882,
            "dt_utc": "0001-01-01T00:00:00Z",
            "end_date": "2022-08-31",
            "error_message": "string",
            "firm_id": 39,
            "frequency": "string",
            "household_id": 27585,
            "id": 1290371,
            "report_date": "2022-08-31",
            "size_bytes": 115805,
            "start_date": "2022-08-01",
            "state": "0",
            "timestamp_utc": 1660575976,
        },
    )
    adapter = TypeAdapter(models.PostReportingPrintableReportsFilterResponse)
    adapter.validate_python(response)
