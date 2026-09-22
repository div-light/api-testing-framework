from config.config import USERNAME, PASSWORD
from utilities.assertions import assert_status_code


def test_valid_login(api_client):

    payload = {
        "userEmail": USERNAME,
        "userPassword": PASSWORD
    }

    response = api_client.post(
        "auth/login",
        json=payload
    )

    assert_status_code(response, 200)

    data = response.headers
    assert "application/json" in data["Content-Type"]
