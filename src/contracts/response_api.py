"""
    Main contract api
"""

from src.interfaces.Iresponse_api import IResponseApi

class ResponseApi(IResponseApi):
    
    def __init__(self):
        """
            Constructor
        """
        self._Status = 0
        self._Message = ""
        self._Return = ""
    
    def get_status(self) -> int: 
        """
            Getter Status
        """
        return self._Status
    
    def set_status(self, value : int) -> None:
        """
            Setter Status
        """
        if value < 200 or value > 599:
            raise Exception(f"[ResponseApi][set_status] Not configured status exception {value}")

        self._Status = value
        return None
    
    def get_message(self) -> str: 
        """
            Getter Status
        """
        return self._Message
    
    def set_message(self, value : str) -> None:
        """
            Setter Status
        """
        if value == None or value == "":
            raise Exception(f"[ResponseApi][set_message] Not configured message exception {value}")

        self._Message = value
        return None
    
    def build_return(self) -> object:
        """
            Build message return to client
        """
        return {
            "message": f"{self.get_message()}" 
        }
