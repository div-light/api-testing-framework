from config.config import BASE_URL
from clients.api_client import APIClient
import pytest

@pytest.fixture
def api_client():
    return APIClient(BASE_URL)

@pytest.fixture
def auth_data(api_client):

    credentials = {
        "userEmail": "testuser77@test.com",
        "userPassword": "Test25@@!!"
    }

    response = api_client.post("auth/login", json=credentials)

    assert response.status_code == 200

    data = response.json()
    assert "token" in data
    assert "userId" in data
    assert "message" in data
    assert isinstance(data["token"], str)
    assert "Successfully" in data['message']

    return {
        "token": data["token"],
        "userId": data["userId"]
    }
