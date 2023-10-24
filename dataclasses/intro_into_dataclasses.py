from dataclasses import dataclass
#here is an example of regular classes

#class Person():
#    def __init__(self, name, age, height, email):
 #       self.name = name
 #       self.age = age
 #       self.height = height
 #       self.email = email  

# However when we use the dataclasses module we need to import dataclass to use it as a decorator in the class we are 
# creating. This means we dont need to write __innit__ function at the start. You only need attributes of the class 
# and their types. Here is an example:



#@dataclass
#class Person():
#    name: str
#    age: int
#    height: float 
#    email: str
    
# can also set values for the attributes:

@dataclass
class Person():  
    name: str = "Subin"
    age: int = 30
    height: float = 1.77 
    email: str = "subin@subin.com"
    
print(Person())

