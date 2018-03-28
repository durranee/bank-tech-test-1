class Processor:
    def __init__(self, account_history):
        self.processed_history = """
        date || credit || debit || balance"""
        self.partial_history = account_history

    def reverse(self):
        self.partial_history = list(reversed(self.partial_history))
