class Stack:
    def __init__(self) -> None:
        self.array = list()

    def push (self, item:str) -> None:
        self.array.append(item)

    def pop (self) -> str:
        item = self.array[-1]
        self.array = self.array[:-1]

        return item
    
    def peek (self) -> str:
        return self.array[-1]
    
    def is_empty(self) -> bool:
        return len(self.array) == 0