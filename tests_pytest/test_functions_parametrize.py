import pytest
from  examples import (addition,
                                 subtraction,
                                 reverse_string,
                                 capitalise_string,
                                 clean_string,
                                 )


@pytest.mark.parametrize( "a, b, expected",  
    [  
        (1, 2, 3),  
        (5, -1, 4),  
    ],)  
def test_addition(a, b, expected):  
    assert addition(a, b) == expected  
  
  
@pytest.mark.parametrize( "a, b, expected",  
    [  
        (1, 2, -1),  
        (5, -1, 6),  
    ],)  
def test_subtraction(a, b, expected):  
    assert subtraction(a, b) == expected  
  
  
# Test String Functions  
@pytest.mark.parametrize( "string, expected",  
    [  
        ("hello", "olleh"),  
        ("world", "dlrow"),  
    ],)  
def test_reverse_string(string, expected):  
    assert reverse_string(string) == expected  
  
  
@pytest.mark.parametrize( "string, expected",  
    [  
        ("hello", "HELLO"),  
        ("world", "WORLD"),  
    ],)  
def test_capitalize_string(string, expected):  
    assert capitalise_string(string) == expected  
  
  
@pytest.mark.parametrize( "string, expected",  
    [  
        (" hello ", "hello"),  
        (" WoRlD ", "world"),  
    ],)  
def test_clean_string(string, expected):  
    assert clean_string(string) == expected
    