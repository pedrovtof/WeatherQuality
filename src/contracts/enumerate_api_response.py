"""
    ENUMERATE response to api
"""
from enum import Enum

class EnumApiResponse(Enum):
    GET_HOURLY_AIR_QUALITY_VALUES_SUCESS = 'Sucess'
    GET_DAILY_CLIMATE_VALUES_SUCESS = 'Sucess'
    GET_CLIMATE_MODELS_SUCESS = 'Sucess'
    GET_HEALTHCHECK = 'Alive'
    ERROR_GENERIC = 'An error occurred during the request'


