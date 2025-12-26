from json import load, dump
from os import path
from datetime import datetime

from transaction import Transaction

class BudgetTracker:
    def __init__ (self, filename: str='budget.json') -> None:
        self.filename = filename
        self.transactions = []
        self.limits = {}
        self.load_data()
    
    def add_transaction (self, description: str, amount: float, category: str, type: bool = False) -> tuple[bool, str]:
        can_add, message = self.can_add_transaction(amount, category, type)
        if not can_add:
            return False, message
        
        transaction = Transaction(description, amount, category, type)
        self.transactions.append(transaction)

        return True, "Транзакция успешно добавлена"

    def can_add_transaction(self, amount: float, category: str, type: bool = False) -> tuple[bool, str]:
        if type:  
            return True, ""
        
        current_balance = self.get_balance()
        if amount > current_balance:
            return False, f"Недостаточно средств. Баланс: {current_balance:.2f} руб., требуется: {amount:.2f} руб."
        
        if category in self.limits:
            category_expenses = self.get_category_expenses(category)
            if category_expenses + amount > self.limits[category]:
                remaining = self.limits[category] - category_expenses
                return False, f"Превышен лимит по категории '{category}'. Осталось: {remaining:.2f} руб."
        
        return True, ""
    
    def get_category_expenses(self, category: str) -> float:
        expenses = 0
        current_month = datetime.now().month
        current_year = datetime.now().year
        
        for transaction in self.transactions:
            transaction_date = transaction.data['date']
            if (transaction.data['category'] == category and 
                not transaction.data['type'] and  
                transaction_date.month == current_month and
                transaction_date.year == current_year):
                expenses += transaction.data['amount']
        return expenses
    
    def get_balance (self) -> float:
        balance = 0
        for transaction in self.transactions:
            if transaction.data['type']:  
                balance += transaction.data['amount']
            else:  
                balance -= transaction.data['amount']
        return balance
    
    def set_limit (self, category: str, limit: float) -> None:
        self.limits[category] = limit
    
    def save_data (self) -> None:
        try:
            data = {
                'transactions': [
                    {
                        'description': t.data['description'],
                        'amount': t.data['amount'],
                        'type': t.data['type'],
                        'category': t.data['category'],
                        'date': t.data['date'].isoformat()
                    }
                    for t in self.transactions
                ],
                'limits': self.limits
            }
            with open(self.filename, 'w', encoding='utf-8') as f:
                dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")
    
    def load_data (self) -> None:
        try:
            if path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = load(f)
                    self.transactions = []

                    for t_data in data.get('transactions', []):
                        transaction = Transaction(
                            t_data['description'],
                            t_data['amount'],
                            t_data['category'],
                            t_data['type']
                        )
                        transaction.data['date'] = datetime.fromisoformat(t_data['date'])
                        self.transactions.append(transaction)
                    
                    self.limits = data.get('limits', {})
        except Exception as e:
            print(f"Ошибка при загрузке: {e}")
            self.transactions = []
            self.limits = {}
    
    def display_transactions (self, transactions=None) -> None:
        if transactions is None:
            transactions = self.transactions
        
        if not transactions:
            print("Нет операций для отображения.")
            return
        
        for i, transaction in enumerate(transactions, 1):
            print(f"{i}. {transaction}")
    
    def __del__ (self) -> None:
        self.save_data()