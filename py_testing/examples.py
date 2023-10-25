# simple maths functions

def addition(a: int | float, b: int | float) -> int | float:  
    return a + b

def subtraction(a: int | float, b: int | float) -> int | float:  
    return a - b  
  
# string Functions  

def reverse_string(string: str) -> str:  
    return string[::-1]  
 
def capitalise_string(string: str) -> str:  
    return string.upper()  
  
def clean_string(string: str) -> str:  
    return string.strip().lower()