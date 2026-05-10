"""
    Main contract to error
"""

from src.contracts.response_api import ResponseApi

class ResponseErrorApi(ResponseApi):

    def __init__(self) -> None:
        """
            Constructor
        """
        super().__init__()
