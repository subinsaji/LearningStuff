"""

    Try: This block will test the excepted error to occur
    
    Except:  Here you can handle the error
    
    Else: If there is no exception then this block will be executed
    
    Finally: Finally block always gets executed either exception is generated or not
    
    
    --------------------------------------------------------------------------------------
    
    
    try:
       # Some Code.... 

    except:
       # optional block
       # Handling of exception (if required)

    else:
       # execute if no exception

    finally:
      # Some code .....(always executed)
      
    
"""






def divide(x,y):
    try:
        result = x//y
        
    except ZeroDivisionError:
        print("Sorry you are diving by zero")
    
    else:
        print("Yes your answer is:", result)
        
        
divide(3,2)
divide(3,0)


def divide_finally(x,y):
    try:
        result = x//y
        
    except ZeroDivisionError:
        print("Sorry you are diving by zero")
    
    else:
        print("Yes your answer is:", result)
    finally:
        print("This is always exectuted") 
        
        
        
divide_finally(3,2)
divide_finally(3,0)


    