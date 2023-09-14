import functools
def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


# decorating functions with parameters

def smart_divide(func):
    def inner(a,b):
        print("I am going to divide", a , "and", b)
        if b == 0 :
            print("Cannot divide!")
            return
        
        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    print(a/b)
    

divide(2,5)
divide(2,0)