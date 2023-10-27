# Class example

class Greeting:
    def __init__(self, name) -> None:
        self.name = name
        
    def say_hello(self) -> str:
        return f"Hello {self.name}"
    
    def say_goodbye(self) -> str:
        return f"Goodbye {self.name}"
    
    