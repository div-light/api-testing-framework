def assert_status_code(response, expected_status):
    assert response.status_code == expected_status