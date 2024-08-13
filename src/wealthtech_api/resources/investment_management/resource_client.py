"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import AsyncBaseClient, SyncBaseClient
from wealthtech_api.resources.investment_management.models import (
    ModelsClient,
    AsyncModelsClient,
)
from wealthtech_api.resources.investment_management.strategies import (
    AsyncStrategiesClient,
    StrategiesClient,
)


class InvestmentManagementClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.models = ModelsClient(base_client=self._base_client)
        self.strategies = StrategiesClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncInvestmentManagementClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.models = AsyncModelsClient(base_client=self._base_client)
        self.strategies = AsyncStrategiesClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
