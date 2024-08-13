"""File Generated by Sideko (sideko.dev)"""

import pytest
from wealthtech_api import Client, AsyncClient
from wealthtech_api.types.data.source.transactions.latest import models
from pydantic import TypeAdapter

# test sync & async methods (keep comment for code generation)


def test_list_200_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = client.data.source.transactions.latest.list(
        pager_limit=123,
        pager_page=123,
        data={
            "account_id": 123,
            "account_ids": [216897, 216898],
            "account_number": "string",
            "category": "crp",
            "classification": "exp",
            "feed_code": "string",
            "id": 123,
            "reported_date": "1970-01-01T00:00:00",
            "security_id": 123,
            "source": "DST",
            "source_security_cusip": "string",
            "source_security_symbol": "string",
            "source_transaction_code": "string",
            "trade_settle_ind": "S",
            "transaction_date": "1970-01-01T00:00:00",
        },
    )
    adapter = TypeAdapter(models.GetDataSourceTransactionsLatestResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_list_200_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = await client.data.source.transactions.latest.list(
        pager_limit=123,
        pager_page=123,
        data={
            "account_id": 123,
            "account_ids": [216897, 216898],
            "account_number": "string",
            "category": "crp",
            "classification": "exp",
            "feed_code": "string",
            "id": 123,
            "reported_date": "1970-01-01T00:00:00",
            "security_id": 123,
            "source": "DST",
            "source_security_cusip": "string",
            "source_security_symbol": "string",
            "source_transaction_code": "string",
            "trade_settle_ind": "S",
            "transaction_date": "1970-01-01T00:00:00",
        },
    )
    adapter = TypeAdapter(models.GetDataSourceTransactionsLatestResponse)
    adapter.validate_python(response)
