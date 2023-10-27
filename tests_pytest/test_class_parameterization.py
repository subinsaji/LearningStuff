"""
Test Class Parametrization
"""

from tests_pytest.example_parametrize_classes import Greeting
import pytest

@pytest.mark.parametrize("name", 
[
    "John Doe",
    "Jan Doe",
    "Foo Bar",
],)
class TestGreeting:
    """
    Test Greeting Class
    """
    
    def test_say_hello(self, name):
        """Test the say_hello method
        """
        greeting = Greeting(name)
        assert greeting.say_hello == f"Hello {name}"
        
    def test_say_goodbye(self, name):
        """Test the say_goodbye method
        """
        greeting = Greeting(name)
        assert greeting.say_goodbye == f"Goodbye {name}"
        
        