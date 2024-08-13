"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    RequestOptions,
    AsyncBaseClient,
    QueryParams,
    default_request_options,
    to_encodable,
    SyncBaseClient,
    encode_param,
)
from wealthtech_api.resources.reporting.benchmarks.create_many import (
    AsyncCreateManyClient,
    CreateManyClient,
)
from wealthtech_api.resources.reporting.benchmarks.delete_many import (
    AsyncDeleteManyClient,
    DeleteManyClient,
)
from wealthtech_api.resources.reporting.benchmarks.filter import (
    AsyncFilterClient,
    FilterClient,
)
import typing
from wealthtech_api.types.reporting.benchmarks import models, params


class BenchmarksClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.create_many = CreateManyClient(base_client=self._base_client)
        self.delete_many = DeleteManyClient(base_client=self._base_client)
        self.filter = FilterClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def put_by_id(
        self,
        *,
        data: params.Benchmark,
        id: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PutReportingBenchmarksIdResponse:
        """
        Provide a Benchmark to update. Then entire Benchmark object **must** be provided to the `PUT` request.

        **Editable Fields:**
        - `name`
        - `coefficients`

        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerBenchmark)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PUT",
            path=f"/reporting/benchmarks/{id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PutReportingBenchmarksIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def put(
        self,
        *,
        data: typing.List[params.Benchmark],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PutReportingBenchmarksResponse:
        """
        Provide a list of Benchmarks to update. Then entire Benchmark object **must** be provided to the `PUT` request.

        **Editable Fields:**
        - `name`
        - `coefficients`

        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=typing.List[params._SerializerBenchmark]
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PUT",
            path="/reporting/benchmarks",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PutReportingBenchmarksResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def create(
        self,
        *,
        data: params.PostReportingBenchmarksBody,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostReportingBenchmarksResponse:
        """
        Returns the created Benchmark
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostReportingBenchmarksBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/reporting/benchmarks",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.PostReportingBenchmarksResponse,
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
    ) -> models.GetReportingBenchmarksIdResponse:
        """
        Returns a Benchmark based on a single ID
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
            path=f"/reporting/benchmarks/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetReportingBenchmarksIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetReportingBenchmarksResponse:
        """
        Returns a list of Benchmarks within the data field
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
            path="/reporting/benchmarks",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetReportingBenchmarksResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def delete(
        self,
        *,
        id: int,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Delete:
        """
        Returns the "OK" message and a json object with the id  of item deleted, if deletion was successful
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
            method="DELETE",
            path=f"/reporting/benchmarks/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Delete,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncBenchmarksClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.create_many = AsyncCreateManyClient(base_client=self._base_client)
        self.delete_many = AsyncDeleteManyClient(base_client=self._base_client)
        self.filter = AsyncFilterClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def put_by_id(
        self,
        *,
        data: params.Benchmark,
        id: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PutReportingBenchmarksIdResponse:
        """
        Provide a Benchmark to update. Then entire Benchmark object **must** be provided to the `PUT` request.

        **Editable Fields:**
        - `name`
        - `coefficients`

        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerBenchmark)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PUT",
            path=f"/reporting/benchmarks/{id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PutReportingBenchmarksIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def put(
        self,
        *,
        data: typing.List[params.Benchmark],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PutReportingBenchmarksResponse:
        """
        Provide a list of Benchmarks to update. Then entire Benchmark object **must** be provided to the `PUT` request.

        **Editable Fields:**
        - `name`
        - `coefficients`

        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=typing.List[params._SerializerBenchmark]
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PUT",
            path="/reporting/benchmarks",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PutReportingBenchmarksResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def create(
        self,
        *,
        data: params.PostReportingBenchmarksBody,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostReportingBenchmarksResponse:
        """
        Returns the created Benchmark
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if pager_limit is not None:
            _query["pager.limit"] = encode_param(pager_limit, False)
        if pager_page is not None:
            _query["pager.page"] = encode_param(pager_page, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostReportingBenchmarksBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/reporting/benchmarks",
            auth_names=["bearerAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.PostReportingBenchmarksResponse,
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
    ) -> models.GetReportingBenchmarksIdResponse:
        """
        Returns a Benchmark based on a single ID
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
            path=f"/reporting/benchmarks/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetReportingBenchmarksIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetReportingBenchmarksResponse:
        """
        Returns a list of Benchmarks within the data field
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
            path="/reporting/benchmarks",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetReportingBenchmarksResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def delete(
        self,
        *,
        id: int,
        pager_limit: typing.Optional[int] = None,
        pager_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Delete:
        """
        Returns the "OK" message and a json object with the id  of item deleted, if deletion was successful
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
            method="DELETE",
            path=f"/reporting/benchmarks/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Delete,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
