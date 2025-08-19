class PersonAccount:
    def __init__(self, first_name, last_name, incomes: list = [], expenses: list = []):

        self.first_name=first_name
        self.last_name=last_name
        self.incomes=incomes
        self.expenses=expenses
        
    def total_income(self):
        total = 0
        for inc in self.incomes:
            total+=inc.get("value")
        return total

    def total_expense(self):
        total = 0
        for inc in self.expenses:
            total+=inc.get("value")
        return total
        
    def account_info(self):
        return f"Name: {self.first_name} {self.last_name} \nTotal income: {self.total_income()} \nTotal expense: {self.total_expense()}\nBalance: {self.account_balance()}"
        
    def add_income(self, income: dict):
        self.incomes.append(income)
        
    def add_expense(self, expense: dict):
        self.expenses.append(expense)
        
    def account_balance(self):
        return self.total_income() - self.total_expense()
        
    
account=PersonAccount("Frank", "Mpo")
account.add_income({"description": "Main", "value": 200})
account.add_income({"description": "Resto", "value": 80})
account.add_income({"description": "Car", "value": 140})
account.add_expense({"description": "Gas monthly", "value": 30})
account.add_expense({"description": "Rent", "value": 220})

print(account.account_info())
