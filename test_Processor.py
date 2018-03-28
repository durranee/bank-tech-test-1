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
    assert process.processed_history == """
    date || credit || debit || balance
    14/01/2012 || || 500.00 || 2500.00
    13/01/2012 || 2000.00 || || 2500.00
    10/01/2012 || 1000.00 || || 2500.00"""

def test_Processor_reverse():
    process = Processor(mock_account.history)
    process.reverse()
    assert process.partial_history == [
        ['14/01/2012', False, 500, 2500],
        ['13/01/2012', 2000, False, 3000],
        ['10/01/2012', 1000, False, 1000]
    ]

def test_Processor_to_string():
    process = Processor(mock_account.history)
    process.to_string()
    assert process.partial_history == [
        ['10/01/2012', '1000.00', '', '1000.00'],
        ['13/01/2012', '2000.00', '', '3000.00'],
        ['14/01/2012', '', '500.00', '2500.00']
    ]
