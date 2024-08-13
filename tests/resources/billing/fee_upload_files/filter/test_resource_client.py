"""File Generated by Sideko (sideko.dev)"""

import pytest
from wealthtech_api import Client, AsyncClient
from wealthtech_api.types.billing.fee_upload_files.filter import models
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
    response = client.billing.fee_upload_files.filter.create(
        pager_limit=123,
        pager_page=123,
        data={
            "end_date": "2017-07-31T00:00:00Z",
            "firm_id": 39,
            "id": 33,
            "num_accounts": 15,
            "num_custodians": 3,
            "num_files": 6,
            "num_households": 123,
            "total_annual_debit": 123.45,
            "total_period_debit": 123.45,
        },
    )
    adapter = TypeAdapter(models.PostBillingFeeUploadFilesFilterResponse)
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
    response = await client.billing.fee_upload_files.filter.create(
        pager_limit=123,
        pager_page=123,
        data={
            "end_date": "2017-07-31T00:00:00Z",
            "firm_id": 39,
            "id": 33,
            "num_accounts": 15,
            "num_custodians": 3,
            "num_files": 6,
            "num_households": 123,
            "total_annual_debit": 123.45,
            "total_period_debit": 123.45,
        },
    )
    adapter = TypeAdapter(models.PostBillingFeeUploadFilesFilterResponse)
    adapter.validate_python(response)
