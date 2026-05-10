"""
    Path to validate the server
"""

from src.contracts.enumerate_api_response import EnumApiResponse
from src.contracts.response_sucess_api import ResponseSucessApi

def healthcheck_message() -> object:
    """
        Return alive json
    """
    response = ResponseSucessApi()
    response.set_status(200);
    response.set_message(EnumApiResponse.GET_HEALTHCHECK.value)
    response.set_details({
        "test":"only to validate"
    })
    
    return response.build_return()
