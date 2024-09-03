import pytest
from fastapi.testclient import TestClient
from restapi.main import app

pytestmark = pytest.mark.asyncio
client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
