"""File Generated by Sideko (sideko.dev)"""

import pytest
from wealthtech_api import AsyncClient, Client
from wealthtech_api.types.billing.invoices.download import models
from pydantic import TypeAdapter
from wealthtech_api.types.binary_response import BinaryResponse

# test sync & async methods (keep comment for code generation)


def test_create_by_id_200_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = client.billing.invoices.download.create_by_id(
        id=123,
        pager_limit=123,
        pager_page=123,
        data={"accept": "string", "content_type": "string"},
    )
    assert isinstance(response, BinaryResponse)


@pytest.mark.asyncio
async def test_await_create_by_id_200_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = await client.billing.invoices.download.create_by_id(
        id=123,
        pager_limit=123,
        pager_page=123,
        data={"accept": "string", "content_type": "string"},
    )
    assert isinstance(response, BinaryResponse)


def test_create_200_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = client.billing.invoices.download.create(
        pager_limit=123, pager_page=123, data={"ids": [123]}
    )
    adapter = TypeAdapter(models.PostBillingInvoicesDownloadResponse)
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
    response = await client.billing.invoices.download.create(
        pager_limit=123, pager_page=123, data={"ids": [123]}
    )
    adapter = TypeAdapter(models.PostBillingInvoicesDownloadResponse)
    adapter.validate_python(response)
