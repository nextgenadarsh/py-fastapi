from . import main
from fastapi.testclient import TestClient

from fastapi import status

client = TestClient(main.app)

def test_health_check():
    response = client.get("/health")
    assert response is not None
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'status': 'Healthy' }
    