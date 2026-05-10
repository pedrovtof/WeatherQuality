# pyrefly: ignore [missing-import]
from fastapi.responses import JSONResponse
from src.contracts.response_sucess_api import ResponseSucessApi
from src.contracts.response_error_api import ResponseErrorApi
from src.contracts.enumerate_api_response import EnumApiResponse
from src.models.openmeteo_model import Openmeteo

class Weather:
    def __init__(self):
        return
    
    def get_hourly_air_quality_values(self, params):

        try:
            openmeteo = Openmeteo()
            _response = openmeteo.execute_api_air_request(params.to_params())
            
            response = ResponseSucessApi()
            response.set_status(200);
            response.set_message(EnumApiResponse.GET_HOURLY_AIR_QUALITY_VALUES_SUCESS.value)
            response.set_details(_response)

            return response.build_return()
        except Exception:
            response = ResponseErrorApi()
            response.set_status(400)
            response.set_message(EnumApiResponse.ERROR_GENERIC.value)

            return JSONResponse(
                status_code=response.get_status(),
                content=response.build_return()
            )

