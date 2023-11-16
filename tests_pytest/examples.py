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

def area_of_triangle(a: int | float, b: int | float):
    return 0.5*a*b

def area_of_square(a: int | float, b: int | float):
    area_of_square = a * b
    return area_of_square
 


