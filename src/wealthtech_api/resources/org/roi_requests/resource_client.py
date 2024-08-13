"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import SyncBaseClient, AsyncBaseClient
from wealthtech_api.resources.org.roi_requests.send_request import (
    SendRequestClient,
    AsyncSendRequestClient,
)


class RoiRequestsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.send_request = SendRequestClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncRoiRequestsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.send_request = AsyncSendRequestClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)