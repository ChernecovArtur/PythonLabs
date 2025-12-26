from engine import Engine

class RotaryEngine(Engine):
    def __init__(self, power: float, voltage: float, max_angle: float) -> None:
        super().__init__(power, voltage)
        self._max_angle = max_angle      
    
    def start(self) -> None:
        self._rotation_speed = 1.0
        print("Вращательный двигатель запущен")
    
    def stop(self) -> None:
        self._rotation_speed = 0.0
        print("Вращательный двигатель остановлен")
    
    def set_angle(self, angle: float) -> None:
        if abs(angle) <= self._max_angle:
            self._rotation_angle = angle
            print(f"Установлен угол: {angle}°")
        else:
            raise ValueError(f"Угол достиг максимума ({self._max_angle}°)")
    
    def __str__(self) -> str:
        return f"Вращательный двигатель({self._power}Вт, макс. угол: {self._max_angle}°)"
    
    def __repr__(self) -> str:
        return f"Вращательный двигатель(мощность={self._power}, макс. угол={self._max_angle})"
