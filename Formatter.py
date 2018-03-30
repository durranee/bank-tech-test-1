class Formatter:
    def __init__(self, account_history):
        self.processed_history = """
        date || credit || debit || balance"""
        self.partial_history = account_history

    def reverse(self):
        self.partial_history = list(reversed(self.partial_history))

    def format_integer(self):
        new_list = []
        for transaction in self.partial_history:
            line = ['%.2f' % value if isinstance(value, int)
                    else value for value in transaction]
            new_list.append(line)
        self.partial_history = new_list
