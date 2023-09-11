class Person:
    number_of_people = 0 # this is a class attribute which means its defines for the entire class
    
    def __init__(self,name):
        self.name = name
        Person.number_of_people += 1


    #class methods and decorators
    @classmethod #this is a decorator to denote a class method
    def number_of_people(cls):
        return cls.number_of_people()
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
    

    
p1 = Person("tim")
print(Person.number_of_people)
p2 = Person("jill")
print(Person.number_of_people)






