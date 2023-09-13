def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper

def say_whee():
    print("Wheee!")
    
say_whee = my_decorator(say_whee) #this is the decorator - its a function within a function
# decorators wrap a function, modifying its behaviour

print(say_whee())