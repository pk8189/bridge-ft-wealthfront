
# Wealthtech API Python SDK

## Overview
RESTful API for controlling and interacting with Atlas data

## Initilization
Initialize either the synchronous or asynchronous client to authenticate

### Synchronous Client
```python
from wealthtech_api import Client
from os import getenv

Client(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
```

### Asynchronous Client
```python
from wealthtech_api import AsyncClient
from os import getenv

AsyncClient(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
```


### Delete an Asset Adjustment
> Returns the "OK" message and a json object with the id  of item deleted, if deletion was successful

```python
client.billing.asset_adjustments.delete(id=123, pager_limit=123, pager_page=123)
```

---

### Delete a Fee Structure
> Deletes the record for the provided fee structure ID.

```python
client.billing.fee_structures.delete(id=123, pager_limit=123, pager_page=123)
```

---

### Delete a Billing Group
> Deletes the billing group record for the provided ID.

```python
client.billing.groups.delete(id=123, pager_limit=123, pager_page=123)
```

---

### Delete a Minimum
> Deletes the billing minimum record for the provided ID.

```python
client.billing.minimums.delete(id=123, pager_limit=123, pager_page=123)
```

---

### Delete a Billing Report
> Deletes the billing report record for the provided ID.

```python
client.billing.reports.delete(id=123, pager_limit=123, pager_page=123)
```

---

### Delete a Billing Split
> Delete the billing split record for the provided ID
> 

```python
client.billing.splits.delete(id=123, pager_limit=123, pager_page=123)
```

---

### Delete a Model
> Returns the "OK" message and a json object with the id  of item deleted, if deletion was successful

```python
client.investment_management.models.delete(id=123, pager_limit=123, pager_page=123)
```

---

### Delete a Strategy
> Returns the "OK" message and a json object with the id  of item deleted, if deletion was successful

```python
client.investment_management.strategies.delete(id=123, pager_limit=123, pager_page=123)
```

---

### Remove an Advisor Code
> Returns the "OK" message and a json object with the id the advisor codes removed, if deletion was successful
> 
> **Note for Advisor Code Mapping in Sandbox Applications**
> To preserve the data integrity of sandbox applications, the advisor code mapping endpoints are read-only
> and requests for creation or deletion of advisor codes will not result in updates to advisor code mappings.
> Sandbox applications can read advisor codes from the `/v2/org/advisor-codes` endpoint, but the changes will not
> be reflected upon updates.
> 
> For production applications, full access is granted to the advisor code mapping endpoints. Creations and removals
> of advisor codes will be applied to the advisor codes mapped to the application.
> 

```python
client.org.advisor_codes.delete(id=123)
```

---

### Delete an Asset Classification
> Returns the "OK" message and a json object with the id  of item deleted, if deletion was successful

```python
client.reporting.asset_classifications.delete(id=123, pager_limit=123, pager_page=123)
```

---

### Delete a Benchmark
> Returns the "OK" message and a json object with the id  of item deleted, if deletion was successful

```python
client.reporting.benchmarks.delete(id=123, pager_limit=123, pager_page=123)
```

---

### Delete a classification Tag
> Returns the "OK" message and a json object with the id  of item deleted, if deletion was successful

```python
client.reporting.class_tags.delete(id=123, pager_limit=123, pager_page=123)
```

---

### Delete a Printable Report
> Returns the "OK" message and a json object with the id  of item deleted, if deletion was successful

```python
client.reporting.printable_reports.delete(id=123, pager_limit=123, pager_page=123)
```

---

### Delete a Target Allocation
> Returns the "OK" message and a json object with the id  of item deleted, if deletion was successful

```python
client.reporting.target_allocations.delete(id=123, pager_limit=123, pager_page=123)
```

---

### List all Accounts
> Return an enveloped list of Accounts accessible to your application

```python
client.account_management.accounts.list(pager_limit=123, pager_page=123)
```

---

### Retrieve an Account
> Returns an account based on a single ID

```python
client.account_management.accounts.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Related Persons
> Returns a list of all related persons for accessible accounts.

```python
client.account_management.related_persons.list(pager_limit=123, pager_page=123)
```

---

### List all TDA to Schwab Migrated Accounts
> Retrieve the list of all your TDA Accounts which are subjected to be migrated to Schwab.

```python
client.account_management.tda_to_swb_migrations.list(pager_limit=123, pager_page=123)
```

---

### Firm-Wide AUM Records
> Returns a list of all firm-wide AUM records that have been calculated over-time. Firm-wide AUM is calculated by BridgeFT daily, stored as a resource and accessible over this API. This enables consumers to view firm AUM as a monthly or daily time-series.

```python
client.analytics.aum.list(
    as_of_date="1970-01-01", firm_id=123, frequency="D", pager_limit=123, pager_page=123
)
```

---

### Retrieve Firm-Wide Asset Under Management Values
> Returns values of assets under management Firm-wide by ID.

```python
client.analytics.aum.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Asset Adjustments
> Returns a list of Asset Adjustments within the data field

```python
client.billing.asset_adjustments.list(pager_limit=123, pager_page=123)
```

---

### Retrieve an Asset Adjustment
> Returns an Asset Adjustment based on a single ID

```python
client.billing.asset_adjustments.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Fee Structures
> Returns an enveloped list of Fee Structures.

```python
client.billing.fee_structures.list(pager_limit=123, pager_page=123)
```

---

### Retrieve a Fee Structure
> Returns the fee structure record for the provided ID

```python
client.billing.fee_structures.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Fee Upload Files
> Return an enveloped list of fee upload files generated by your application.

```python
client.billing.fee_upload_files.list(pager_limit=123, pager_page=123)
```

---

### Retrieve a Fee Upload File
> Returns the fee upload file record for the provided ID.

```python
client.billing.fee_upload_files.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Billing Groups
> Retrieve the enveloped list of Billing Groups

```python
client.billing.groups.list(pager_limit=123, pager_page=123)
```

---

### Retrieve a Billing Group
> Returns a billing group record for a provided ID

```python
client.billing.groups.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Invoices
> Returns an enveloped list of invoices generated from Billing Reports.

```python
client.billing.invoices.list(pager_limit=123, pager_page=123)
```

---

### Retrieve an Invoice
> Returns an invoice detail object for the provided ID.

```python
client.billing.invoices.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Minimums
> Returns an enveloped list of Billing Minimums.

```python
client.billing.minimums.list(pager_limit=123, pager_page=123)
```

---

### Retrieve a Minimum
> Returns a Billing Minimum record for the provided ID.

```python
client.billing.minimums.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Billing Reports
> Returns a list of Billing Reports within the data field

```python
client.billing.reports.list(pager_limit=123, pager_page=123)
```

---

### Retrieve a Billing Report
> Returns a Billing Report based on a single ID

```python
client.billing.reports.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Billing Splits
> Returns an enveloped list of Billing Split records

```python
client.billing.splits.list(pager_limit=123, pager_page=123)
```

---

### Retrieve a Billing Split
> Returns the Billing Split record for the provided ID

```python
client.billing.splits.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Securities
> Returns a list of securities

```python
client.data.custodian.securities.list(pager_limit=123, pager_page=123)
```

---

### Get Compressed Securities
> Returns compressed and modified representations of all Securities that are being tracked

```python
client.data.custodian.securities.get_compressed.list(pager_limit=123, pager_page=123)
```

---

### Get Security with USD
> Returns the first security object where the issue_type_code is 1

```python
client.data.custodian.securities.get_usd.list(pager_limit=123, pager_page=123)
```

---

### Get Managed Securities
> Returns a list of security ids that belong to the user's household and firm

```python
client.data.custodian.securities.managed.list(pager_limit=123, pager_page=123)
```

---

### Search for Securities
> Returns modified representations of Securities based on input parameters used for filtering

```python
client.data.custodian.securities.search.get(q="string", pager_limit=123, pager_page=123)
```

---

### Retrieve a Security
> Returns a single  security based on an ID

```python
client.data.custodian.securities.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all List all IDC Indexes
> Returns a list of List all IDC Indexes

```python
client.data.idc.indexes.list(pager_limit=123, pager_page=123)
```

---

### Retrieve an IDC Index
> Returns an idc index based on a single ID

```python
client.data.idc.indexes.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all account balances records
> Returns a list of account balances

```python
client.data.source.account_balances.list(
    pager_limit=123, pager_page=123, related="securities"
)
```

---

### Latest Account Balance Records
> Returns a list of the most recent account balance records as of the latest date reported by the custodian. Endpoint Supports optional filtering.

```python
client.data.source.account_balances.latest.list(
    pager_limit=123,
    pager_page=123,
    data={
        "account_id": 123,
        "account_ids": [216897, 216898],
        "account_number": "string",
        "advisor_code": "string",
        "cash_value_aggregated": 123.45,
        "cash_value_reported": 123.45,
        "created_at_utc": "1970-01-01T00:00:00",
        "id": 123,
        "original_data": {},
        "reported_date": "1970-01-01T00:00:00",
        "securities_value_aggregated": 123.45,
        "securities_value_reported": 123.45,
        "source": "FPR",
        "total_value_aggregated": 123.45,
        "total_value_reported": 123.45,
    },
)
```

---

### Retrieve an account balance record
> Returns an account balance record based on its ID

