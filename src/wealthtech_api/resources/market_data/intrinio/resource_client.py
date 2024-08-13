"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    RequestOptions,
    AsyncBaseClient,
    default_request_options,
    encode_param,
    QueryParams,
    SyncBaseClient,
)
import typing


class IntrinioClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def get(
        self,
        *,
        intrinio_endpoint: str,
        x_intrinio_api_key: str,
        next_page: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Endpoint to access market data from Intrinio. Sign up for an API Key [here](https://docs.intrinio.com/documentation/api_v2/getting_started). The endpoint response varies depending on the Intrinio endpoint provided.
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if next_page is not None:
            _query["next_page"] = encode_param(next_page, False)
        _header: typing.Dict[str, str] = {}
        _header["x-Intrinio-Api-Key"] = encode_param(x_intrinio_api_key, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/market-data/intrinio/{intrinio_endpoint}",
            auth_names=["bearerAuth"],
            query_params=_query,
            headers=_header,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncIntrinioClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def get(
        self,
        *,
        intrinio_endpoint: str,
        x_intrinio_api_key: str,
        next_page: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Endpoint to access market data from Intrinio. Sign up for an API Key [here](https://docs.intrinio.com/documentation/api_v2/getting_started). The endpoint response varies depending on the Intrinio endpoint provided.
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if next_page is not None:
            _query["next_page"] = encode_param(next_page, False)
        _header: typing.Dict[str, str] = {}
        _header["x-Intrinio-Api-Key"] = encode_param(x_intrinio_api_key, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/market-data/intrinio/{intrinio_endpoint}",
            auth_names=["bearerAuth"],
            query_params=_query,
            headers=_header,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
