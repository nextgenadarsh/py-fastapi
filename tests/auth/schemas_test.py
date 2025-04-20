import pytest

from api.auth.schemas import UserRequest

@pytest.fixture
def user_create_request():
    return UserRequest(username='adarsh', 
                       email='email@google.com', 
                       password='password',
                       first_name='Adarsh', 
                       last_name='Kumar',
                       roles='admin')

def test_user_create_request(user_create_request):
    assert user_create_request.username == 'adarsh'
    assert user_create_request.first_name == 'Adarsh'