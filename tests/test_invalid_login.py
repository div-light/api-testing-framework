from test_data.test_data import INVALID_LOGINS
from utilities.assertions import assert_status_code
import pytest

@pytest.mark.parametrize(
    "email, password, expected_status",
    INVALID_LOGINS
)
def test_invalid_login(api_client, email, password, expected_status):

    payload = {
        "userEmail": email,
        "userPassword": password
    }

    response = api_client.post(
        "auth/login",
        json=payload
    )

    assert_status_code(response, expected_status)