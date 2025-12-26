class Task:
    def __init__ (self, description:str, category:str, status:bool=False) -> None:
        self.data = {
            'description': description,
            'status': status,
            'category': category
        }

    def change_status (self) -> None:
        self.data['status'] = not self.data['status']

    def __str__ (self) -> str:
        status = "[x]" if self.data['status'] else "[ ]"
        return f"{status} {self.data['description']} #{self.data['category']}"