import pytest
from pytest_parametrize_cases import Case, parametrize_cases


"""
Below is the what is the pytest docs do it. It is rather un-Pythonic and comma seperated
sepereated strings are hard on the eyes
"""


# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected


@parametrize_cases(
    Case(test_input="3+5", expected=8),
    Case(test_input="2+4", expected=6),
    Case(test_input="6*9", expected=42)
)

def test_eval(test_input, expected):
    assert eval(test_input) == expected