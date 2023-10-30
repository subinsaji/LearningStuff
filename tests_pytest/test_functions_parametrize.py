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
    
# parametrize test with 2 arguments and ranges


# range gives an array array of numbers
    
@pytest.mark.parametrize("a", range(5))
@pytest.mark.parametrize("b", range(10))
def test_addition_2_args(a,b):
    assert addition(a,b) == a + b
    
    
# however not all inputs are integers and the range() func
# is less useful in other cases

# pytest also has an object called pytest_generate_tests which
# receives the metafuc object as an arg
#
# metafunc object provides information about the test function
# i.e. name, args, fixtures
#
# You can use the metafunc object to generate parametrized tests by
# calling the metafunc.parametrize() method:


def pytest_generate_tests(metafunc):
    if 'x' in metafunc.fixturenames and 'y' in metafunc.fixturenames:
        metafunc.parametrize('x', [1, 2, 3])
        metafunc.parametrize('y', [5, 6, 7])
        
def test_addition_generate_tests(x,y):
    assert addition(x,y) == x + y
    
