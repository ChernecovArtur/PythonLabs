from datetime import datetime

class Transaction:
    def __init__ (self, description:str, amount:float, category:str, type:bool=False) -> None:
        self.data = {
            'description': description,
            'amount': amount,
            'type': type, 
            'category': category,
            'date': datetime.now()
        }

    def __str__(self) -> str:
        sign = "+" if self.data['type'] else "-"
        type_str = "доход" if self.data['type'] else "расход"
        date_str = self.data['date'].strftime("%d.%m.%Y %H:%M")

        return f"{sign} {self.data['amount']} руб. - {self.data['description']} [{self.data['category']}] ({type_str}) - {date_str}"