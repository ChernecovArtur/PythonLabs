from abc import ABC, abstractmethod
from vehicle import Vehicle

class RoadVehicle(Vehicle, ABC):
    
    @abstractmethod
    def get_engine_type(self) -> str:
        pass