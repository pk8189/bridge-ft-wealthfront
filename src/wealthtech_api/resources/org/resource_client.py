"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import AsyncBaseClient, SyncBaseClient
from wealthtech_api.resources.org.advisor_codes import (
    AsyncAdvisorCodesClient,
    AdvisorCodesClient,
)
from wealthtech_api.resources.org.firms import AsyncFirmsClient, FirmsClient
from wealthtech_api.resources.org.roi_requests import (
    AsyncRoiRequestsClient,
    RoiRequestsClient,
)


class OrgClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.advisor_codes = AdvisorCodesClient(base_client=self._base_client)
        self.firms = FirmsClient(base_client=self._base_client)
        self.roi_requests = RoiRequestsClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncOrgClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.advisor_codes = AsyncAdvisorCodesClient(base_client=self._base_client)
        self.firms = AsyncFirmsClient(base_client=self._base_client)
        self.roi_requests = AsyncRoiRequestsClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
