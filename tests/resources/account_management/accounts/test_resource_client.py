"""File Generated by Sideko (sideko.dev)"""

import pytest
from wealthtech_api import AsyncClient, Client
from wealthtech_api.types.account_management.accounts import models
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
    response = client.account_management.accounts.put_by_id(
        id=123,
        data={
            "acct_type": "string",
            "address_1": "string",
            "address_2": "string",
            "address_3": "string",
            "advisor_code": "string",
            "advisor_codes": ["string"],
            "benchmarks_ids": [123],
            "billing_splits_ids": [123],
            "buy_securities_ids": [123],
            "city": "string",
            "close_date": "1970-01-01T00:00:00",
            "country": "string",
            "created_at_utc": "1970-01-01T00:00:00",
            "custodian": "PER",
            "custodian_name": "string",
            "display_name": "string",
            "display_number": "string",
            "do_not_buy_securities_ids": [123],
            "do_not_sell_securities_ids": [123],
            "entity_id": "string",
            "fee_structures_ids": [123],
            "firm_id": 123,
            "first_billable_date": "1970-01-01T00:00:00",
            "first_cost_basis_date": "1970-01-01T00:00:00",
            "first_funded_date": "1970-01-01T00:00:00",
            "first_papered_date": "1970-01-01T00:00:00",
            "first_performance_date": "1970-01-01T00:00:00",
            "first_positions_date": "1970-01-01",
            "first_quarantine_date": "1970-01-01",
            "first_transactions_date": "1970-01-01",
            "has_custodian_name": True,
            "household_id": 123,
            "id": 123,
            "inception_date": "1970-01-01T00:00:00",
            "investment_model_id": 123,
            "is_account": True,
            "is_active": True,
            "is_closed": True,
            "is_custodian_billed": True,
            "is_direct_billed": True,
            "is_household": True,
            "is_tax_deferred": True,
            "is_taxable": True,
            "last_cost_basis_date": "1970-01-01T00:00:00",
            "last_portfolio_data_date": "1970-01-01T00:00:00",
            "last_positions_date": "1970-01-01",
            "last_reporting_date": "1970-01-01",
            "last_transactions_date": "1970-01-01",
            "name": "string",
            "notes": "string",
            "number": "string",
            "payment_source": "C",
            "required_cash": 123.45,
            "required_cash_frequency": "Q",
            "sell_securities_ids": [123],
            "short_name": "string",
            "state": "string",
            "status": "funded",
            "target_allocation_id": 123,
            "tax_id_token": "string",
            "unsupervised_securities_ids": [123],
            "updated_at_utc": "1970-01-01T00:00:00",
            "zip_code": "string",
        },
    )
    adapter = TypeAdapter(models.Account)
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
    response = await client.account_management.accounts.put_by_id(
        id=123,
        data={
            "acct_type": "string",
            "address_1": "string",
            "address_2": "string",
            "address_3": "string",
            "advisor_code": "string",
            "advisor_codes": ["string"],
            "benchmarks_ids": [123],
            "billing_splits_ids": [123],
            "buy_securities_ids": [123],
            "city": "string",
            "close_date": "1970-01-01T00:00:00",
            "country": "string",
            "created_at_utc": "1970-01-01T00:00:00",
            "custodian": "PER",
            "custodian_name": "string",
            "display_name": "string",
            "display_number": "string",
            "do_not_buy_securities_ids": [123],
            "do_not_sell_securities_ids": [123],
            "entity_id": "string",
            "fee_structures_ids": [123],
            "firm_id": 123,
            "first_billable_date": "1970-01-01T00:00:00",
            "first_cost_basis_date": "1970-01-01T00:00:00",
            "first_funded_date": "1970-01-01T00:00:00",
            "first_papered_date": "1970-01-01T00:00:00",
            "first_performance_date": "1970-01-01T00:00:00",
            "first_positions_date": "1970-01-01",
            "first_quarantine_date": "1970-01-01",
            "first_transactions_date": "1970-01-01",
            "has_custodian_name": True,
            "household_id": 123,
            "id": 123,
            "inception_date": "1970-01-01T00:00:00",
            "investment_model_id": 123,
            "is_account": True,
            "is_active": True,
            "is_closed": True,
            "is_custodian_billed": True,
            "is_direct_billed": True,
            "is_household": True,
            "is_tax_deferred": True,
            "is_taxable": True,
            "last_cost_basis_date": "1970-01-01T00:00:00",
            "last_portfolio_data_date": "1970-01-01T00:00:00",
            "last_positions_date": "1970-01-01",
            "last_reporting_date": "1970-01-01",
            "last_transactions_date": "1970-01-01",
            "name": "string",
            "notes": "string",
            "number": "string",
            "payment_source": "C",
            "required_cash": 123.45,
            "required_cash_frequency": "Q",
            "sell_securities_ids": [123],
            "short_name": "string",
            "state": "string",
            "status": "funded",
            "target_allocation_id": 123,
            "tax_id_token": "string",
            "unsupervised_securities_ids": [123],
            "updated_at_utc": "1970-01-01T00:00:00",
            "zip_code": "string",
        },
    )
    adapter = TypeAdapter(models.Account)
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
    response = client.account_management.accounts.put(
        data=[
            {
                "acct_type": "string",
                "address_1": "string",
                "address_2": "string",
                "address_3": "string",
                "advisor_code": "string",
                "advisor_codes": ["string"],
                "benchmarks_ids": [123],
                "billing_splits_ids": [123],
                "buy_securities_ids": [123],
                "city": "string",
                "close_date": "1970-01-01T00:00:00",
                "country": "string",
                "created_at_utc": "1970-01-01T00:00:00",
                "custodian": "NFS",
                "custodian_name": "string",
                "display_name": "string",
                "display_number": "string",
                "do_not_buy_securities_ids": [123],
                "do_not_sell_securities_ids": [123],
                "entity_id": "string",
                "fee_structures_ids": [123],
                "firm_id": 123,
                "first_billable_date": "1970-01-01T00:00:00",
                "first_cost_basis_date": "1970-01-01T00:00:00",
                "first_funded_date": "1970-01-01T00:00:00",
                "first_papered_date": "1970-01-01T00:00:00",
                "first_performance_date": "1970-01-01T00:00:00",
                "first_positions_date": "1970-01-01",
                "first_quarantine_date": "1970-01-01",
                "first_transactions_date": "1970-01-01",
                "has_custodian_name": True,
                "household_id": 123,
                "id": 123,
                "inception_date": "1970-01-01T00:00:00",
                "investment_model_id": 123,
                "is_account": True,
                "is_active": True,
                "is_closed": True,
                "is_custodian_billed": True,
                "is_direct_billed": True,
                "is_household": True,
                "is_tax_deferred": True,
                "is_taxable": True,
                "last_cost_basis_date": "1970-01-01T00:00:00",
                "last_portfolio_data_date": "1970-01-01T00:00:00",
                "last_positions_date": "1970-01-01",
                "last_reporting_date": "1970-01-01",
                "last_transactions_date": "1970-01-01",
                "name": "string",
                "notes": "string",
                "number": "string",
                "payment_source": "C",
                "required_cash": 123.45,
                "required_cash_frequency": "O",
                "sell_securities_ids": [123],
                "short_name": "string",
                "state": "string",
                "status": "closed",
                "target_allocation_id": 123,
                "tax_id_token": "string",
                "unsupervised_securities_ids": [123],
                "updated_at_utc": "1970-01-01T00:00:00",
                "zip_code": "string",
            }
        ]
    )
    adapter = TypeAdapter(models.PutAccountManagementAccountsResponse)
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
    response = await client.account_management.accounts.put(
        data=[
            {
                "acct_type": "string",
                "address_1": "string",
                "address_2": "string",
                "address_3": "string",
                "advisor_code": "string",
                "advisor_codes": ["string"],
                "benchmarks_ids": [123],
                "billing_splits_ids": [123],
                "buy_securities_ids": [123],
                "city": "string",
                "close_date": "1970-01-01T00:00:00",
                "country": "string",
                "created_at_utc": "1970-01-01T00:00:00",
                "custodian": "NFS",
                "custodian_name": "string",
                "display_name": "string",
                "display_number": "string",
                "do_not_buy_securities_ids": [123],
                "do_not_sell_securities_ids": [123],
                "entity_id": "string",
                "fee_structures_ids": [123],
                "firm_id": 123,
                "first_billable_date": "1970-01-01T00:00:00",
                "first_cost_basis_date": "1970-01-01T00:00:00",
                "first_funded_date": "1970-01-01T00:00:00",
                "first_papered_date": "1970-01-01T00:00:00",
                "first_performance_date": "1970-01-01T00:00:00",
                "first_positions_date": "1970-01-01",
                "first_quarantine_date": "1970-01-01",
                "first_transactions_date": "1970-01-01",
                "has_custodian_name": True,
                "household_id": 123,
                "id": 123,
                "inception_date": "1970-01-01T00:00:00",
                "investment_model_id": 123,
                "is_account": True,
                "is_active": True,
                "is_closed": True,
                "is_custodian_billed": True,
                "is_direct_billed": True,
                "is_household": True,
                "is_tax_deferred": True,
                "is_taxable": True,
                "last_cost_basis_date": "1970-01-01T00:00:00",
                "last_portfolio_data_date": "1970-01-01T00:00:00",
                "last_positions_date": "1970-01-01",
                "last_reporting_date": "1970-01-01",
                "last_transactions_date": "1970-01-01",
                "name": "string",
                "notes": "string",
                "number": "string",
                "payment_source": "C",
                "required_cash": 123.45,
                "required_cash_frequency": "O",
                "sell_securities_ids": [123],
                "short_name": "string",
                "state": "string",
                "status": "closed",
                "target_allocation_id": 123,
                "tax_id_token": "string",
                "unsupervised_securities_ids": [123],
                "updated_at_utc": "1970-01-01T00:00:00",
                "zip_code": "string",
            }
        ]
    )
    adapter = TypeAdapter(models.PutAccountManagementAccountsResponse)
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
    response = client.account_management.accounts.get(
        id=123, pager_limit=123, pager_page=123
    )
    adapter = TypeAdapter(models.Account)
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
    response = await client.account_management.accounts.get(
        id=123, pager_limit=123, pager_page=123
    )
    adapter = TypeAdapter(models.Account)
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
    response = client.account_management.accounts.list(pager_limit=123, pager_page=123)
    adapter = TypeAdapter(models.GetAccountManagementAccountsResponse)
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
    response = await client.account_management.accounts.list(
        pager_limit=123, pager_page=123
    )
    adapter = TypeAdapter(models.GetAccountManagementAccountsResponse)
    adapter.validate_python(response)
