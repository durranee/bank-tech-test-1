from Account import Account
from freezegun import freeze_time
import datetime
import pytest


@freeze_time("2018-01-18")
@pytest.fixture(scope="function")
def account():
    account = Account()
    account.deposit(1000)
    account.deposit(1000)
    return account


def test_Account(account):
    assert isinstance(account, Account)


def test_Account_deposit(account):
    account.deposit(1000)
    assert account.balance == 2000


def test_Account_withdraw(account):
    account.withdraw(500)
    assert account.balance == 500


@freeze_time("2018-01-18")
def test_Account_history(account):
    account
    assert account.history == [['18/01/2018', 1000, '', 1000]]
    account.withdraw(1000)
    assert account.history == [['18/01/2018', 1000, '', 1000],
                               ['18/01/2018', '', 1000, 0]]
