import mock
from Formatter import Formatter
mock_account = mock.Mock()
mock_account.history = [
    ['10/01/2012', 1000, '', 1000],
    ['13/01/2012', 2000, '', 3000],
    ['14/01/2012', '', 500, 2500]
]

mock_account.string = [['10/01/2012', 1000, '', 1000]]


def test_Formatter_reverse():
    formatter = Formatter(mock_account.history)
    formatter.reverse()
    assert formatter.partial_history == [
        ['14/01/2012', '', 500, 2500],
        ['13/01/2012', 2000, '', 3000],
        ['10/01/2012', 1000, '', 1000]
    ]


def test_Formatter_format_integer():
    formatter = Formatter(mock_account.history)
    formatter.format_integer()
    assert formatter.partial_history == [
        ['10/01/2012', '1000.00', '', '1000.00'],
        ['13/01/2012', '2000.00', '', '3000.00'],
        ['14/01/2012', '', '500.00', '2500.00']
    ]


def test_Formatter_to_string():
    formatter = Formatter(mock_account.string)
    formatter.reverse()
    formatter.format_integer()
    formatter.to_string()
    answer = "date || credit || debit || balance\n10/01/2012 || 1000.00 ||  || 1000.00"
    assert formatter.processed_history == answer
