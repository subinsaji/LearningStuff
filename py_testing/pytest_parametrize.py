import pytest


"""
Below is the what is the pytest docs do it. It is rather un-Pythonic and comma seperated
sepereated strings are hard on the eyes
"""


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

@pytest.mark.parametrize("number_1",
                         [0,1,2,3,4])
def test_number_less_than_3(number_1):
    assert number_1 < 3

# maths functions

