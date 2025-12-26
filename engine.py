class Engine: 
    def __init__(self, power: float, voltage: float) -> None:
        self._power = power          
        self._voltage = voltage      
        self._rotation_angle = 0.0   
        self._rotation_speed = 0.0   
        self._acceleration = 0.0     
    
    def start(self) -> None:
        self._rotation_speed = 0.1
        print(f"Двигатель запущен")
    
    def stop(self) -> None:
        self._rotation_speed = 0.0
        self._acceleration = 0.0
        print("Двигатель остановлен")
    
    def __eq__(self, other) -> bool:
        return self._power == other._power
    
    def __lt__(self, other) -> bool:
        return self._power < other._power
    
    def __le__(self, other) -> bool:
        return self._power <= other._power
    
    def __gt__(self, other) -> bool:
        return self._power > other._power
    
    def __ge__(self, other) -> bool:
        return self._power >= other._power
    
    def __str__(self) -> str:
        return f"Двигатель({self._power}Вт, {self._voltage}В)"
    
    def __repr__(self) -> str:
        return f"Двигатель(мощность={self._power}, напряжение={self._voltage})"