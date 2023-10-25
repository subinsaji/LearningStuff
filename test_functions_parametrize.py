import pytest

from examples import (
    addition,
    substraction,
    reverse_string,
    capitalise_string,
    clean_string,
)


# tests for simple maths

@pytest.mark.parametrize( "a, b, expected", [(1,2,3), (5,-1,4),],)
def test_addition(a,b, expected):
    assert addition(a, b) == expected
    
    
@pytest.mark.parametrize(" a, b, expected", [(1,2,-1), (5,-1,6),],)
def test_substraction(a,b, expected):
    assert substraction(a, b) == expected
    
    
# tests for simple strings    
    
@pytest.mark.parametrize( "string, expected", 
    [
        ("hello", "olleh")
        ("world", "dlrow")
        
        ],)
def test_reverse_string(a,b, expected):
    assert reverse_string(a, b) == expected
    
    
@pytest.mark.parametrize( "string, expected", 
    [
        ("hello", "HELLO")
        ("world", "WORLD")
        
        ],)
def test_capitalise_string(string, expected):
    assert capitalise_string(string) == expected
    
    

@pytest.mark.parametrize( "string, expected", 
    [
        ("hello", "HELLO")
        ("world", "WORLD")
        
        ],)
def test_clean_string(string, expected):
    assert clean_string(string) == expected
    