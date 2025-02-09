"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import AsyncBaseClient, SyncBaseClient
from wealthtech_api.resources.data.custodian.securities import (
    SecuritiesClient,
    AsyncSecuritiesClient,
)


class CustodianClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.securities = SecuritiesClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncCustodianClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.securities = AsyncSecuritiesClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
