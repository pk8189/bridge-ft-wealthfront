"""File Generated by Sideko (sideko.dev)"""

import pytest
from wealthtech_api import Client, AsyncClient
from wealthtech_api.types.account_management.related_persons import models
from pydantic import TypeAdapter

# test sync & async methods (keep comment for code generation)


def test_list_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        base_url="https://api.sideko.dev/v1/api_project/a9773eee-d42b-469d-a46d-faaf05e641b0/version/43ecbc55-8afa-476e-ab94-df5433a98189/mock",
    )
    response = client.account_management.related_persons.list(
        pager_limit=123, pager_page=123
    )
    adapter = TypeAdapter(models.GetAccountManagementRelatedPersonsResponse)
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
    response = await client.account_management.related_persons.list(
        pager_limit=123, pager_page=123
    )
    adapter = TypeAdapter(models.GetAccountManagementRelatedPersonsResponse)
    adapter.validate_python(response)