```python
client.data.source.account_balances.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all lots records
> Returns a list of lots

```python
client.data.source.lots.list(
    reported_date="2022-08-28", pager_limit=123, pager_page=123, related="securities"
)
```

---

### Latest Lots Records
> Returns a list of the most recent lot records as of the latest date reported by the custodian. Request body fields can be included in request body, or as query parameters for optional filtering.

```python
client.data.source.lots.latest.list(
    pager_limit=123,
    pager_page=123,
    data={
        "abs_acquisition_quantity": 123.45,
        "abs_adjusted_cost_basis": 123.45,
        "abs_cost_basis": 123.45,
        "abs_current_market_value": 123.45,
        "abs_current_quantity": 123.45,
        "account_id": 123,
        "account_ids": [216897, 216898],
        "account_number": "string",
        "acquisition_date": "1970-01-01T00:00:00",
        "advisor_code": "string",
        "certified": True,
        "created_at_utc": "1970-01-01T00:00:00",
        "direction": "S",
        "disallowed_loss_amount": True,
        "fully_known": True,
        "id": 123,
        "lot_identifier": "string",
        "lot_selection_method": "string",
        "reported_date": "1970-01-01T00:00:00",
        "security_id": 123,
        "source": "TDA (Available prior to Sept. 2, 2023)",
        "source_security_cusip": "string",
        "source_security_symbol": "string",
        "unrealized_gain_loss": 123.45,
        "wash_sale": True,
    },
)
```

---

### Retrieve a lot record
> Returns a lot record based on its ID

```python
client.data.source.lots.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all positions records
> Returns a list of positions

```python
client.data.source.positions.list(
    reported_date="2022-08-28", pager_limit=123, pager_page=123, related="securities"
)
```

---

### Latest Position Records
> Returns a list of the most recent position records as of the latest date reported by the custodian. Request body fields can be included in request body, or as query parameters for optional filtering.

```python
client.data.source.positions.latest.list(
    pager_limit=123,
    pager_page=123,
    data={
        "abs_cost_basis": 123.45,
        "abs_settled_units": 123.45,
        "abs_units": 123.45,
        "account_id": 123,
        "account_ids": [216897, 216898],
        "account_number": "string",
        "advisor_code": "string",
        "calculated_unrealized_gain_loss": 123.45,
        "cost_basis_fully_known": True,
        "created_at_utc": "1970-01-01T00:00:00",
        "direction": "L",
        "id": 123,
        "market_value_unit_price": 123.45,
        "reported_date": "1970-01-01T00:00:00",
        "reported_unrealized_gain_loss": 123.45,
        "security_id": 123,
        "source": "EGB",
        "source_security_cusip": "string",
        "source_security_symbol": "string",
    },
)
```

---

### Retrieve a position record
> Returns a position record based on its ID

```python
client.data.source.positions.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Realized Gain Losses records
> Returns a list of Realized Gain Losses

```python
client.data.source.realized_gain_loss.list(
    reported_date="2022-08-28", pager_limit=123, pager_page=123, related="securities"
)
```

---

### Latest Realized Gain Loss Records
> Returns a list of the most recent realized gain loss records as of the latest date reported by the custodian. Request body fields can be included in request body, or as query parameters for optional filtering.

```python
client.data.source.realized_gain_loss.latest.list(
    pager_limit=123,
    pager_page=123,
    data={
        "abs_closed_units": 123.45,
        "abs_closed_value": 123.45,
        "abs_opened_units": 123.45,
        "abs_opened_value": 123.45,
        "account_id": 123,
        "account_ids": [216897, 216898],
        "account_number": "string",
        "advisor_code": "string",
        "amount": 123.45,
        "amount_long_term": 123.45,
        "amount_short_term": 123.45,
        "close_date": "1970-01-01T00:00:00",
        "created_at_utc": "1970-01-01T00:00:00",
        "direction": "L",
        "id": 123,
        "lot_identifier": "string",
        "lot_selection_method": "string",
        "open_date": "1970-01-01T00:00:00",
        "reported_date": "1970-01-01T00:00:00",
        "security_id": 123,
        "settle_date": "1970-01-01T00:00:00",
        "source": "PER",
        "source_security_cusip": "string",
        "source_security_symbol": "string",
    },
)
```

---

### Retrieve a Realized Gain Loss record
> Returns a Realized Gain Loss record based on its ID

```python
client.data.source.realized_gain_loss.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all transactions records
> Returns a list of transactions

```python
client.data.source.transactions.list(
    pager_limit=123, pager_page=123, related="securities"
)
```

---

### Latest Transaction Records
> Returns a list of the most recent transaction records as of the latest date reported by the custodian. Request body fields can be included in request body, or as query parameters for optional filtering.

```python
client.data.source.transactions.latest.list(
    pager_limit=123,
    pager_page=123,
    data={
        "account_id": 123,
        "account_ids": [216897, 216898],
        "account_number": "string",
        "category": "oth",
        "classification": "btc",
        "feed_code": "string",
        "id": 123,
        "reported_date": "1970-01-01T00:00:00",
        "security_id": 123,
        "source": "APX",
        "source_security_cusip": "string",
        "source_security_symbol": "string",
        "source_transaction_code": "string",
        "trade_settle_ind": "T",
        "transaction_date": "1970-01-01T00:00:00",
    },
)
```

---

### Retrieve a transaction record
> Returns a transaction record based on its ID

```python
client.data.source.transactions.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Models
> Returns a list of models within the data field

```python
client.investment_management.models.list(pager_limit=123, pager_page=123)
```

---

### Retrieve a Model
> Returns a model based on a single ID

```python
client.investment_management.models.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Strategies
> Returns a list of strategies within the data field

```python
client.investment_management.strategies.list(pager_limit=123, pager_page=123)
```

---

### Retrieve a Strategy
> Returns a strategy based on a single ID

```python
client.investment_management.strategies.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Jobs
> Returns a list of jobs

```python
client.jobs.list(pager_limit=123, pager_page=123)
```

---

### Retrieve a Job
> Returns a Job based on a single ID

```python
client.jobs.get(id=123, pager_limit=123, pager_page=123)
```

---

### Get Intrinio Market Data
> Endpoint to access market data from Intrinio. Sign up for an API Key [here](https://docs.intrinio.com/documentation/api_v2/getting_started). The endpoint response varies depending on the Intrinio endpoint provided.

```python
client.market_data.intrinio.get(
    intrinio_endpoint="string", next_page="string", x_intrinio_api_key="string"
)
```

---

### List Advisor Codes
> Returns a list of all of the advisor codes associated with the application.

```python
client.org.advisor_codes.list(pager_limit=123, pager_page=123)
```

---

### List all Firms
> Returns a list of firms within the data field

```python
client.org.firms.list(pager_limit=123, pager_page=123)
```

---

### Retrieve a Firm
> Returns a firm based on a single ID

```python
client.org.firms.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Asset Classifications
> Returns a list of asset classifications within the data field

```python
client.reporting.asset_classifications.list(pager_limit=123, pager_page=123)
```

---

### Retrieve an Asset Classification
> Returns an asset classification based on a single ID

```python
client.reporting.asset_classifications.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Benchmarks
> Returns a list of Benchmarks within the data field

```python
client.reporting.benchmarks.list(pager_limit=123, pager_page=123)
```

---

### Retrieve a Benchmark
> Returns a Benchmark based on a single ID

```python
client.reporting.benchmarks.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Classification Tags
> Returns a list of Classification Tags within the data field

```python
client.reporting.class_tags.list(pager_limit=123, pager_page=123)
```

---

### Retrieve a Classification Tag
> Returns a classification tag based on a single ID

```python
client.reporting.class_tags.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Households
> Returns a list of households within the data field

```python
client.reporting.households.list(pager_limit=123, pager_page=123)
```

---

### Retrieve a Household
> Returns a household based on a single ID

```python
client.reporting.households.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Printable Reports
> Returns a list of Printable Reports within the data field

```python
client.reporting.printable_reports.list(pager_limit=123, pager_page=123)
```

---

### Retrieve a Printable Report
> Returns a Printable Report based on a single ID

