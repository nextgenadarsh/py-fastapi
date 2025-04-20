from fastapi import status
from fastapi.testclient import TestClient
import pytest
from sqlalchemy import engine, text

from api.auth.router import get_user
from api.database import get_db
from api.todos.models import Todos
from tests.database_mock import engine, TestingSessionLocal, get_db_override
from main import app

#region Overrides
def get_user_override():
    return { 'user_name': 'adarsh', 'id': 1, 'roles': 'admin' }

app.dependency_overrides[get_db] = get_db_override
app.dependency_overrides[get_user] = get_user_override
#endregion

client = TestClient(app)

@pytest.fixture
def test_todo():
    todo = Todos(
        title = 'Test todo',
        description = 'Test desc',
        priority = 4,
        complete = False,
        owner_id = 1
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text('DELETE FROM todos'))
        connection.commit()

def test_get_todos(test_todo):
    response = client.get("/todos")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() != []
    assert len(response.json()) == 1