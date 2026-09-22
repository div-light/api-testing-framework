VALID_LOGIN = {
    "userEmail": "testuser77@test.com",
    "userPassword": "Test25@@!!"
}

INVALID_LOGINS = [
    ("invalid@test.com", "wrong_password", 400),
    ("", "Test25@@!!", 400),
    ("testuser77@test.com", "", 400)
]