```python
client.reporting.printable_reports.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Report Settings
> Returns a list of Report Settings within the data field

```python
client.reporting.report_settings.list(pager_limit=123, pager_page=123)
```

---

### Retrieve Report Settings
> Returns report settings based on a single ID

```python
client.reporting.report_settings.get(id=123, pager_limit=123, pager_page=123)
```

---

### List all Target Allocations
> Returns a list of Target Allocations within the data field

```python
client.reporting.target_allocations.list(pager_limit=123, pager_page=123)
```

---

### Retrieve a Target Allocation
> Returns a Target Allocation based on a single ID

```python
client.reporting.target_allocations.get(id=123, pager_limit=123, pager_page=123)
```

---

### Account Meta Status Summary
> Fetch account meta status summary for all the source data accross the firm

```python
client.status.account_summary.list(reported_date="1970-01-01")
```

---

### Filter Account records
> Filter accounts

```python
client.account_management.accounts.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "acct_type": "401k",
        "advisor_code": "DEMO2",
        "city": "New Irmachester",
        "close_date": "1970-01-01",
        "custodian": "SWB",
        "firm_id": 39,
        "household_id": 68778,
        "id": 216897,
        "inception_date": "1970-01-01",
        "is_tax_deferred": True,
        "is_taxable": True,
        "name": "Violet Juns",
        "number": "DEMO3577",
        "payment_source": "C",
        "status": "funded",
        "zip_code": "90337",
    },
)
```

---

### Filter related persons
> Filter related persons

```python
client.account_management.related_persons.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "account_id": 12341234,
        "account_ids": [12345, 12346],
        "date_of_birth": "1995-09-23",
        "email_field": "john.doe@example.com",
        "entity_name": "John Doe's Company",
        "first_name": "John",
        "id": 1234,
        "last_name": "Doe",
        "middle_initial": "H",
        "tax_id_token": "tax_id_token",
        "type": "Beneficiary",
    },
)
```

---

### Retrieve Many Tokenized Tax IDs
> Exchange multiple Tax IDs for their tokenized representations.

```python
client.account_management.tax_id.create(data=["string"])
```

---

### Exchange Tax ID Tokens
> Exchange list of `tax_id_tokens` For Their Plain Text Values

```python
client.account_management.tax_id.exchange.create(data={"tax_id_tokens": ["string"]})
```

---

### Exchange Tax ID Token
> Exchange`tax_id_token` For Plain Text Value

```python
client.account_management.tax_id.exchange.create_by_tax_id_token(tax_id_token="string")
```

---

### Retrieve Single Tokenized Tax ID
> Exchange a single Tax ID for the tokenized representation.

```python
client.account_management.tax_id.create_by_taxid(taxid="string")
```

---

### Filter TDA to Schwab Migrated Accounts
> Filter out to find particular TDA Account and its respective new Schwab account number.

```python
client.account_management.tda_to_swb_migrations.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "account_id": 216897,
        "account_ids": [216897, 216898],
        "schwab_account_number": "SWBACCOUNT1",
        "schwab_account_numbers": ["SWBACCOUNT1", "SWBACCOUNT2"],
        "schwab_master_number": "SWBMASTERNUMBER1",
        "schwab_master_numbers": ["SWBMASTERNUMBER1", "SWBMASTERNUMBER2"],
        "tda_account_number": "TDAACCOUNT1",
        "tda_account_numbers": ["TDAACCOUNT1", "TDAACCOUNT2"],
        "tda_rep_code": "TDAREPCODE1",
        "tda_rep_codes": ["TDAREPCODE1", "TDAREPCODE2"],
    },
)
```

---

### Account Performance Data
> Fetch Account Performance for a list of Account IDs

```python
client.analytics.account_performance.create(
    data={"as_of_date": "2022-07-31", "entity_ids": [27585, 28028]}
)
```

---

### Account AUM
> Returns AUM records for requested Account(s) on a selected date. Provide a list of `account_ids` and receive the assets under management value for each account.

```python
client.analytics.aum.by_account.create(
    data={"account_ids": [383649, 383912, 383930], "as_of_date": "2023-07-26"}
)
```

---

### Household AUM
> Returns AUM records for requested Household(s) on a selected date. Provide a list of `household_ids` and receive the assets under management value for each household.

```python
client.analytics.aum.by_household.create(
    data={"as_of_date": "2023-07-26", "household_ids": [91243, 108660, 48631]}
)
```

---

### Filter Firm-Wide AUM
> Returns a list of all firm-wide AUM records that have been calculated over-time. Firm-wide AUM is calculated by BridgeFT daily, stored as a resource and accessible over this API. This endpoint enables consumers to view firm AUM filtered by various parameters (as of date, frequency and AUM value) provided in the request body.

```python
client.analytics.aum.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "as_of_date": "2004-05-14T00:00:00Z",
        "firm_id": 39,
        "frequency": "D",
        "id": 294605515,
        "total": 697658,
    },
)
```

---

### Get filtered AUM
> Returns a list of AUM, filtered by frequency and ordered by as_of_date

```python
client.analytics.aum.get_aum.create(pager_limit=123, pager_page=123)
```

---

### Benchmark Performance data
> Fetch Benchmark Performance for a list of Benchmark IDs

```python
client.analytics.benchmark_performance.create(
    data={
        "benchmarks_ids": [11149, 11150],
        "end_date": "2022-07-31",
        "start_date": "2022-07-01",
    }
)
```

---

### Household Performance data
> Fetch Household Performance for a list of Household IDs

```python
client.analytics.household_performance.create(
    data={"as_of_date": "2022-07-31", "entity_ids": [27585, 28028]}
)
```

---

### Create an Asset Adjustment
> Returns a created Asset Adjustment

```python
client.billing.asset_adjustments.create(
    pager_limit=123,
    pager_page=123,
    data={
        "adjustment_type": "e",
        "firm_id": 39,
        "level": "a",
        "name": "Exclude Apple",
        "slug": "exclude-apple",
        "weight": 100,
    },
)
```

---

### Create Many Asset Adjustments
> Returns the created Asset Adjustment

```python
client.billing.asset_adjustments.create_many.create(
    pager_limit=123,
    pager_page=123,
    data=[
        {
            "adjustment_type": "e",
            "created_at_utc": "1970-01-01T00:00:00",
            "firm_id": 123,
            "id": 123,
            "level": "a",
            "name": "string",
            "security_ids": [123],
            "slug": "string",
            "updated_at_utc": "1970-01-01T00:00:00",
            "weight": 123,
        }
    ],
)
```

---

### Delete many Asset Adjustments
> Returns the "OK" message and a json object with the number of items deleted, if deletion was successful

```python
client.billing.asset_adjustments.delete_many.create(
    pager_limit=123, pager_page=123, data={"ids": [123]}
)
```

---

### Filter all Asset Adjustment
> Returns a filtered list of Asset Adjustment

```python
client.billing.asset_adjustments.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "adjustment_type": "e",
        "firm_id": 39,
        "id": 60,
        "level": "a",
        "name": "Exclude Apple",
        "security_ids": [62],
        "slug": "exclude-apple",
    },
)
```

---

### Create a Fee Structure
> Returns the created  Fee Structure

```python
client.billing.fee_structures.create(
    pager_limit=123,
    pager_page=123,
    data={
        "balance_type": "E",
        "calculation_type": "T",
        "collection_type": "R",
        "created_by_user_id": 123,
        "firm_id": 39,
        "flat_dollar_fee": 123.45,
        "flat_rate": 1,
        "frequency": "Q",
        "name": "Standard Tiered Rate",
        "quarter_cycle": 1,
        "slug": "standard-tiered-rate",
        "tiers": [
            {
                "fee_structure_id": 1290,
                "id": 4249,
                "max_balance": 1000000,
                "min_balance": 0,
                "rate": 0.9,
            },
            {
                "fee_structure_id": 1290,
                "id": 4250,
                "max_balance": None,
                "min_balance": 1000000.01,
                "rate": 0.75,
            },
        ],
    },
)
```

---

### Create Many Fee Structures
> Returns a list of created Fee Structures

```python
client.billing.fee_structures.create_many.create(
    pager_limit=123,
    pager_page=123,
    data=[
        {
            "balance_type": "E",
            "calculation_type": "T",
            "collection_type": "R",
            "created_by_user_id": 123,
            "firm_id": 39,
            "flat_dollar_fee": 123.45,
            "flat_rate": 1,
            "frequency": "Q",
            "name": "Standard Tiered Rate",
            "quarter_cycle": 1,
            "slug": "standard-tiered-rate",
            "tiers": [
                {
                    "fee_structure_id": 1290,
                    "id": 4249,
                    "max_balance": 1000000,
                    "min_balance": 0,
                    "rate": 0.9,
                },
                {
                    "fee_structure_id": 1290,
                    "id": 4250,
                    "max_balance": None,
                    "min_balance": 1000000.01,
                    "rate": 0.75,
                },
            ],
        }
    ],
)
```

---

### Delete Many Fee Structures
> Deletes the records for the provided Fee Structure `ids`
> 

```python
client.billing.fee_structures.delete_many.create(
    pager_limit=123, pager_page=123, data={"ids": [123]}
)
```

---

### Filter all Fee Structures
> Returns a filtered list of Fee Structure

```python
client.billing.fee_structures.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "balance_type": "E",
        "calculation_type": "T",
        "collection_type": "R",
        "created_by_user_id": 123,
        "firm_id": 39,
        "flat_dollar_fee": 123.45,
        "flat_rate": 1,
        "frequency": "Q",
        "id": 1290,
        "name": "Standard Tiered Rate",
        "quarter_cycle": 1,
        "slug": "standard-tiered-rate",
    },
)
```

---

### Download the Fee Upload File
> Returns the fee upload file .zip archive for the specified ID.

```python
client.billing.fee_upload_files.download.create(id=123, pager_limit=123, pager_page=123)
```

---

### Filter all Fee Upload Files
> Returns a filtered list of Fee Upload Files

```python
client.billing.fee_upload_files.filter.create(
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
```

---

### Create a Billing Group
> Returns the created billing group

```python
client.billing.groups.create(
    pager_limit=123,
    pager_page=123,
    data={
        "assignments": [
            {
                "account_id": 230805,
                "fee_location": 0,
                "fee_location_option": "5",
                "group_id": 290599,
                "id": 642504,
            }
        ],
        "firm_id": 39,
        "household_id": 63618,
        "minimum_ids": [123],
        "name": "John Thomas Household",
        "slug": "john-thomas-household",
    },
)
```

---

### Create Billing Groups from Households
> Deletes existing Billing Groups, and recreates for the accounts of each household managed by the firm

```python
client.billing.groups.create_from_households.create(pager_limit=123, pager_page=123)
```

---

### Create Many Billing Groups
> Returns a list of created Billing Groups

```python
client.billing.groups.create_many.create(
    pager_limit=123,
    pager_page=123,
    data=[
        {
            "assignments": [
                {
                    "account_id": 230805,
                    "fee_location": 0,
                    "fee_location_option": "5",
                    "group_id": 290599,
                    "id": 642504,
                }
            ],
            "firm_id": 39,
            "household_id": 63618,
            "minimum_ids": [123],
            "name": "John Thomas Household",
            "slug": "john-thomas-household",
        }
    ],
)
```

---

### Delete Many Billing Groups
> Removes billing group records for the provided `ids`
> 

```python
client.billing.groups.delete_many.create(
    pager_limit=123, pager_page=123, data={"ids": [123]}
)
```

---

### Filter all Billing Groups
> Returns a filtered list of Billing Groups

```python
client.billing.groups.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "firm_id": 39,
        "household_id": 63618,
        "id": 315948,
        "name": "Ezequiel Roberts Household",
        "slug": "ezequiel-roberts-household",
    },
)
```

---

### Remove a Billing Group Assignment
> Delete a single assignment tied to a Billing Group

```python
client.billing.groups.remove_assignment.create(
    pager_limit=123, pager_page=123, data={"group_id": 315948, "id": 703866}
)
```

---

### Bulk Download Billing Invoices
> Starts and returns a bulk download job

```python
client.billing.invoices.download.create(
    pager_limit=123, pager_page=123, data={"ids": [123]}
)
```

---

### Download a PDF Invoice
> Returns the binary data for a specified invoice. This endpoint allows you to download the PDF file corresponding to the provided invoice ID.
> 

```python
client.billing.invoices.download.create_by_id(
    id=123,
    pager_limit=123,
    pager_page=123,
    data={"accept": "string", "content_type": "string"},
)
```

---

### Filter all Invoices
> Returns a filtered list of Invoices

```python
client.billing.invoices.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "annual_debit": 123.45,
        "annual_fee": 123.45,
        "billing_group_id": 123,
        "billing_report_id": 123,
        "custodian_billed_period_debit": 123.45,
        "direct_billed_period_debit": 123.45,
        "due_date": "1970-01-01T00:00:00",
        "firm_id": 123,
        "group_id": 123,
        "id": 123,
        "is_paid": True,
        "n_accounts": 123,
        "n_fee_structures": 123,
        "period_debit": 123.45,
        "snapshot_date": "1970-01-01T00:00:00",
        "total_balance": 123.45,
    },
)
```

---

### Create a Minimum
> Returns the created Minimums

```python
client.billing.minimums.create(
    pager_limit=123,
    pager_page=123,
    data={"firm_id": 39, "name": "Insurance Claim", "value": 2500, "value_type": "F"},
)
```

---

### Create Many Minimums
> Returns a list of created Minimums

```python
client.billing.minimums.create_many.create(
    pager_limit=123,
    pager_page=123,
    data=[{"firm_id": 39, "name": "Insurance Claim", "value": 2500, "value_type": "F"}],
)
```

---

### Delete Many Minimums
> Deletes the corresponding billing minimum records for the provided IDs.

```python
client.billing.minimums.delete_many.create(
    pager_limit=123, pager_page=123, data={"ids": [123]}
)
```

---

### Filter Minimums
> Returns a filtered list of Minimums

```python
client.billing.minimums.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "firm_id": 39,
        "id": 19,
        "name": "Insurance Claim",
        "value": 2500,
        "value_type": "F",
    },
)
```

---

### Start a Billing Job
> Starts a Billing Job with PDF Reporting and returns the created Background Job Instance

```python
client.billing.reports.create(
    pager_limit=123,
    pager_page=123,
    data={
        "billing_date": "2022-08-31",
        "create_invoices": True,
        "email_notification": True,
        "firm_id": 20,
        "group_ids": [123],
        "is_invoice_by_client": True,
        "period_type": "S",
    },
)
```

---

### Delete many Billing Reports
> Deletes the corresponding billing report records for the provided list of `"ids"` in the request body.
> 

```python
client.billing.reports.delete_many.create(
    pager_limit=123, pager_page=123, data={"ids": [123]}
)
```

---

### Filter all Billing Reports
> Returns a filtered list of Billing Reports

```python
client.billing.reports.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "annual_debit": 86748.68,
        "annual_fee": 86748.68,
        "aum_on_billing_date": 8674867.56,
        "billing_date": "2022-09-30T00:00:00Z",
        "created_date": "0001-01-01T00:00:00Z",
        "created_invoices": True,
        "custodian_billed_period_debit": 7229.03,
        "direct_billed_period_debit": 123.45,
        "fee_upload_file_id": 123,
        "firm_id": 39,
        "firm_share": 7229.03,
        "firm_share_annualized": 86748.68,
        "id": 18444,
        "n_accounts": 4,
        "n_fee_structures": 7,
        "n_groups": 1,
        "n_splits": 16,
        "period_debit": 7229.03,
        "run_date": "2022-08-12T00:00:00Z",
        "snapshot_date": "2022-09-30T00:00:00Z",
        "split_payout": 123.45,
        "split_payout_annualized": 123.45,
        "total_balance": 8674867.56,
    },
)
```

---

### Create a Billing Split
> Returns the created Billing Split

```python
client.billing.splits.create(
    pager_limit=123,
    pager_page=123,
    data={
        "firm_id": 39,
        "name": "Advisor #2 Clients",
        "percentage": 10,
        "splitter_name": "Kevin Orick",
        "splitter_slug": "kevin-orick",
    },
)
```

---

### Create Many Billing Splits
> Returns a list of created Billing Splits

```python
client.billing.splits.create_many.create(
    pager_limit=123,
    pager_page=123,
    data=[
        {
            "created_at_utc": "1970-01-01T00:00:00",
            "firm_id": 123,
            "id": 123,
            "name": "string",
            "percentage": 123.45,
            "splitter_name": "string",
            "splitter_slug": "string",
            "updated_at_utc": "1970-01-01T00:00:00",
        }
    ],
)
```

---

### Delete Many Billing Splits
> Delete billing split records for the provided `ids`
> 

```python
client.billing.splits.delete_many.create(
    pager_limit=123, pager_page=123, data={"ids": [123]}
)
```

---

### Filter Billing Splits
> Returns a filtered list of Billing Splits

```python
client.billing.splits.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "firm_id": 39,
        "id": 722,
        "name": "Advisor #1 Clients",
        "percentage": 10,
        "splitter_name": "Kevin Orick",
        "splitter_slug": "kevin-orick",
    },
)
```

---

### Fetch Securities
> Returns a list of securities based on the ids passed in

```python
client.data.custodian.securities.fetch.create(
    pager_limit=123, pager_page=123, data={"ids": [123]}
)
```

---

### Filter all Securities
> Returns a filtered list of Securities

```python
client.data.custodian.securities.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "broad_code": "string",
        "cusip": "string",
        "description": "string",
        "id": 123,
        "issue_code": "string",
        "master_asset_class": "CR",
        "sic_code": "string",
        "symbol_field": "string",
    },
)
```

---

### List all Security Reference Records
> Returns a list of normalized custodian reported securities enriched with Intrinio Market data for a provided `reported_date`
> 
> **Example Records**
> 
> Below is an example of two security records reported by Schwab, the first is a standard `AAPL` stock and below that
> is an AAPL option. Option records will have additional data points populated that provided specific information about
> the option as reported by the custodian.
> 
> ```json
> [
>   {
>     "reported_date": "2024-07-10",
>     "source": "SWB",
>     "cusip": "037833100",
>     "symbol": "AAPL",
>     "description": "APPLE INC ",
>     "security_type": "COM",
>     "security_type_description": "COMMON STOCK",
>     "option_root_symbol": "",
>     "option_expiration_date": "",
>     "option_code": "",
>     "strike_price_amount": 0,
>     "market_data": {
>         "symbol": "AAPL",
>         "description": "Apple Inc",
>         "figi": "BBG000B9Y5X2",
>         "composite_figi": "BBG000B9XRY4",
>         "security_type": "Ordinary Shares",
>         "security_code": "EQS",
>         "security_code_description": "Equity Shares"
>     }
>   },
>   {
>     "reported_date": "2024-07-10",
>     "source": "SWB",
>     "cusip": "",
>     "symbol": "AAPL",
>     "description": "CALL APPLE INC $195        EXP 09/19/25",
>     "security_type": "OEQ",
>     "security_type_description": "EQUITY OPTION",
>     "option_root_symbol": "AAPL",
>     "option_expiration_date": "2025-09-19",
>     "option_code": "C",
>     "strike_price_amount": 195,
>     "market_data": {
>         "symbol": "AAPL",
>         "description": "Apple Inc",
>         "figi": "BBG000B9Y5X2",
>         "composite_figi": "BBG000B9XRY4",
>         "security_type": "Ordinary Shares",
>         "security_code": "EQS",
>         "security_code_description": "Equity Shares"
>     }
>   }
> ]
> ```
> 

```python
client.data.custodian.securities.reference.create(data={"reported_date": "1970-01-01"})
```

---

### Filter all IDC Indexes
> Return a filtered list of all IDC indexes

```python
client.data.idc.indexes.filter.create(
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
```

---

### Filter all account balance records
> Returns a filtered list of account balance records

```python
client.data.source.account_balances.filter.create(
    pager_limit=123,
    pager_page=123,
    related="securities",
    data={
        "account_id": 123,
        "account_ids": [216897, 216898],
        "account_number": "string",
        "advisor_code": "string",
        "cash_value_aggregated": 123.45,
        "cash_value_reported": 123.45,
        "created_at_utc": "1970-01-01T00:00:00",
        "id": 123,
        "original_data": {},
        "reported_date": "1970-01-01T00:00:00",
        "securities_value_aggregated": 123.45,
        "securities_value_reported": 123.45,
        "source": "EGB",
        "total_value_aggregated": 123.45,
        "total_value_reported": 123.45,
    },
)
```

---

### Filter all lot records
> Returns a filtered list of lot records

```python
client.data.source.lots.filter.create(
    pager_limit=123,
    pager_page=123,
    related="securities",
    data={
        "abs_acquisition_quantity": 123.45,
        "abs_adjusted_cost_basis": 123.45,
        "abs_cost_basis": 123.45,
        "abs_current_market_value": 123.45,
        "abs_current_quantity": 123.45,
        "account_id": 123,
        "account_ids": [216897, 216898],
        "account_number": "string",
        "acquisition_date": "1970-01-01T00:00:00",
        "advisor_code": "string",
        "certified": True,
        "created_at_utc": "1970-01-01T00:00:00",
        "direction": "L",
        "disallowed_loss_amount": True,
        "fully_known": True,
        "id": 123,
        "lot_identifier": "string",
        "lot_selection_method": "string",
        "reported_date": "1970-01-01T00:00:00",
        "security_id": 123,
        "source": "DST",
        "source_security_cusip": "string",
        "source_security_symbol": "string",
        "unrealized_gain_loss": 123.45,
        "wash_sale": True,
    },
)
```

---

### Filter all position records
> Returns a filtered list of position records

```python
client.data.source.positions.filter.create(
    pager_limit=123,
    pager_page=123,
    related="securities",
    data={
        "abs_cost_basis": 123.45,
        "abs_settled_units": 123.45,
        "abs_units": 123.45,
        "account_id": 123,
        "account_ids": [216897, 216898],
        "account_number": "string",
        "advisor_code": "string",
        "calculated_unrealized_gain_loss": 123.45,
        "cost_basis_fully_known": True,
        "created_at_utc": "1970-01-01T00:00:00",
        "direction": "S",
        "id": 123,
        "market_value_unit_price": 123.45,
        "reported_date": "1970-01-01T00:00:00",
        "reported_unrealized_gain_loss": 123.45,
        "security_id": 123,
        "source": "SWB",
        "source_security_cusip": "string",
        "source_security_symbol": "string",
    },
)
```

---

### Filter all Realized Gain Loss records
> Returns a filtered list of Realized Gain Loss records

```python
client.data.source.realized_gain_loss.filter.create(
    pager_limit=123,
    pager_page=123,
    related="securities",
    data={
        "abs_closed_units": 123.45,
        "abs_closed_value": 123.45,
        "abs_opened_units": 123.45,
        "abs_opened_value": 123.45,
        "account_id": 123,
        "account_ids": [216897, 216898],
        "account_number": "string",
        "advisor_code": "string",
        "amount": 123.45,
        "amount_long_term": 123.45,
        "amount_short_term": 123.45,
        "close_date": "1970-01-01T00:00:00",
        "created_at_utc": "1970-01-01T00:00:00",
        "direction": "L",
        "id": 123,
        "lot_identifier": "string",
        "lot_selection_method": "string",
        "open_date": "1970-01-01T00:00:00",
        "reported_date": "1970-01-01T00:00:00",
        "security_id": 123,
        "settle_date": "1970-01-01T00:00:00",
        "source": "IBK",
        "source_security_cusip": "string",
        "source_security_symbol": "string",
    },
)
```

---

### Filter all transaction records
> Returns a filtered list of transaction records

```python
client.data.source.transactions.filter.create(
    pager_limit=123,
    pager_page=123,
    related="securities",
    data={
        "account_id": 123,
        "account_ids": [216897, 216898],
        "account_number": "string",
        "category": "crp",
        "classification": "inc",
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
```

---

### Create a Model
> Returns the created model

```python
client.investment_management.models.create(
    pager_limit=123,
    pager_page=123,
    data={
        "firm_id": 39,
        "name": "Fidelity Mixed",
        "strategy_allocations": [
            {"strategy_id": 6, "weight": 20},
            {"strategy_id": 5, "weight": 60},
            {"strategy_id": 3, "weight": 10},
            {"strategy_id": 23, "weight": 10},
        ],
    },
)
```

---

### Delete many Models
> Returns the "OK" message and a json object with the number of items deleted, if deletion was successful

```python
client.investment_management.models.delete_many.create(
    pager_limit=123, pager_page=123, data={"ids": [123]}
)
```

---

### Filter all Models
> Returns a filtered list of Model

```python
client.investment_management.models.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "created_at_utc": "2021-08-18T14:37:26.31346Z",
        "firm_id": 39,
        "id": 2,
        "name": "Fidelity Mixed",
        "updated_at_utc": "2022-06-28T19:24:38.807279Z",
    },
)
```

---

### Create a Strategy
> Returns the created strategy

```python
client.investment_management.strategies.create(
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
```

---

### Create Many Strategies
> Returns a list of created strategies

```python
client.investment_management.strategies.create_many.create(
    pager_limit=123,
    pager_page=123,
    data=[
        {
            "firm_id": 39,
            "name": "Demo Strategy - Fidelity Aggressive Equity",
            "security_allocations": [
                {"security_id": 236, "weight": 80},
                {"security_id": 78, "weight": 20},
            ],
        }
    ],
)
```

---

### Delete many Strategies
> Returns the "OK" message and a json object with the number of items deleted, if deletion was successful

```python
client.investment_management.strategies.delete_many.create(
    pager_limit=123, pager_page=123, data={"ids": [123]}
)
```

---

### Filter all Strategies
> Returns a filtered list of Strategy

```python
client.investment_management.strategies.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "asset_type": "EQ",
        "benchmark_id": 11149,
        "created_at_utc": "2021-08-18T14:27:44.144798Z",
        "description": "This is a model that focuses on capital appreciation.",
        "fee": 1000,
        "firm_id": 39,
        "id": 3,
        "investment_minimum": 100000,
        "name": "Demo Strategy - Fidelity Aggressive Equity",
        "provider": "Fidelity",
        "risk_category": "AG",
        "strategy_type": "Core",
        "tax_managed": False,
        "updated_at_utc": "2021-10-13T11:34:37.614577Z",
    },
)
```

---

### Clear a Job
> Deletes the Background Jobs associated with the user's profile

```python
client.jobs.clear.create(pager_limit=123, pager_page=123)
```

---

### Filter all Jobs
> Return a filtered list of all Jobs

```python
client.jobs.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "created_by_id": 123,
        "created_dt_utc": "1970-01-01T00:00:00",
        "current_step": 123,
        "email_notification": "1970-01-01T00:00:00",
        "email_notification_dt_utc": "1970-01-01T00:00:00",
        "failed_dt_utc": "1970-01-01T00:00:00",
        "finished_dt_utc": "1970-01-01T00:00:00",
        "firm_id": 123,
        "id": 123,
        "is_failed": True,
        "is_finished": True,
        "is_revoked": True,
        "is_running": True,
        "job_type": "b",
        "last_updated_dt_utc": "1970-01-01T00:00:00",
        "num_steps": 123,
        "queued_dt_utc": "1970-01-01T00:00:00",
        "started_dt_utc": "1970-01-01T00:00:00",
    },
)
```

---

### Get an Auth Token
> Exchange your application's `client_id` and `client_secret` for a secure JWT Token. Please note that the encoded `username:password` in the Basic Auth request corresponds to `client_id:client_secret`.

```python
client.oauth2.token_resource.create(data={"grant_type": "client_credentials"})
```

---

### Create an Advisor Code
> Returns the created Advisor Code, if successful.
> 
> **Note for Advisor Code Mapping in Sandbox Applications**
> To preserve the data integrity of sandbox applications, the advisor code mapping endpoints are read-only
> and requests for creation or deletion of advisor codes will not result in updates to advisor code mappings.
> Sandbox applications can read advisor codes from the `/v2/org/advisor-codes` endpoint, but the changes will not
> be reflected upon updates.
> 
> For production applications, full access is granted to the advisor code mapping endpoints. Creations and removals
> of advisor codes will be applied to the advisor codes mapped to the application.
> 

```python
client.org.advisor_codes.create(
    pager_limit=123,
    pager_page=123,
    data={"code_field": "NEWCODE", "firm_id": 39, "source": "APX"},
)
```

---

### Create Multiple Advisor Codes
> Enables the ability create new advisor codes for your application
> 
> **Note for Advisor Code Mapping in Sandbox Applications**
> To preserve the data integrity of sandbox applications, the advisor code mapping endpoints are read-only
> and requests for creation or deletion of advisor codes will not result in updates to advisor code mappings.
> Sandbox applications can read advisor codes from the `/v2/org/advisor-codes` endpoint, but the changes will not
> be reflected upon updates.
> 
> For production applications, full access is granted to the advisor code mapping endpoints. Creations and removals
> of advisor codes will be applied to the advisor codes mapped to the application.
> 

```python
client.org.advisor_codes.create_many.create(
    data=[{"code_field": "NEWCODE", "firm_id": 39, "source": "APX"}]
)
```

---

### Delete multiple Advisor Codes
> Gives the ability to remove multiple advisor codes from your application by providing IDs. The `id`'s provided can be found from resources returned from the `GET /v2/org/advisor-codes` endpoint.
> 
> **Note for Advisor Code Mapping in Sandbox Applications**
> To preserve the data integrity of sandbox applications, the advisor code mapping endpoints are read-only
> and requests for creation or deletion of advisor codes will not result in updates to advisor code mappings.
> Sandbox applications can read advisor codes from the `/v2/org/advisor-codes` endpoint, but the changes will not
> be reflected upon updates.
> 
> For production applications, full access is granted to the advisor code mapping endpoints. Creations and removals
> of advisor codes will be applied to the advisor codes mapped to the application.
> 

```python
client.org.advisor_codes.delete_many.create(data={"ids": [123]})
```

---

### Filter all Firms
> Return a filtered list of all Firms

```python
client.org.firms.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "billing_include_accrued_income": True,
        "billing_partition_option": "M",
        "cp_enabled": True,
        "cp_heldaways_enabled": True,
        "cp_invoices_enabled": True,
        "cp_printable_reports_enabled": True,
        "cp_shared_files_enabled": True,
        "cp_web_reports_enabled": True,
        "disclosures": "string",
        "id": 39,
        "invoice_annualized_effective_rates": False,
        "invoice_due_date_option": "30",
        "invoice_effective_rates": True,
        "invoice_footer": "<p>This is a test Footer message.&nbsp;</p>",
        "invoice_from": "string",
        "invoice_header": "<p>This is a test Header message.</p>",
        "invoice_include_fee_structures": True,
        "invoice_not_a_bill_explanation": True,
        "invoice_show_agreement": True,
        "is_active": True,
        "is_billing_active": False,
        "logo_url": "https://s3.amazonaws.com/com.bridgeft.prod.logos/dem/logo.png",
        "parent_firm_id": 315,
        "relationship_code": "DM0717ILPL",
        "report_on_heldaway_accounts": True,
        "reporting_frequency": "Q",
        "short_name": "dem",
        "show_bridge_logo": True,
        "show_firm_logo": True,
    },
)
```

---

### Send ROI Request to Custodian
> Automatically generates and sends an email to selected Custodian in order to authorize Release of Information between Custodian and BridgeFT.

```python
client.org.roi_requests.send_request.create(
    pager_limit=123,
    pager_page=123,
    data={
        "advisor_codes": [85462, 123456],
        "cc_emails": ["string"],
        "custodian": "MLT",
        "firm_name": "Acme Financial",
        "owner_name": "John Jonson",
        "reply_to_emails": ["string"],
        "sender_name": "Alex Alexen",
    },
)
```

---

### Create an Asset Classification
> Returns the created asset classification

```python
client.reporting.asset_classifications.create(
    pager_limit=123,
    pager_page=123,
    data={
        "class_tag_id": 188,
        "created_by_user_id": 265,
        "firm_id": 39,
        "security_id": 332905,
    },
)
```

---

### Create Many Asset Classifications
> Returns a list of created Asset Classifications

```python
client.reporting.asset_classifications.create_many.create(
    pager_limit=123,
    pager_page=123,
    data=[
        {
            "class_tag_id": 188,
            "created_by_user_id": 265,
            "firm_id": 39,
            "security_id": 332905,
        }
    ],
)
```

---

### Delete many Asset Classifications
> Returns the "OK" message and a json object with the number of items deleted, if deletion was successful

```python
client.reporting.asset_classifications.delete_many.create(
    pager_limit=123, pager_page=123, data={"ids": [123]}
)
```

---

### Filter all Asset Classifications
> Returns a filtered list of Asset Classifications

```python
client.reporting.asset_classifications.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "class_tag_id": 435,
        "created_by_user_id": 265,
        "firm_id": 39,
        "id": 42788,
        "security_id": 322968,
    },
)
```

---

### Create a Benchmark
> Returns the created Benchmark

```python
client.reporting.benchmarks.create(
    pager_limit=123,
    pager_page=123,
    data={"firm_id": 39, "name": "Major Index", "slug": "major-index"},
)
```

---

### Create Many Benchmarks
> Returns a list of created Benchmarks

```python
client.reporting.benchmarks.create_many.create(
    pager_limit=123,
    pager_page=123,
    data=[{"firm_id": 39, "name": "Major Index", "slug": "major-index"}],
)
```

---

### Delete many Benchmarks
> Returns the "OK" message and a json object with the number of items deleted, if deletion was successful

```python
client.reporting.benchmarks.delete_many.create(
    pager_limit=123, pager_page=123, data={"ids": [123]}
)
```

---

### Filter all Benchmarks
> Returns a filtered list of Benchmarks

```python
client.reporting.benchmarks.filter.create(
    pager_limit=123,
    pager_page=123,
    data={"firm_id": 39, "id": 11149, "name": "S&P 500", "slug": "sandp-500"},
)
```

---

### Create a Classification Tag
> Returns the created classification tag

```python
client.reporting.class_tags.create(
    pager_limit=123, pager_page=123, data={"firm_id": 39, "name": "International"}
)
```

---

### Create Many Classification Tags
> Returns a list of created Classification Tags

```python
client.reporting.class_tags.create_many.create(
    pager_limit=123, pager_page=123, data=[{"firm_id": 39, "name": "International"}]
)
```

---

### Delete many Classification Tags
> Returns the "OK" message and a json object with the number of items deleted, if deletion was successful

```python
client.reporting.class_tags.delete_many.create(
    pager_limit=123, pager_page=123, data={"ids": [123]}
)
```

---

### Filter all Classification Tags
> Returns a filtered list of classification tags

```python
client.reporting.class_tags.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "created_dt_utc": "2017-12-27T16:47:11.253166Z",
        "firm_id": 39,
        "id": 180,
        "name": "International",
    },
)
```

---

### Create a Household
> Returns the created Household

```python
client.reporting.households.create(
    pager_limit=123,
    pager_page=123,
    data={"firm_id": 39, "name": "Joe and Rebecca Jones Household"},
)
```

---

### Create Many Households
> Returns a list of created Households

```python
client.reporting.households.create_many.create(
    pager_limit=123,
    pager_page=123,
    data=[
        {"firm_id": 39, "name": "Joe and Rebecca Jones Household"},
        {"firm_id": 39, "name": "Tim Blanco Household"},
    ],
)
```

---

### Filter all Households
> Return a filtered list of all Households

```python
client.reporting.households.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "close_date": "1970-01-01",
        "entity_id": "H-90A44DFF",
        "firm_id": 39,
        "id": 27585,
        "inception_date": "2004-05-14",
        "name": "Rachel and Alex Green-Smith Household",
        "opening_date": "2021-12-31",
        "short_name": "90A44DFF",
        "status": "110",
    },
)
```

---

### Assign Accounts to Households
> Provide a map keyed on string `account_id` with value of the `household` the `account_id` should be mapped to.
> 
> **Example Request Body:**
> 
> ```json
> {
>   "123456": 23,
>   "123457": 23,
>   "123458": 23,
>   "123459": 24,
>   "123460": 24,
>   "123461": 24
> }
> ```
> 
> The above payload would assign account IDs `123456`, `123457`, and `123458` to `household_id` 23. While the following
> accounts are mapped to `household_id` 24.
> 
> **NOTE:** The `/reporting/households/remap` endpoint does not support removing accounts from households, only mapping accounts to specific households
> or assigning an account from one household to another.
> 
> Alternatively, accounts can be assigned/unassigned households by updating the `household_id` on account(s) records directly via `PUT` requests.
> 
> [Update a single account](https://docs.bridgeft.com/reference/readupdatedaccount-1)
> [Update multiple accounts](https://docs.bridgeft.com/reference/readupdatedaccounts-1)
> 

```python
client.reporting.households.remap.create(data={"216895": 77458, "216919": 77458})
```

---

### Start a PDFReport Job
> Starts a Background Job for PDF Reporting and returns the created Background Job Instance
> 
> **Available Sub Reports**
>    - `account_summary`
>    - `allocation_and_performance_summary`
>    - `appraisals`
>    - `appraisals_wo_cost_basis`
>    - `asset_allocation_top_holdings`
>    - `benchmark_perf_summary`
>    - `buy_sells`
>    - `consolidated_summary`
>    - `deposits_withdrawals`
>    - `household_performance_attribution`
>    - `income`
>    - `management_fees`
>    - `net_investment_chart`
>    - `performance_summary`
>    - `performance_chart`
>    - `portfolio_snapshot`
>    - `realized_gain_loss`
>    - `risk_return_chart`
>    - `security_performance`
>    - `target_vs_actual_allocation`
> 

```python
client.reporting.printable_reports.create.create(
    pager_limit=123,
    pager_page=123,
    data={
        "account_ids": [1, 2, 3],
        "end_date": "2022-08-31",
        "exclude_portfolio_performance_summary": True,
        "household_ids": [4, 5, 6],
        "irr_performance": True,
        "non_inception_performance_chart": True,
        "portrait_pdf_orientation": True,
        "start_date": "2022-08-01",
        "sub_reports": [
            "account_summary",
            "consolidated_summary",
            "performance_summary",
        ],
    },
)
```

---

### Delete many Printable Reports
> Returns the "OK" message and a json object with the number of items deleted, if deletion was successful

```python
client.reporting.printable_reports.delete_many.create(
    pager_limit=123, pager_page=123, data={"ids": [123]}
)
```

---

### Bulk Download Printable PDFs
> Starts and returns a bulk download job

```python
client.reporting.printable_reports.download.create(
    pager_limit=123, pager_page=123, data={"ids": [123]}
)
```

---

### Download a Printable Report
> Returns the PDF for the provided printable report ID.

```python
client.reporting.printable_reports.download.create_by_id(
    id=123,
    pager_limit=123,
    pager_page=123,
    data={"accept": "string", "content_type": "string"},
)
```

---

### Filter all Printable Reports
> Returns a filtered list of Printable Reports

```python
client.reporting.printable_reports.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "account_id": 123,
        "client_accessible": False,
        "created_by_user_id": 8882,
        "dt_utc": "0001-01-01T00:00:00Z",
        "end_date": "2022-08-31",
        "error_message": "string",
        "firm_id": 39,
        "frequency": "string",
        "household_id": 27585,
        "id": 1290371,
        "report_date": "2022-08-31",
        "size_bytes": 115805,
        "start_date": "2022-08-01",
        "state": "0",
        "timestamp_utc": 1660575976,
    },
)
```

---

### Filter all Report Settings
> Returns a filtered list of Report Settings

```python
client.reporting.report_settings.filter.create(
    pager_limit=123,
    pager_page=123,
    data={
        "account_summary": True,
        "appraisals": True,
        "asset_allocation_top_holdings": True,
        "benchmark_perf_summary": True,
        "buy_sells": True,
        "component": "advisor_defaults",
        "consolidated_summary": True,
        "deposits_withdrawals": True,
        "firm_id": 39,
        "id": 95,
        "income": True,
        "management_fees": True,
        "net_investment_chart": True,
        "performance_chart": True,
        "performance_summary": True,
        "portfolio_snapshot": False,
        "realized_gain_loss": True,
        "user_id": 123,
    },
)
```

---

### Create a Target Allocation
> Returns the created Target Allocation

```python
client.reporting.target_allocations.create(
    pager_limit=123,
    pager_page=123,
    data={
        "coefficients": [
            {
                "class_tag_id": None,
                "mac": "EQ",
                "negative_tolerance": 5,
                "positive_tolerance": 5,
                "weight": 40,
            },
            {
                "class_tag_id": None,
                "mac": "DT",
                "negative_tolerance": 5,
                "positive_tolerance": 5,
                "weight": 50,
            },
        ],
        "firm_id": 39,
        "name": "Conservative",
        "slug": "conservative",
    },
)
```

---

### Create Many Target Allocations
> Returns a list of created Target Allocations

```python
client.reporting.target_allocations.create_many.create(
    pager_limit=123,
    pager_page=123,
    data=[
        {
            "coefficients": [
                {
                    "class_tag_id": None,
                    "mac": "EQ",
                    "negative_tolerance": 5,
                    "positive_tolerance": 5,
                    "weight": 40,
                },
                {
                    "class_tag_id": None,
                    "mac": "DT",
                    "negative_tolerance": 5,
                    "positive_tolerance": 5,
                    "weight": 50,
                },
            ],
            "firm_id": 39,
            "name": "Conservative",
            "slug": "conservative",
        }
    ],
)
```

---

### Delete many Target Allocations
> Returns the "OK" message and a json object with the number of items deleted, if deletion was successful

```python
client.reporting.target_allocations.delete_many.create(
    pager_limit=123, pager_page=123, data={"ids": [123]}
)
```

---

### Filter all Target Allocations
> Returns a filtered list of Target Allocations

```python
client.reporting.target_allocations.filter.create(
    pager_limit=123,
    pager_page=123,
    data={"firm_id": 39, "id": 1, "name": "Conservative", "slug": "conservative"},
)
```

---

### Run a web report
> Runs a web report and returns the reporting output synchronously
> 
> **Available Sub Reports**
> - `account_summary`
> - `allocation_and_performance_summary`
> - `appraisals`
> - `appraisals_wo_cost_basis`
> - `asset_allocation_top_holdings`
> - `benchmark_perf_summary`
> - `buy_sells`
> - `consolidated_summary`
> - `deposits_withdrawals`
> - `household_performance_attribution`
> - `income`
> - `management_fees`
> - `net_investment_chart`
> - `performance_summary`
> - `performance_chart`
> - `portfolio_snapshot`
> - `realized_gain_loss`
> - `risk_return_chart`
> - `security_performance`
> - `target_vs_actual_allocation`
> 

```python
client.reporting.web_reports.create(
    data={
        "account_id": 123,
        "end": "2022-08-31",
        "firm_id": 123,
        "household_id": 123,
        "irr_performance": False,
        "start": "2022-08-01",
        "sub_reports": [
            "account_summary",
            "consolidated_summary",
            "performance_summary",
        ],
    }
)
```

---

### Source Data Status
> Status of source data ingestion. TDA availability status is applicable prior to Sept. 2, 2023.

```python
client.status.source_data.create(data={"as_of_date": "2006-01-02"})
```

---

### Update Accounts
> Provide a list of accounts to update. Then entire account object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `benchmarks_ids`
> - `fee_structures_ids`
> - `billing_splits_ids`
> - `notes`
> - `nickname`
> - `household_id` To remove an account from a household, provide `null` in this field.
> - `target_allocation_id`
> - `first_performance_date`
> - `payment_source`
> - `first_billable_date`
> - `investment_model_id`
> - `required_cash`
> - `unsupervised_securities_ids`
> - `buy_securities_ids`
> - `sell_securities_ids`
> - `do_not_buy_securities_ids`
> - `do_not_sell_securities_ids`
> - `required_cash_frequency`
> 

```python
client.account_management.accounts.put(
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
            "payment_source": "D",
            "required_cash": 123.45,
            "required_cash_frequency": "Q",
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
```

---

### Update an Account
> Provide an account to update. Then entire account object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `benchmark_ids`
> - `fee_structure_ids`
> - `billing_split_ids`
> - `notes`
> - `nickname`
> - `household_id` To remove an account from a household, provide `null` in this field.
> - `target_allocation_id`
> - `first_performance_date`
> - `payment_source`
> - `first_billable_date`
> - `investment_model_id`
> - `required_cash`
> - `unsupervised_securities_ids`
> - `buy_securities_ids`
> - `sell_securities_ids`
> - `do_not_buy_securities_ids`
> - `do_not_sell_securities_ids`
> - `required_cash_frequency`
> 

```python
client.account_management.accounts.put_by_id(
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
        "custodian": "FPR",
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
        "required_cash_frequency": "M",
        "sell_securities_ids": [123],
        "short_name": "string",
        "state": "string",
        "status": "stale",
        "target_allocation_id": 123,
        "tax_id_token": "string",
        "unsupervised_securities_ids": [123],
        "updated_at_utc": "1970-01-01T00:00:00",
        "zip_code": "string",
    },
)
```

---

### Bulk Update Asset Adjustments
> Provide a list of asset adjustments to update. Then entire asset adjustment object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `adjustment_type`
> - `level`
> - `security_ids`
> - `weight`
> 

```python
client.billing.asset_adjustments.put(
    data=[
        {
            "adjustment_type": "i",
            "created_at_utc": "1970-01-01T00:00:00",
            "firm_id": 123,
            "id": 123,
            "level": "a",
            "name": "string",
            "security_ids": [123],
            "slug": "string",
            "updated_at_utc": "1970-01-01T00:00:00",
            "weight": 123,
        }
    ]
)
```

---

### Update an Asset Adjustment
> Provide an asset adjustment to update. Then entire asset adjustment object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `adjustment_type`
> - `level`
> - `security_ids`
> - `weight`
> 

```python
client.billing.asset_adjustments.put_by_id(
    id=123,
    data={
        "adjustment_type": "i",
        "created_at_utc": "1970-01-01T00:00:00",
        "firm_id": 123,
        "id": 123,
        "level": "f",
        "name": "string",
        "security_ids": [123],
        "slug": "string",
        "updated_at_utc": "1970-01-01T00:00:00",
        "weight": 123,
    },
)
```

---

### Bulk Update Fee Structures
> Provide a list of fee structures to update. Then entire fee structure object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `calculation_type`
> - `collection_type`
> - `frequency`
> - `quarter_cycle`
> - `balance_type`
> - `flat_rate`
> - `flat_dollar_fee`
> - `semi_annual_cycle`
> - `annual_cycle`
> - `tiers`
> 

```python
client.billing.fee_structures.put(
    data=[
        {
            "balance_type": "A",
            "calculation_type": "string",
            "collection_type": "G",
            "created_at_utc": "1970-01-01T00:00:00",
            "created_by_user_id": 123,
            "firm_id": 123,
            "flat_dollar_fee": 123.45,
            "flat_rate": 123.45,
            "frequency": "M",
            "id": 123,
            "name": "string",
            "quarter_cycle": 123,
            "slug": "string",
            "tiers": [
                {
                    "fee_structure_id": 123,
                    "id": 123,
                    "max_balance": 123.45,
                    "min_balance": 123.45,
                    "rate": 123.45,
                }
            ],
            "updated_at_utc": "1970-01-01T00:00:00",
        }
    ]
)
```

---

### Update a Fee Structure
> Provide a fee structure to update. Then entire fee structure object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `calculation_type`
> - `collection_type`
> - `frequency`
> - `quarter_cycle`
> - `balance_type`
> - `flat_rate`
> - `flat_dollar_fee`
> - `semi_annual_cycle`
> - `annual_cycle`
> - `tiers`
> 

```python
client.billing.fee_structures.put_by_id(
    id=123,
    data={
        "balance_type": "E",
        "calculation_type": "string",
        "collection_type": "A",
        "created_at_utc": "1970-01-01T00:00:00",
        "created_by_user_id": 123,
        "firm_id": 123,
        "flat_dollar_fee": 123.45,
        "flat_rate": 123.45,
        "frequency": "Q",
        "id": 123,
        "name": "string",
        "quarter_cycle": 123,
        "slug": "string",
        "tiers": [
            {
                "fee_structure_id": 123,
                "id": 123,
                "max_balance": 123.45,
                "min_balance": 123.45,
                "rate": 123.45,
            }
        ],
        "updated_at_utc": "1970-01-01T00:00:00",
    },
)
```

---

### Bulk Update Billing Groups
> Provide a list of billing groups to update. Then entire billing group object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `minimum_ids`
> - `household_id`
> - `assignments`
> 

```python
client.billing.groups.put(
    data=[
        {
            "assignments": {
                "account_id": 123,
                "fee_location": 123,
                "fee_location_option": "S",
                "group_id": 123,
                "id": 123,
            },
            "created_at_utc": "1970-01-01T00:00:00",
            "firm_id": 123,
            "household_id": 123,
            "id": 123,
            "minimum_ids": [123],
            "name": "string",
            "slug": "string",
            "updated_at_utc": "1970-01-01T00:00:00",
        }
    ]
)
```

---

### Update a Billing Group
> Provide a billing group to update. Then entire billing group object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `minimum_ids`
> - `household_id`
> - `assignments`
> 

```python
client.billing.groups.put_by_id(
    id=123,
    data={
        "assignments": {
            "account_id": 123,
            "fee_location": 123,
            "fee_location_option": "A",
            "group_id": 123,
            "id": 123,
        },
        "created_at_utc": "1970-01-01T00:00:00",
        "firm_id": 123,
        "household_id": 123,
        "id": 123,
        "minimum_ids": [123],
        "name": "string",
        "slug": "string",
        "updated_at_utc": "1970-01-01T00:00:00",
    },
)
```

---

### Bulk Update Minimums
> Provide a list of billing minimums to update. Then entire billing minimum object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `value`
> - `value_type`
> 

```python
client.billing.minimums.put(
    data=[
        {
            "created_at_utc": "1970-01-01T00:00:00",
            "firm_id": 123,
            "id": 123,
            "name": "string",
            "updated_at_utc": "1970-01-01T00:00:00",
            "value": 123.45,
            "value_type": "F",
        }
    ]
)
```

---

### Update a Minimum
> Provide a billing minimum to update. Then entire billing minimum object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `value`
> - `value_type`
> 

```python
client.billing.minimums.put_by_id(
    id=123,
    data={
        "created_at_utc": "1970-01-01T00:00:00",
        "firm_id": 123,
        "id": 123,
        "name": "string",
        "updated_at_utc": "1970-01-01T00:00:00",
        "value": 123.45,
        "value_type": "F",
    },
)
```

---

### Bulk Update Billing Splits
> Provide a list billing splits to update. Then entire billing split object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `percentage`
> - `splitter_name`
> 

```python
client.billing.splits.put(
    data=[
        {
            "created_at_utc": "1970-01-01T00:00:00",
            "firm_id": 123,
            "id": 123,
            "name": "string",
            "percentage": 123.45,
            "splitter_name": "string",
            "splitter_slug": "string",
            "updated_at_utc": "1970-01-01T00:00:00",
        }
    ]
)
```

---

### Update a Billing Split
> Provide a billing split to update. Then entire billing split object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `percentage`
> - `splitter_name`
> 

```python
client.billing.splits.put_by_id(
    id=123,
    data={
        "created_at_utc": "1970-01-01T00:00:00",
        "firm_id": 123,
        "id": 123,
        "name": "string",
        "percentage": 123.45,
        "splitter_name": "string",
        "splitter_slug": "string",
        "updated_at_utc": "1970-01-01T00:00:00",
    },
)
```

---

### Bulk Update Models
> Provide a list of Investment Models update. Then entire Investment Model object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `strategy_allocations`
> 

```python
client.investment_management.models.put(
    data=[
        {
            "created_at_utc": "1970-01-01T00:00:00",
            "firm_id": 123,
            "id": 123,
            "name": "string",
            "strategy_allocations": [
                {"id": 123, "model_id": 123, "strategy_id": 123, "weight": 123.45}
            ],
            "updated_at_utc": "1970-01-01T00:00:00",
        }
    ]
)
```

---

### Update a Model
> Provide an Investment Model update. Then entire Investment Model object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `strategy_allocations`
> 

```python
client.investment_management.models.put_by_id(
    id=123,
    data={
        "created_at_utc": "1970-01-01T00:00:00",
        "firm_id": 123,
        "id": 123,
        "name": "string",
        "strategy_allocations": [
            {"id": 123, "model_id": 123, "strategy_id": 123, "weight": 123.45}
        ],
        "updated_at_utc": "1970-01-01T00:00:00",
    },
)
```

---

### Bulk Update Strategies
> Provide a list of Investment Strategies to update. Then entire Investment Strategy object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `description`
> - `provider`
> - `investment_minimum`
> - `fee`
> - `security_allocations`
> 

```python
client.investment_management.strategies.put(
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
            "risk_category": "CO",
            "search_tags": ["string"],
            "security_allocations": [
                {"id": 123, "security_id": 123, "strategy_id": 123, "weight": 123.45}
            ],
            "strategy_type": "Core",
            "tax_managed": True,
            "updated_at_utc": "1970-01-01T00:00:00",
        }
    ]
)
```

---

### Update a Strategy
> Provide an Investment Strategy update. Then entire Investment Strategy object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `description`
> - `provider`
> - `investment_minimum`
> - `fee`
> - `security_allocations`
> 

```python
client.investment_management.strategies.put_by_id(
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
        "risk_category": "CP",
        "search_tags": ["string"],
        "security_allocations": [
            {"id": 123, "security_id": 123, "strategy_id": 123, "weight": 123.45}
        ],
        "strategy_type": "Core",
        "tax_managed": True,
        "updated_at_utc": "1970-01-01T00:00:00",
    },
)
```

---

### Update a Firm
> Provide an firm object update. Then entire firm object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `disclosures`
> - `reporting_frequency`
> - `invoice_header`
> - `invoice_footer`
> - `invoice_from`
> - `invoice_due_date_option`
> - `invoice_include_fee_structures`
> - `invoice_effective_rates`
> - `invoice_annualized_effective_rates`
> - `invoice_show_agreement`
> - `invoice_not_a_bill_explanation`
> - `billing_partition_option`
> - `billing_include_accrued_income`
> 

```python
client.org.firms.put(
    id=123,
    data={
        "accent_color": "string",
        "billing_include_accrued_income": True,
        "billing_partition_option": "Y",
        "brand_colors": ["string"],
        "cp_enabled": True,
        "cp_heldaways_enabled": True,
        "cp_invoices_enabled": True,
        "cp_printable_reports_enabled": True,
        "cp_shared_files_enabled": True,
        "cp_web_reports_enabled": True,
        "created_at_utc": "1970-01-01T00:00:00",
        "disclosures": "string",
        "id": 123,
        "invoice_annualized_effective_rates": True,
        "invoice_due_date_option": "30",
        "invoice_effective_rates": True,
        "invoice_footer": "string",
        "invoice_from": "string",
        "invoice_header": "string",
        "invoice_include_fee_structures": True,
        "invoice_not_a_bill_explanation": True,
        "invoice_show_agreement": True,
        "is_active": True,
        "is_billing_active": True,
        "logo_url": "string",
        "name": "string",
        "parent_firm_id": 123,
        "permissions": ["string"],
        "primary_color": "string",
        "relationship_code": "string",
        "report_on_heldaway_accounts": True,
        "reporting_frequency": "Y",
        "short_name": "string",
        "show_bridge_logo": True,
        "show_firm_logo": True,
        "updated_at_utc": "1970-01-01T00:00:00",
    },
)
```

---

### Bulk Update Asset Classifications
> Provide a list Asset Classifications to update. Then entire Asset Classification object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `security_id`
> - `class_tag_id`
> 

```python
client.reporting.asset_classifications.put(
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
```

---

### Update an Asset Classification
> Provide an Asset Classification to update. Then entire Asset Classification object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `security_id`
> - `class_tag_id`
> 

```python
client.reporting.asset_classifications.put_by_id(
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
```

---

### Bulk Update Benchmarks
> Provide a list of Benchmarks to update. Then entire Benchmark object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `coefficients`
> 

```python
client.reporting.benchmarks.put(
    data=[
        {
            "coefficients": {
                "benchmark_id": 123,
                "id": 123,
                "index_id": 123,
                "weight": "string",
            },
            "created_at_utc": "1970-01-01T00:00:00",
            "firm_id": 123,
            "id": 123,
            "name": "string",
            "slug": "string",
            "updated_at_utc": "1970-01-01T00:00:00",
        }
    ]
)
```

---

### Update a Benchmark
> Provide a Benchmark to update. Then entire Benchmark object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `coefficients`
> 

```python
client.reporting.benchmarks.put_by_id(
    id=123,
    data={
        "coefficients": {
            "benchmark_id": 123,
            "id": 123,
            "index_id": 123,
            "weight": "string",
        },
        "created_at_utc": "1970-01-01T00:00:00",
        "firm_id": 123,
        "id": 123,
        "name": "string",
        "slug": "string",
        "updated_at_utc": "1970-01-01T00:00:00",
    },
)
```

---

### Bulk Update Classification Tags
> Provide a list of Classification Tags to update. Then entire Classification Tag object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> 

```python
client.reporting.class_tags.put(
    data=[
        {
            "created_at_utc": "1970-01-01T00:00:00",
            "created_dt_utc": "1970-01-01T00:00:00",
            "firm_id": 123,
            "id": 123,
            "name": "string",
            "updated_at_utc": "1970-01-01T00:00:00",
        }
    ]
)
```

---

### Update a Classification Tag
> Provide a Classification Tag to update. The entire Classification Tag object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> 

```python
client.reporting.class_tags.put_by_id(
    id=123,
    data={
        "created_at_utc": "1970-01-01T00:00:00",
        "created_dt_utc": "1970-01-01T00:00:00",
        "firm_id": 123,
        "id": 123,
        "name": "string",
        "updated_at_utc": "1970-01-01T00:00:00",
    },
)
```

---

### Update Households
> Provide a list of Households to update. Then entire Household object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `benchmarks_ids`
> 

```python
client.reporting.households.put(
    data=[
        {
            "benchmarks_ids": [123],
            "close_date": "1970-01-01T00:00:00",
            "created_at_utc": "1970-01-01T00:00:00",
            "entity_id": "string",
            "firm_id": 123,
            "first_account_reporting_date": "1970-01-01T00:00:00",
            "id": 123,
            "inception_date": "1970-01-01T00:00:00",
            "is_account": True,
            "is_household": True,
            "last_account_reporting_date": "1970-01-01T00:00:00",
            "last_reporting_date": "1970-01-01T00:00:00",
            "name": "string",
            "opening_date": "1970-01-01T00:00:00",
            "short_name": "string",
            "status": "string",
            "updated_at_utc": "1970-01-01T00:00:00",
        }
    ]
)
```

---

### Update a Household
> Provide a Household to update. Then entire Household object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `benchmarks_ids`
> 

```python
client.reporting.households.put_by_id(
    id=123,
    data={
        "benchmarks_ids": [123],
        "close_date": "1970-01-01T00:00:00",
        "created_at_utc": "1970-01-01T00:00:00",
        "entity_id": "string",
        "firm_id": 123,
        "first_account_reporting_date": "1970-01-01T00:00:00",
        "id": 123,
        "inception_date": "1970-01-01T00:00:00",
        "is_account": True,
        "is_household": True,
        "last_account_reporting_date": "1970-01-01T00:00:00",
        "last_reporting_date": "1970-01-01T00:00:00",
        "name": "string",
        "opening_date": "1970-01-01T00:00:00",
        "short_name": "string",
        "status": "string",
        "updated_at_utc": "1970-01-01T00:00:00",
    },
)
```

---

### Bulk Update Report Settings
> Returns the updated Report Settings

```python
client.reporting.report_settings.put(pager_limit=123, pager_page=123)
```

---

### Update Report Settings
> Returns the updated Report Settings

```python
client.reporting.report_settings.put_by_id(id=123, pager_limit=123, pager_page=123)
```

---

### Bulk Update Target Allocations
> Provide a list of Target Allocations to update. Then entire Target Allocation object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `coefficients`
> 

```python
client.reporting.target_allocations.put(
    data=[
        {
            "coefficients": [
                {
                    "class_tag_id": 123,
                    "id": 123,
                    "mac": 123,
                    "negative_tolerance": 123.45,
                    "positive_tolerance": 123.45,
                    "weight": 123.45,
                }
            ],
            "created_at_utc": "1970-01-01T00:00:00",
            "firm_id": 123,
            "id": 123,
            "name": 123,
            "slug": "string",
            "updated_at_utc": "1970-01-01T00:00:00",
        }
    ]
)
```

---

### Update a Target Allocation
> Provide a Target Allocation to update. Then entire Target Allocation object **must** be provided to the `PUT` request.
> 
> **Editable Fields:**
> - `name`
> - `coefficients`
> 

```python
client.reporting.target_allocations.put_by_id(
    id=123,
    data={
        "coefficients": [
            {
                "class_tag_id": 123,
                "id": 123,
                "mac": 123,
                "negative_tolerance": 123.45,
                "positive_tolerance": 123.45,
                "weight": 123.45,
            }
        ],
        "created_at_utc": "1970-01-01T00:00:00",
        "firm_id": 123,
        "id": 123,
        "name": 123,
        "slug": "string",
        "updated_at_utc": "1970-01-01T00:00:00",
    },
)
```


