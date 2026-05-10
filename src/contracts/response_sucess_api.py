"""
    Main contract to sucess
"""

from src.contracts.response_api import ResponseApi

class ResponseSucessApi(ResponseApi):
    
    def __init__(self) -> None:
        """
            Constructor
        """
        super().__init__()
        self._Details = {}

    def get_details(self) -> object:
        """
            Getter Details
        """
        return self._Details

    def set_details(self, value : object) -> None:
        """
            Setter Details
        """

        if value is None:
            raise Exception("[ResponseSucessApi][set_details] The details must be passed")

        if isinstance(value, dict) and len(value) == 0:
            raise Exception("[ResponseSucessApi][set_details] The details must be passed")

        self._Details = value

        return None

    def build_return(self) -> object:
        """
           Build sucess message return to client
        """
        
        return {
            "message": f"{self.get_message()}",
            "data": self._Details
        }

