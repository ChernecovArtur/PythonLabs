class Queue:
    def __init__(self) -> None:
        self.array = list()

    def enqueue (self, item:str) -> None:
        self.array.append(item)

    def dequeue (self) -> str:
        item = self.array[0]
        self.array = self.array[1:]

        return item
    
    def peek (self) -> str:
        return self.array[0]
    
    def is_empty(self) -> bool:
        return len(self.array) == 0