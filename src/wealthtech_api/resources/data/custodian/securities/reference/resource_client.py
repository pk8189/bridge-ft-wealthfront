"""File Generated by Sideko (sideko.dev)"""

from wealthtech_api.core import (
    SyncBaseClient,
    to_encodable,
    AsyncBaseClient,
    RequestOptions,
    default_request_options,
)
from wealthtech_api.types.data.custodian.securities.reference import models, params
import typing


class ReferenceClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.PostDataCustodianSecuritiesReferenceBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.PostDataCustodianSecuritiesReferenceResponseItem]:
        """
        Returns a list of normalized custodian reported securities enriched with Intrinio Market data for a provided `reported_date`

        **Example Records**

        Below is an example of two security records reported by Schwab, the first is a standard `AAPL` stock and below that
        is an AAPL option. Option records will have additional data points populated that provided specific information about
        the option as reported by the custodian.

        ```json
        [
          {
            "reported_date": "2024-07-10",
            "source": "SWB",
            "cusip": "037833100",
            "symbol": "AAPL",
            "description": "APPLE INC ",
            "security_type": "COM",
            "security_type_description": "COMMON STOCK",
            "option_root_symbol": "",
            "option_expiration_date": "",
            "option_code": "",
            "strike_price_amount": 0,
            "market_data": {
                "symbol": "AAPL",
                "description": "Apple Inc",
                "figi": "BBG000B9Y5X2",
                "composite_figi": "BBG000B9XRY4",
                "security_type": "Ordinary Shares",
                "security_code": "EQS",
                "security_code_description": "Equity Shares"
            }
          },
          {
            "reported_date": "2024-07-10",
            "source": "SWB",
            "cusip": "",
            "symbol": "AAPL",
            "description": "CALL APPLE INC $195        EXP 09/19/25",
            "security_type": "OEQ",
            "security_type_description": "EQUITY OPTION",
            "option_root_symbol": "AAPL",
            "option_expiration_date": "2025-09-19",
            "option_code": "C",
            "strike_price_amount": 195,
            "market_data": {
                "symbol": "AAPL",
                "description": "Apple Inc",
                "figi": "BBG000B9Y5X2",
                "composite_figi": "BBG000B9XRY4",
                "security_type": "Ordinary Shares",
                "security_code": "EQS",
                "security_code_description": "Equity Shares"
            }
          }
        ]
        ```

        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerPostDataCustodianSecuritiesReferenceBody,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/data/custodian/securities/reference",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=typing.List[
                models.PostDataCustodianSecuritiesReferenceResponseItem
            ],
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncReferenceClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.PostDataCustodianSecuritiesReferenceBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.PostDataCustodianSecuritiesReferenceResponseItem]:
        """
        Returns a list of normalized custodian reported securities enriched with Intrinio Market data for a provided `reported_date`

        **Example Records**

        Below is an example of two security records reported by Schwab, the first is a standard `AAPL` stock and below that
        is an AAPL option. Option records will have additional data points populated that provided specific information about
        the option as reported by the custodian.

        ```json
        [
          {
            "reported_date": "2024-07-10",
            "source": "SWB",
            "cusip": "037833100",
            "symbol": "AAPL",
            "description": "APPLE INC ",
            "security_type": "COM",
            "security_type_description": "COMMON STOCK",
            "option_root_symbol": "",
            "option_expiration_date": "",
            "option_code": "",
            "strike_price_amount": 0,
            "market_data": {
                "symbol": "AAPL",
                "description": "Apple Inc",
                "figi": "BBG000B9Y5X2",
                "composite_figi": "BBG000B9XRY4",
                "security_type": "Ordinary Shares",
                "security_code": "EQS",
                "security_code_description": "Equity Shares"
            }
          },
          {
            "reported_date": "2024-07-10",
            "source": "SWB",
            "cusip": "",
            "symbol": "AAPL",
            "description": "CALL APPLE INC $195        EXP 09/19/25",
            "security_type": "OEQ",
            "security_type_description": "EQUITY OPTION",
            "option_root_symbol": "AAPL",
            "option_expiration_date": "2025-09-19",
            "option_code": "C",
            "strike_price_amount": 195,
            "market_data": {
                "symbol": "AAPL",
                "description": "Apple Inc",
                "figi": "BBG000B9Y5X2",
                "composite_figi": "BBG000B9XRY4",
                "security_type": "Ordinary Shares",
                "security_code": "EQS",
                "security_code_description": "Equity Shares"
            }
          }
        ]
        ```

        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerPostDataCustodianSecuritiesReferenceBody,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/data/custodian/securities/reference",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=typing.List[
                models.PostDataCustodianSecuritiesReferenceResponseItem
            ],
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)