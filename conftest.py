import pytest

from clients.api_client import APIClient
from config.config import BASE_URL, USERNAME, PASSWORD


@pytest.fixture
def api_client():
    return APIClient(BASE_URL)


@pytest.fixture
def auth_data(api_client):

    credentials = {
        "userEmail": USERNAME,
        "userPassword": PASSWORD
    }

    response = api_client.post(
        "auth/login",
        json=credentials
    )

    assert response.status_code == 200

    data = response.json()

    assert "token" in data
    assert "userId" in data
    assert "message" in data

    assert isinstance(data["token"], str)
    assert len(data["token"]) > 0
    assert "Successfully" in data["message"]

    return {
        "token": data["token"],
        "userId": data["userId"]
    }