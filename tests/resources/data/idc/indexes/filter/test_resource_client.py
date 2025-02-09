"""File Generated by Sideko (sideko.dev)"""

import pytest
from wealthtech_api import AsyncClient, Client
from wealthtech_api.types.data.idc.indexes.filter import models
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
    response = client.data.idc.indexes.filter.create(
        pager_limit=123,
        pager_page=123,
        data={
            "cusip": "string",
            "id": 123,
            "internal_name": "string",
            "issuer_cusip": "string",
            "name": "string",
            "symbol_field": "string",
            "vendor_name": "string",
        },
    )
    adapter = TypeAdapter(models.PostDataIdcIndexesFilterResponse)
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
    response = await client.data.idc.indexes.filter.create(
        pager_limit=123,
        pager_page=123,
        data={
            "cusip": "string",
            "id": 123,
            "internal_name": "string",
            "issuer_cusip": "string",
            "name": "string",
            "symbol_field": "string",
            "vendor_name": "string",
        },
    )
    adapter = TypeAdapter(models.PostDataIdcIndexesFilterResponse)
    adapter.validate_python(response)
