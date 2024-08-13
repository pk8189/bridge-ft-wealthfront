"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import SyncBaseClient, AsyncBaseClient
from wealthtech_api.resources.status.account_summary import (
    AccountSummaryClient,
    AsyncAccountSummaryClient,
)
from wealthtech_api.resources.status.source_data import (
    AsyncSourceDataClient,
    SourceDataClient,
)


class StatusClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.account_summary = AccountSummaryClient(base_client=self._base_client)
        self.source_data = SourceDataClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncStatusClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.account_summary = AsyncAccountSummaryClient(base_client=self._base_client)
        self.source_data = AsyncSourceDataClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
