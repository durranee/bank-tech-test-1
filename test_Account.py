from Account import Account
from freezegun import freeze_time
import datetime

def test_Account():
    account = Account()
    assert isinstance(account, Account)
    assert account.balance == 0
    account.deposit(1000)
    assert account.balance == 1000
    account.withdraw(500)
    assert account.balance == 500

@freeze_time("2018-01-18")
def test_Account_history():
    assert datetime.datetime.now() == datetime.datetime(2018, 1, 18)
    account = Account()
    assert account.history == []
    account.deposit(1000)
    assert account.history == [['18/01/2018', 1000.00, False, 1000.00]]
