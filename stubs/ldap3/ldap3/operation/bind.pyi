from _typeshed import Incomplete

def bind_operation(
    version,
    authentication,
    name: str = ...,
    password: Incomplete | None = ...,
    sasl_mechanism: Incomplete | None = ...,
    sasl_credentials: Incomplete | None = ...,
    auto_encode: bool = ...,
): ...
def bind_request_to_dict(request): ...
def bind_response_operation(
    result_code,
    matched_dn: str = ...,
    diagnostic_message: str = ...,
    referral: Incomplete | None = ...,
    server_sasl_credentials: Incomplete | None = ...,
): ...
def bind_response_to_dict(response): ...
def sicily_bind_response_to_dict(response): ...
def bind_response_to_dict_fast(response): ...
def sicily_bind_response_to_dict_fast(response): ...
