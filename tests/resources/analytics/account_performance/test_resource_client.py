"""File Generated by Sideko (sideko.dev)"""

import pytest
from wealthtech_api import Client, AsyncClient
import typing
from wealthtech_api.types.analytics.account_performance import models
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
    response = client.analytics.account_performance.create(
        data={"as_of_date": "2022-07-31", "entity_ids": [27585, 28028]}
    )
    adapter = TypeAdapter(
        typing.List[models.PostAnalyticsAccountPerformanceResponseItem]
    )
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
    response = await client.analytics.account_performance.create(
        data={"as_of_date": "2022-07-31", "entity_ids": [27585, 28028]}
    )
    adapter = TypeAdapter(
        typing.List[models.PostAnalyticsAccountPerformanceResponseItem]
    )
    adapter.validate_python(response)
