import pytest
from login_user import save_new_user, user_psw
from validators import hash_password

@pytest.fixture
def new_user():
    name = "testuser"
    password = "ValidPass123"
    save_new_user(name, hash_password(password + name))
    return name, password

def test_user_saved_correctly(new_user):
    name, password = new_user
    hashed = hash_password(password + name)
    assert user_psw[name] == hashed

