"""
    Main contract interface
"""

from abc import ABC, abstractmethod

class IResponseApi(ABC):

    @abstractmethod
    def get_status(self) -> int: 
        """
            Getter Status
        """
    
    @abstractmethod
    def set_status(self, value : int) -> None:
        """
            Setter Status
        """
    
    @abstractmethod
    def get_message(self) -> str: 
        """
            Getter Message
        """

    @abstractmethod
    def set_message(self, value : str) -> None:
        """
            Setter Message
        """

    @abstractmethod
    def build_return(self) -> object:
        """
            Build message return to client
        """
