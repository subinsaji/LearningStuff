class Person:
    number_of_people = 0 # this is a class attribute which means its defines for the entire class. It doesnt use self
    
    def __init__(self,name):
        self.name = name
        Person.add_person()

    @classmethod  # This is decorator to denote that this specific method is class method
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod # "cls" is referencing the class itself and not the class method
    def add_person(cls):
        cls.number_of_people += 1
    
    
    
p1 = Person("Tim")
p2 = Person("Jill")


print(Person.number_of_people_())
