# pyrefly: ignore [missing-import]
from fastapi.responses import JSONResponse
from src.contracts.response_sucess_api import ResponseSucessApi
from src.contracts.response_error_api import ResponseErrorApi
from src.contracts.enumerate_api_response import EnumApiResponse
from src.models.openmeteo_model import Openmeteo

class Climate:
    def __init__(self):
        return
    
    def get_daily_climate_values(self, params):

        try:
            openmeteo = Openmeteo()
            _response = openmeteo.execute_api_climate_request(params.to_params())
            
            response = ResponseSucessApi()
            response.set_status(200);
            response.set_message(EnumApiResponse.GET_DAILY_CLIMATE_VALUES_SUCESS.value)
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

    def get_available_models(self):
        try:
            models = [
                {"model": "CMCC_CM2_VHR4", "description": "Euro-Mediterranean Center on Climate Change (Italy)"},
                {"model": "FGOALS_f3_H", "description": "Chinese Academy of Sciences (China)"},
                {"model": "HiRAM_SIT_HR", "description": "National Oceanic and Atmospheric Administration (USA)"},
                {"model": "MRI_AGCM3_2_S", "description": "Meteorological Research Institute (Japan)"},
                {"model": "EC_Earth3P_HR", "description": "EC-Earth Consortium (Europe)"},
                {"model": "MPI_ESM1_2_XR", "description": "Max Planck Institute for Meteorology (Germany)"},
                {"model": "NICAM16_8S", "description": "University of Tokyo / RIKEN (Japan)"}
            ]
            
            response = ResponseSucessApi()
            response.set_status(200)
            response.set_message(EnumApiResponse.GET_CLIMATE_MODELS_SUCESS.value)
            response.set_details(models)

            return response.build_return()
        except Exception:
            response = ResponseErrorApi()
            response.set_status(400)
            response.set_message(EnumApiResponse.ERROR_GENERIC.value)

            return JSONResponse(
                status_code=response.get_status(),
                content=response.build_return()
            )
