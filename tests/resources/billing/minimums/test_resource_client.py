"""File Generated by Sideko (sideko.dev)"""

import pytest
from wealthtech_api import AsyncClient, Client
from wealthtech_api.types.billing.minimums import models
from pydantic import TypeAdapter

# test sync & async methods (keep comment for code generation)


def test_put_by_id_200_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = client.billing.minimums.put_by_id(
        id=123,
        data={
            "created_at_utc": "1970-01-01T00:00:00",
            "firm_id": 123,
            "id": 123,
            "name": "string",
            "updated_at_utc": "1970-01-01T00:00:00",
            "value": 123.45,
            "value_type": "P",
        },
    )
    adapter = TypeAdapter(models.PutBillingMinimumsIdResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_put_by_id_200_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = await client.billing.minimums.put_by_id(
        id=123,
        data={
            "created_at_utc": "1970-01-01T00:00:00",
            "firm_id": 123,
            "id": 123,
            "name": "string",
            "updated_at_utc": "1970-01-01T00:00:00",
            "value": 123.45,
            "value_type": "P",
        },
    )
    adapter = TypeAdapter(models.PutBillingMinimumsIdResponse)
    adapter.validate_python(response)


def test_put_200_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = client.billing.minimums.put(
        data=[
            {
                "created_at_utc": "1970-01-01T00:00:00",
                "firm_id": 123,
                "id": 123,
                "name": "string",
                "updated_at_utc": "1970-01-01T00:00:00",
                "value": 123.45,
                "value_type": "P",
            }
        ]
    )
    adapter = TypeAdapter(models.PutBillingMinimumsResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_put_200_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = await client.billing.minimums.put(
        data=[
            {
                "created_at_utc": "1970-01-01T00:00:00",
                "firm_id": 123,
                "id": 123,
                "name": "string",
                "updated_at_utc": "1970-01-01T00:00:00",
                "value": 123.45,
                "value_type": "P",
            }
        ]
    )
    adapter = TypeAdapter(models.PutBillingMinimumsResponse)
    adapter.validate_python(response)


def test_create_200_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = client.billing.minimums.create(
        pager_limit=123,
        pager_page=123,
        data={
            "firm_id": 39,
            "name": "Insurance Claim",
            "value": 2500,
            "value_type": "F",
        },
    )
    adapter = TypeAdapter(models.PostBillingMinimumsResponse)
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
    response = await client.billing.minimums.create(
        pager_limit=123,
        pager_page=123,
        data={
            "firm_id": 39,
            "name": "Insurance Claim",
            "value": 2500,
            "value_type": "F",
        },
    )
    adapter = TypeAdapter(models.PostBillingMinimumsResponse)
    adapter.validate_python(response)


def test_get_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = client.billing.minimums.get(id=123, pager_limit=123, pager_page=123)
    adapter = TypeAdapter(models.GetBillingMinimumsIdResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = await client.billing.minimums.get(
        id=123, pager_limit=123, pager_page=123
    )
    adapter = TypeAdapter(models.GetBillingMinimumsIdResponse)
    adapter.validate_python(response)


def test_list_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = client.billing.minimums.list(pager_limit=123, pager_page=123)
    adapter = TypeAdapter(models.GetBillingMinimumsResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = await client.billing.minimums.list(pager_limit=123, pager_page=123)
    adapter = TypeAdapter(models.GetBillingMinimumsResponse)
    adapter.validate_python(response)


def test_delete_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = client.billing.minimums.delete(id=123, pager_limit=123, pager_page=123)
    adapter = TypeAdapter(models.Delete)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_delete_200_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = await client.billing.minimums.delete(
        id=123, pager_limit=123, pager_page=123
    )
    adapter = TypeAdapter(models.Delete)
    adapter.validate_python(response)
