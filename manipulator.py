from synchronous_servo import SynchronousServo
from stepper_servo import StepperServo
from typing import List, Tuple, Self

class SixAxisManipulator:
    def __init__(self) -> None:
        
        self.servos = [
            SynchronousServo(123, 24, 180),
            SynchronousServo(152, 24, 120), 
            SynchronousServo(118, 24, 135),  
            StepperServo(45, 12, 270),      
            StepperServo(54, 12, 180),      
            SynchronousServo(51, 12, 360)    
        ]
        self.position = [0, 0, 0]
    
    def start_all(self) -> None:
        for i, servo in enumerate(self.servos):
            servo.start()
            print(f"Звено {i+1}: {servo}")
    
    def set_angles(self, angles: List[float]) -> None:
        if len(angles) != 6:
            raise ValueError("Нужно 6 углов для 6-звенного манипулятора")
        
        for servo, angle in zip(self.servos, angles):
            servo.set_position(angle)
        
        self.position = [
            sum(angles[:3]) * 0.1,
            sum(angles[3:]) * 0.1,  
            max(angles) * 0.05
        ]
    
    def __add__(self, vector: Tuple[float, float, float]) -> Self:
        new_x = self.position[0] + vector[0]
        new_y = self.position[1] + vector[1] 
        new_z = self.position[2] + vector[2]
        
        new_angles = [
            new_x * 10, new_y * 8, new_z * 6,
            new_x * 4, new_y * 3, new_z * 5
        ]
        
        self.set_angles(new_angles)
        return self
    
    def __str__(self) -> str:
        return f"6-звенный манипулятор(позиция={self.position})"
    
    def __repr__(self) -> str:
        return f"6-звенный манипулятор(позиция={self.position})"