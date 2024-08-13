"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    SyncBaseClient,
    encode_param,
    RequestOptions,
    QueryParams,
    default_request_options,
    AsyncBaseClient,
    to_encodable,
)
from wealthtech_api.resources.reporting.households.create_many import (
    CreateManyClient,
    AsyncCreateManyClient,
)
from wealthtech_api.resources.reporting.households.filter import (
    FilterClient,
    AsyncFilterClient,
)
from wealthtech_api.resources.reporting.households.remap import (
    AsyncRemapClient,
    RemapClient,
)
import typing
from wealthtech_api.types.reporting.households import params, models


class HouseholdsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.create_many = CreateManyClient(base_client=self._base_client)
        self.filter = FilterClient(base_client=self._base_client)
        self.remap = RemapClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def put_by_id(
        self,
        *,
        data: params.Household,
        id: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PutReportingHouseholdsIdResponse:
        """
        Provide a Household to update. Then entire Household object **must** be provided to the `PUT` request.

        **Editable Fields:**
        - `name`
        - `benchmarks_ids`

        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerHousehold)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PUT",
            path=f"/reporting/households/{id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PutReportingHouseholdsIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def put(
        self,
        *,
        data: typing.List[params.Household],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PutReportingHouseholdsResponse:
        """
        Provide a list of Households to update. Then entire Household object **must** be provided to the `PUT` request.

        **Editable Fields:**
        - `name`
        - `benchmarks_ids`

        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=typing.List[params._SerializerHousehold]
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PUT",
            path="/reporting/households",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PutReportingHouseholdsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def create(
        self,
        *,
        data: params.PostReportingHouseholdsBody,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostReportingHouseholdsResponse:
        """
        Returns the created Household
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostReportingHouseholdsBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/reporting/households",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.PostReportingHouseholdsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: int,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetReportingHouseholdsIdResponse:
        """
        Returns a household based on a single ID
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/reporting/households/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetReportingHouseholdsIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetReportingHouseholdsResponse:
        """
        Returns a list of households within the data field
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path="/reporting/households",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetReportingHouseholdsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncHouseholdsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.create_many = AsyncCreateManyClient(base_client=self._base_client)
        self.filter = AsyncFilterClient(base_client=self._base_client)
        self.remap = AsyncRemapClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def put_by_id(
        self,
        *,
        data: params.Household,
        id: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PutReportingHouseholdsIdResponse:
        """
        Provide a Household to update. Then entire Household object **must** be provided to the `PUT` request.

        **Editable Fields:**
        - `name`
        - `benchmarks_ids`

        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerHousehold)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PUT",
            path=f"/reporting/households/{id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PutReportingHouseholdsIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def put(
        self,
        *,
        data: typing.List[params.Household],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PutReportingHouseholdsResponse:
        """
        Provide a list of Households to update. Then entire Household object **must** be provided to the `PUT` request.

        **Editable Fields:**
        - `name`
        - `benchmarks_ids`

        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=typing.List[params._SerializerHousehold]
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PUT",
            path="/reporting/households",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PutReportingHouseholdsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def create(
        self,
        *,
        data: params.PostReportingHouseholdsBody,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostReportingHouseholdsResponse:
        """
        Returns the created Household
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostReportingHouseholdsBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/reporting/households",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.PostReportingHouseholdsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: int,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetReportingHouseholdsIdResponse:
        """
        Returns a household based on a single ID
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/reporting/households/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetReportingHouseholdsIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetReportingHouseholdsResponse:
        """
        Returns a list of households within the data field
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path="/reporting/households",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetReportingHouseholdsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
