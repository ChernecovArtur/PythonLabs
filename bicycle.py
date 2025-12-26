from road_vehicle import RoadVehicle

class Bicycle (RoadVehicle):
    def __init__(self, max_speed: float) -> None:
        self._max_speed = max_speed
        
    def get_max_speed(self) -> float:
        return self._max_speed
    
    def get_vehicle_type(self) -> str:
        return "Велосипед"
    
    def get_engine_type(self) -> str:
        return "Энергия человека"