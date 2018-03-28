class Processor:
    def __init__(self, account_history):
        self.processed_history = """
        date || credit || debit || balance"""
        self.partial_history = account_history

    def process_history(self):
        self.partial_history = self.reverse()

    def reverse(self):
        return list(reversed(self.partial_history))

    
