from road_vehicle import RoadVehicle

ENGINE_TYPES = ['бензиновый', 'электрический']

class Car (RoadVehicle):
    def __init__(self, max_speed: float, engine_type: str) -> None:
        self._max_speed = max_speed
        if engine_type not in ENGINE_TYPES:
            engine_type = ''
            
        self._engine_type = engine_type
        
    def get_max_speed(self) -> float:
        return self._max_speed
    
    def get_vehicle_type(self) -> str:
        return "Автомобиль"
    
    def get_engine_type(self) -> str:
        return self._engine_type