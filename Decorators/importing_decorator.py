from decorators import do_twice

#@do_twice
#def say_whee():
#    print("Whee")
    
    
#@do_twice
#def greet(name):
#    print(f"Hello {name}")
    
#greet("Hello")


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"hi {name}"

hi_adam = return_greeting("Adam")
print(hi_adam)



