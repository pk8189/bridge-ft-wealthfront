"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import SyncBaseClient, AsyncBaseClient
from wealthtech_api.resources.data.source.account_balances import (
    AccountBalancesClient,
    AsyncAccountBalancesClient,
)
from wealthtech_api.resources.data.source.lots import LotsClient, AsyncLotsClient
from wealthtech_api.resources.data.source.positions import (
    AsyncPositionsClient,
    PositionsClient,
)
from wealthtech_api.resources.data.source.realized_gain_loss import (
    AsyncRealizedGainLossClient,
    RealizedGainLossClient,
)
from wealthtech_api.resources.data.source.transactions import (
    TransactionsClient,
    AsyncTransactionsClient,
)


class SourceClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.account_balances = AccountBalancesClient(base_client=self._base_client)
        self.lots = LotsClient(base_client=self._base_client)
        self.positions = PositionsClient(base_client=self._base_client)
        self.realized_gain_loss = RealizedGainLossClient(base_client=self._base_client)
        self.transactions = TransactionsClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncSourceClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.account_balances = AsyncAccountBalancesClient(
            base_client=self._base_client
        )
        self.lots = AsyncLotsClient(base_client=self._base_client)
        self.positions = AsyncPositionsClient(base_client=self._base_client)
        self.realized_gain_loss = AsyncRealizedGainLossClient(
            base_client=self._base_client
        )
        self.transactions = AsyncTransactionsClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)