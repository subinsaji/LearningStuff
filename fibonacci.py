import numpy as np

# fibonacci sequence starts with two numbers:

F_0 = 0
F_1 = 1

print(F_0)
print(F_1)

# sequence as follows the equation: F_{n} = F_{n-1} + F_{n-2}
# basically just add the last two numbers before the next one

F_2 = F_0 + F_1

print(F_2)

# cool! Now we have the third term in the sequence
# this fourth term is like this and so on...

F_3 = F_2 + F_1
print(F_3)

F_4 = F_3 + F_2
print(F_4)

F_5 = F_4 + F_3
print(F_5)

# This is rather tedious work...
# We can make a function and do some for looping instead
# Lets say we want the first 10 terms, n=11

def fibonacci_sequence(n):
    n = n+1
    fib = np.zeros(n) # making an empty numpy array of n+1 terms
    fib[1] = 1 # in the array the 1st position (after the 0th position) is set to 1: 0,  -->1<--  ,  1  ,  2  ,  3
    for i in range(2, n): # range() fuction has arguments: range(start, stop)
        fib[i] = fib[i-1] + fib[i-2] # F_{n} = F_{n-1} + F_{n-2}
    return print(fib)
    
fibonacci_sequence(10) # now running the function with n=10

#    Things that helped me understand:
#  - the indentation of return print(fib) needed to be in indented out of loop so for loop waits to finish then prints whole sequence
#  - know what the range() funcion does
#  - fib[] in square brackets just means position. In pyton the first position is always zero i.e. fib[0]
 
    
    
    
    