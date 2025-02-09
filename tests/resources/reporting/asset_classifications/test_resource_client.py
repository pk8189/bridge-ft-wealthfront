"""File Generated by Sideko (sideko.dev)"""

import pytest
from wealthtech_api import Client, AsyncClient
from wealthtech_api.types.reporting.asset_classifications import models
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
    response = client.reporting.asset_classifications.put_by_id(
        id=123,
        data={
            "class_tag_id": 123,
            "created_at_utc": "1970-01-01T00:00:00",
            "created_by_user_id": 123,
            "firm_id": 123,
            "id": 123,
            "security_id": 123,
            "updated_at_utc": "1970-01-01T00:00:00",
        },
    )
    adapter = TypeAdapter(models.PutReportingAssetClassificationsIdResponse)
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
    response = await client.reporting.asset_classifications.put_by_id(
        id=123,
        data={
            "class_tag_id": 123,
            "created_at_utc": "1970-01-01T00:00:00",
            "created_by_user_id": 123,
            "firm_id": 123,
            "id": 123,
            "security_id": 123,
            "updated_at_utc": "1970-01-01T00:00:00",
        },
    )
    adapter = TypeAdapter(models.PutReportingAssetClassificationsIdResponse)
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
    response = client.reporting.asset_classifications.put(
        data=[
            {
                "class_tag_id": 123,
                "created_at_utc": "1970-01-01T00:00:00",
                "created_by_user_id": 123,
                "firm_id": 123,
                "id": 123,
                "security_id": 123,
                "updated_at_utc": "1970-01-01T00:00:00",
            }
        ]
    )
    adapter = TypeAdapter(models.PutReportingAssetClassificationsResponse)
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
    response = await client.reporting.asset_classifications.put(
        data=[
            {
                "class_tag_id": 123,
                "created_at_utc": "1970-01-01T00:00:00",
                "created_by_user_id": 123,
                "firm_id": 123,
                "id": 123,
                "security_id": 123,
                "updated_at_utc": "1970-01-01T00:00:00",
            }
        ]
    )
    adapter = TypeAdapter(models.PutReportingAssetClassificationsResponse)
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
    response = client.reporting.asset_classifications.create(
        pager_limit=123,
        pager_page=123,
        data={
            "class_tag_id": 188,
            "created_by_user_id": 265,
            "firm_id": 39,
            "security_id": 332905,
        },
    )
    adapter = TypeAdapter(models.PostReportingAssetClassificationsResponse)
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
    response = await client.reporting.asset_classifications.create(
        pager_limit=123,
        pager_page=123,
        data={
            "class_tag_id": 188,
            "created_by_user_id": 265,
            "firm_id": 39,
            "security_id": 332905,
        },
    )
    adapter = TypeAdapter(models.PostReportingAssetClassificationsResponse)
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
    response = client.reporting.asset_classifications.get(
        id=123, pager_limit=123, pager_page=123
    )
    adapter = TypeAdapter(models.GetReportingAssetClassificationsIdResponse)
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
    response = await client.reporting.asset_classifications.get(
        id=123, pager_limit=123, pager_page=123
    )
    adapter = TypeAdapter(models.GetReportingAssetClassificationsIdResponse)
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
    response = client.reporting.asset_classifications.list(
        pager_limit=123, pager_page=123
    )
    adapter = TypeAdapter(models.GetReportingAssetClassificationsResponse)
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
    response = await client.reporting.asset_classifications.list(
        pager_limit=123, pager_page=123
    )
    adapter = TypeAdapter(models.GetReportingAssetClassificationsResponse)
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
    response = client.reporting.asset_classifications.delete(
        id=123, pager_limit=123, pager_page=123
    )
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
    response = await client.reporting.asset_classifications.delete(
        id=123, pager_limit=123, pager_page=123
    )
    adapter = TypeAdapter(models.Delete)
    adapter.validate_python(response)
