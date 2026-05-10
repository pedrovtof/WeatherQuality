from src.contracts.response_sucess_api import ResponseSucessApi
import pytest

def test_response_sucess_api():
    response = ResponseSucessApi()
    response.set_status(200)
    response.set_message("Success")
    response.set_details({"test": "data"})
    
    assert response.get_status() == 200
    assert response.get_message() == "Success"
    assert response.get_details() == {"test": "data"}
    
    result = response.build_return()
    assert result["message"] == "Success"
    assert result["data"] == {"test": "data"}

def test_response_api_invalid_status():
    response = ResponseSucessApi()
    with pytest.raises(Exception):
        response.set_status(100)
    with pytest.raises(Exception):
        response.set_status(600)
