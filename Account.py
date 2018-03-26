import datetime

class Account:
    def __init__(self):
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append([
            datetime.date.today().strftime("%d/%m/%Y"),
            amount,
            False,
            self.balance
            ])

    def withdraw(self, amount):
        self.balance -= amount
