class Account:
    def __init__(self):
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
