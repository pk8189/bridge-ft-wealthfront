"""File Generated by Sideko (sideko.dev)"""

import pytest
from wealthtech_api import AsyncClient, Client
from wealthtech_api.types.investment_management.strategies import models
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
    response = client.investment_management.strategies.put_by_id(
        id=123,
        data={
            "asset_type": "string",
            "benchmark_id": 123,
            "created_at_utc": "1970-01-01T00:00:00",
            "description": "string",
            "esg": True,
            "etf_action_identifier": "string",
            "fact_sheet_available": True,
            "fee": 123.45,
            "firm_id": 123,
            "id": 123,
            "investment_minimum": 123.45,
            "name": "string",
            "provider": "string",
            "risk_category": "GR",
            "search_tags": ["string"],
            "security_allocations": [
                {"id": 123, "security_id": 123, "strategy_id": 123, "weight": 123.45}
            ],
            "strategy_type": "Core",
            "tax_managed": True,
            "updated_at_utc": "1970-01-01T00:00:00",
        },
    )
    adapter = TypeAdapter(models.PutInvestmentManagementStrategiesIdResponse)
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
    response = await client.investment_management.strategies.put_by_id(
        id=123,
        data={
            "asset_type": "string",
            "benchmark_id": 123,
            "created_at_utc": "1970-01-01T00:00:00",
            "description": "string",
            "esg": True,
            "etf_action_identifier": "string",
            "fact_sheet_available": True,
            "fee": 123.45,
            "firm_id": 123,
            "id": 123,
            "investment_minimum": 123.45,
            "name": "string",
            "provider": "string",
            "risk_category": "GR",
            "search_tags": ["string"],
            "security_allocations": [
                {"id": 123, "security_id": 123, "strategy_id": 123, "weight": 123.45}
            ],
            "strategy_type": "Core",
            "tax_managed": True,
            "updated_at_utc": "1970-01-01T00:00:00",
        },
    )
    adapter = TypeAdapter(models.PutInvestmentManagementStrategiesIdResponse)
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
    response = client.investment_management.strategies.put(
        data=[
            {
                "asset_type": "string",
                "benchmark_id": 123,
                "created_at_utc": "1970-01-01T00:00:00",
                "description": "string",
                "esg": True,
                "etf_action_identifier": "string",
                "fact_sheet_available": True,
                "fee": 123.45,
                "firm_id": 123,
                "id": 123,
                "investment_minimum": 123.45,
                "name": "string",
                "provider": "string",
                "risk_category": "AG",
                "search_tags": ["string"],
                "security_allocations": [
                    {
                        "id": 123,
                        "security_id": 123,
                        "strategy_id": 123,
                        "weight": 123.45,
                    }
                ],
                "strategy_type": "Alternatives",
                "tax_managed": True,
                "updated_at_utc": "1970-01-01T00:00:00",
            }
        ]
    )
    adapter = TypeAdapter(models.PutInvestmentManagementStrategiesResponse)
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
    response = await client.investment_management.strategies.put(
        data=[
            {
                "asset_type": "string",
                "benchmark_id": 123,
                "created_at_utc": "1970-01-01T00:00:00",
                "description": "string",
                "esg": True,
                "etf_action_identifier": "string",
                "fact_sheet_available": True,
                "fee": 123.45,
                "firm_id": 123,
                "id": 123,
                "investment_minimum": 123.45,
                "name": "string",
                "provider": "string",
                "risk_category": "AG",
                "search_tags": ["string"],
                "security_allocations": [
                    {
                        "id": 123,
                        "security_id": 123,
                        "strategy_id": 123,
                        "weight": 123.45,
                    }
                ],
                "strategy_type": "Alternatives",
                "tax_managed": True,
                "updated_at_utc": "1970-01-01T00:00:00",
            }
        ]
    )
    adapter = TypeAdapter(models.PutInvestmentManagementStrategiesResponse)
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
    response = client.investment_management.strategies.create(
        pager_limit=123,
        pager_page=123,
        data={
            "firm_id": 39,
            "name": "Demo Strategy - Fidelity Aggressive Equity",
            "security_allocations": [
                {"security_id": 236, "weight": 80},
                {"security_id": 78, "weight": 20},
            ],
        },
    )
    adapter = TypeAdapter(models.PostInvestmentManagementStrategiesResponse)
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
    response = await client.investment_management.strategies.create(
        pager_limit=123,
        pager_page=123,
        data={
            "firm_id": 39,
            "name": "Demo Strategy - Fidelity Aggressive Equity",
            "security_allocations": [
                {"security_id": 236, "weight": 80},
                {"security_id": 78, "weight": 20},
            ],
        },
    )
    adapter = TypeAdapter(models.PostInvestmentManagementStrategiesResponse)
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
    response = client.investment_management.strategies.get(
        id=123, pager_limit=123, pager_page=123
    )
    adapter = TypeAdapter(models.GetInvestmentManagementStrategiesIdResponse)
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
    response = await client.investment_management.strategies.get(
        id=123, pager_limit=123, pager_page=123
    )
    adapter = TypeAdapter(models.GetInvestmentManagementStrategiesIdResponse)
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
    response = client.investment_management.strategies.list(
        pager_limit=123, pager_page=123
    )
    adapter = TypeAdapter(models.GetInvestmentManagementStrategiesResponse)
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
    response = await client.investment_management.strategies.list(
        pager_limit=123, pager_page=123
    )
    adapter = TypeAdapter(models.GetInvestmentManagementStrategiesResponse)
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
    response = client.investment_management.strategies.delete(
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
    response = await client.investment_management.strategies.delete(
        id=123, pager_limit=123, pager_page=123
    )
    adapter = TypeAdapter(models.Delete)
    adapter.validate_python(response)
