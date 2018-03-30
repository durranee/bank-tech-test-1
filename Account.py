import datetime


class Account:

    def __init__(self):
        self.balance = 0
        self.history = []

    def save_transaction(self, date, credit, debit, balance):
        self.history.append([
            date,
            credit,
            debit,
            balance
            ])

    def deposit(self, amount):
        self.balance += amount
        date = datetime.date.today().strftime("%d/%m/%Y")
        self.save_transaction(date, amount, '', self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        date = datetime.date.today().strftime("%d/%m/%Y")
        self.save_transaction(date, '', amount, self.balance)
