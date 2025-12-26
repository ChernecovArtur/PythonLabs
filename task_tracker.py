from json import load, dump
from os import path

from task import Task

class TaskTracker:
    def __init__ (self, filename:str='tasks.json') -> None:
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task (self, description:str, category:str) -> object:
        task = Task(description, category)
        self.tasks.append(task)
        return task
    
    def mark_task (self, task_index: int) -> bool:
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].change_status()
            return True
        return False
    
    def get_all_tasks (self) -> list:
        return self.tasks
    
    def get_tasks_by_category (self, category:str) -> list:
        return [task for task in self.tasks if task.data['category'] == category]
    
    def search_tasks (self, search_term:str) -> list:
        search_term = search_term.lower()
        return [task for task in self.tasks if search_term in task.data['description'].lower()]
    
    def save_tasks (self) -> None:
        try:
            data = {
                'tasks': [task.data for task in self.tasks]
            }

            with open(self.filename, 'w', encoding='utf-8') as f:
                dump(data, f, ensure_ascii=False, indent=2)

        except Exception as e:
            print(f"Ошибка при сохранении задач: {e}")
    
    def load_tasks (self) -> None:
        try:
            if path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = load(f)
                    self.tasks = [
                        Task(
                            task_data['description'], 
                            task_data['category'], 
                            task_data['status']
                        ) for task_data in data.get('tasks', [])
                    ]
        except Exception as e:
            print(f"Ошибка при загрузке задач: {e}")
            self.tasks = []
    
    def display_tasks (self, tasks:list=None) -> None:
        if tasks is None:
            tasks = self.tasks
        
        if not tasks:
            print("Нет задач для отображения.")
            return
        
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    
    def __del__ (self) -> None:
        self.save_tasks()