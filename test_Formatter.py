import mock
from Formatter import Formatter
mock_account = mock.Mock()
mock_account.history = [
    ['10/01/2012', 1000, '', 1000],
    ['13/01/2012', 2000, '', 3000],
    ['14/01/2012', '', 500, 2500]
]


def test_Formatter():
    format = Formatter(mock_account.history)
    assert format.formated_history == """
    date || credit || debit || balance
    14/01/2012 || || 500.00 || 2500.00
    13/01/2012 || 2000.00 || || 2500.00
    10/01/2012 || 1000.00 || || 2500.00"""


def test_Formatter_reverse():
    format = Formatter(mock_account.history)
    format.reverse()
    assert format.partial_history == [
        ['14/01/2012', '', 500, 2500],
        ['13/01/2012', 2000, '', 3000],
        ['10/01/2012', 1000, '', 1000]
    ]


def test_Formatter_format_integer():
    format = Formatter(mock_account.history)
    format.format_integer()
    assert format.partial_history == [
        ['10/01/2012', '1000.00', '', '1000.00'],
        ['13/01/2012', '2000.00', '', '3000.00'],
        ['14/01/2012', '', '500.00', '2500.00']
    ]
