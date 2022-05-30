from abc import ABC,abstractmethod
from typing import Optional,TypeVar
from venv import create

T = TypeVar("T")

class DataBase(ABC):
    
    @abstractmethod
    def create(**kwargs):
        pass
    
    @abstractmethod
    def read(**kwargs):
        pass
    
    @abstractmethod
    def update(**kwargs):
        pass
    
    @abstractmethod
    def delete(**kwargs):
        pass