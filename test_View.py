import mock
from View import View
mock_form = mock.Mock()
mock_form.processed_history = """date || credit || debit || balance
                10/01/2012 || 1000.00 ||  || 1000.00
                10/01/2012 || 1000.00 ||  || 1000.00"""


def test_View(capsys):
    view = View(mock_form.processed_history)
    out, err = capsys.readouterr()
    assert out == """date || credit || debit || balance
                10/01/2012 || 1000.00 ||  || 1000.00
                10/01/2012 || 1000.00 ||  || 1000.00
"""
