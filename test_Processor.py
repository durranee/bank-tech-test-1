import pytest
import mock
from Processor import Processor
mock_account = mock.Mock()

mock_account.history = [
    ['10/01/2012', 1000, False, 1000],
    ['13/01/2012', 2000, False, 3000],
    ['14/01/2012', False, 500, 2500]
]

def test_Processor():
    process = Processor(mock_account.history)
    assert process.processed_statement == """
    date || credit || debit || balance
    14/01/2012 || || 500.00 || 2500.00
    13/01/2012 || 2000.00 || || 2500.00
    10/01/2012 || 1000.00 || || 2500.00"""
