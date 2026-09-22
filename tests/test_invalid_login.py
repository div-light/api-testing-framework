def test_invalid_login(api_client):

    invalid_credentials = {
        "userEmail": "testuser77@test.com",
        "userPassword": "Test25@@!!"
    }

    response = api_client.post(
        "login/auth",
        json=invalid_credentials
    )

    print(response.status_code)
    print(response.text)