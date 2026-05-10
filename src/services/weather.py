from src.contracts.response_sucess_api import ResponseSucessApi
from src.contracts.response_error_api import ResponseErrorApi
from src.contracts.enumerate_api_response import EnumApiResponse
from src.models.openmeteo_model import Openmeteo

class Weather:
    def __init__(self):
        return
    
    def get_hourly_air_quality_values(self):

        openmeteo = Openmeteo()
        _response = openmeteo.execute_api_request({     
            "latitude": 52.52,
            "longitude": 13.41,
            "hourly": ["pm10", "pm2_5"]
        })
        
        response = ResponseSucessApi()
        response.set_status(200);
        response.set_message(EnumApiResponse.GET_HOURLY_AIR_QUALITY_VALUES_SUCESS.value)
        response.set_details(_response)

        return response.build_return()

