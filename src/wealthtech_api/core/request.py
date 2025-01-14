from typing import Any, Dict, Type, Union, Sequence
from urllib.parse import quote_plus


import httpx
from typing_extensions import TypedDict, Required, NotRequired
from pydantic import TypeAdapter, BaseModel

QueryParams = Dict[
    str, Union[httpx._types.PrimitiveData, Sequence[httpx._types.PrimitiveData]]
]


class RequestConfig(TypedDict):
    method: Required[str]
    url: Required[httpx._types.URLTypes]
    content: NotRequired[httpx._types.RequestContent]
    data: NotRequired[httpx._types.RequestData]
    files: NotRequired[httpx._types.RequestFiles]
    json: NotRequired[Any]
    params: NotRequired[QueryParams]
    headers: NotRequired[Dict[str, str]]
    cookies: NotRequired[Dict[str, str]]
    auth: NotRequired[httpx._types.AuthTypes]
    follow_redirects: NotRequired[bool]
    timeout: NotRequired[httpx._types.TimeoutTypes]
    extensions: NotRequired[httpx._types.RequestExtensions]


class RequestOptions(TypedDict):
    """
    Attributes:
        - timeout: int. The number of seconds to await an API call before timing out.

        - additional_headers: typing.Dict[str, typing.Any]. A dictionary containing additional parameters to spread into the request's header dict

        - additional_params: typing.Dict[str, typing.Any]. A dictionary containing additional parameters to spread into the request's query parameters dict

    """

    timeout: NotRequired[int]
    additional_headers: NotRequired[Dict[str, str]]
    additional_params: NotRequired[QueryParams]


def default_request_options() -> RequestOptions:
    """Returns default request options"""
    return {}


def model_dump(item: Any) -> Any:
    if isinstance(item, list):
        return [model_dump(i) for i in item]

    if isinstance(item, BaseModel):
        return item.model_dump(exclude_unset=True, by_alias=True)
    else:
        return item


def to_encodable(*, item: Any, dump_with: Type) -> Any:
    adapter = TypeAdapter(dump_with)
    validated_item = adapter.validate_python(item)
    return model_dump(validated_item)


def encode_param(
    value: Any, explode: bool
) -> Union[httpx._types.PrimitiveData, Sequence[httpx._types.PrimitiveData]]:
    if isinstance(value, (list, dict)) and not explode:
        return quote_plus(",".join(map(str, value)))
    else:
        return value
