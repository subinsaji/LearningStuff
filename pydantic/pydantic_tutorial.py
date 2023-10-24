import json
from pydantic import BaseModel
from typing import Optional, List


class Book(BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_30: Optional[str]
    subtitle: Optional[str]
     





def main() -> None:
    """Maon Function"""
    with open("/home/wks59344/training_wheels/pydantic/data.json") as file:
        data = json.load(file)
        books: List[Book] = [Book(**item) for item in data]
        print(books[0])
        
    
if __name__ == "__main__":
    main()
    
    