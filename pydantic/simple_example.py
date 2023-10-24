from pydantic import BaseModel, ValidationError

# lets define model for out person 
class Person(BaseModel):
    age: int
    name: str
    is_married: bool
    
# create dictionary for containing the data we want to parse

data = {
    "name": John,
    "age" : 20,
    "is_married": False 
}

try:
    person = Person(**data)
    print(person.dict())
    

# now we create an object of the person class

person = Person(**data)
