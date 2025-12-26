from rotary_engine import RotaryEngine

class StepperServo(RotaryEngine):
    def __init__(self, power: float, voltage: float, max_angle: float) -> None:
        super().__init__(power, voltage, max_angle)
        self._steps = 200
    
    def start(self) -> None:
        self._rotation_speed = 0.5
        print(f"Шаговый сервопривод запущен")
    
    def stop(self) -> None:
        self._rotation_speed = 0.0
        print("Шаговый сервопривод остановлен")
    
    def set_position(self, angle: float) -> None:
        steps_needed = int(angle * self._steps / 360)
        super().set_angle(angle)
        print(f"Угол {angle}° установлен через {steps_needed} шагов")
    
    def __str__(self) -> str:
        return f"Шаговый сервопривод({self._power}Вт)"
    
    def __repr__(self) -> str:
        return f"Шаговый сервопривод(мощность={self._power}, макс. угол={self._max_angle})"