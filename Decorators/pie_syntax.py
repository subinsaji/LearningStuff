def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is being called")
        func()
        print("Something is happening after the function is being called")
    return wrapper

@my_decorator #this @ is a better way of saying say_whee = my_decorator(say_whee)
def say_whee():
    print("Whee!")
    
    