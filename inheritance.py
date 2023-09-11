"""""
class Cat:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

        def speak(self):
            print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

        def speak(self):
            print("Bark")
"""""



"""""
We use inhertance to stop copying common attributes in the class. Saves lines.
We can remove the __init__ method from both the classes and put it in a parent class ot an upper level classs. 

"""""


class Pet: # Gerneral class 
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
        
    def speak(self):
        print("I dont know what to say")
        
class Cat(Pet):
        def speak(self):
            print("Meow")

class Dog(Pet):
        def speak(self):
            print("Bark")


p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 34)
c.speak()
d = Dog("Jill",12)
d.show()