from Account import Account

def test_Account():
    account = Account()
    assert isinstance(account, Account)
    assert account.balance == 0
    account.deposit(1000)
    assert account.balance == 1000
    account.withdraw(500)
    assert account.balance == 500

def test_Account_history():
    account = Account()
    assert account.history == []
