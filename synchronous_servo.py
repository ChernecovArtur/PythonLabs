from rotary_engine import RotaryEngine

class SynchronousServo(RotaryEngine):
    def __init__(self, power: float, voltage: float, max_angle: float) -> None:
        super().__init__(power, voltage, max_angle)
    
    def start(self) -> None:
        self._rotation_speed = 2.0
        print(f"Синхронный сервопривод запущен")
    
    def stop(self) -> None:
        self._rotation_speed = 0.0
        print("Синхронный сервопривод остановлен")
    
    def set_position(self, angle: float) -> None:
        super().set_angle(angle)
        print(f"Позиция установлена: {angle}°")
    
    def __str__(self) -> str:
        return f"Синхронный сервопривод({self._power}Вт)"
    
    def __repr__(self) -> str:
        return f"Синхронный сервопривод(мощность={self._power}, макс. угол={self._max_angle})"