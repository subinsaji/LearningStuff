""""Test Fixture Parameterization
"""

import pytest

@pytest.mark.parametrize("name, username, password",
    [
        ("John Smith", "johnsmith", "password"),
        ("Jane Smith", "janesmith", "secret"),
        ("Subin Saji", "subinsaji", "foobin"),
    ],)
def test_login(user, name, username, password):
    """Test the login functionality with different users"""
    assert user["name"] == name
    assert user["username"] == username
    assert user["password"] == password
    
