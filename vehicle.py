from abc import ABC, abstractmethod

class Vehicle (ABC):
    
    @abstractmethod
    def get_max_speed (self) -> float:
        pass
    
    @abstractmethod
    def get_vehicle_type (self) -> str:
        pass
