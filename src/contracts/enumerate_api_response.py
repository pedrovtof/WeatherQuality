"""
    ENUMERATE response to api
"""
from enum import Enum

class EnumApiResponse(Enum):
    GET_HOURLY_AIR_QUALITY_VALUES_SUCESS = 'Sucess'
    GET_HEALTHCHECK = 'Alive'


