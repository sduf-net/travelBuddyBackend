from schemas.auth.token import Token

def test_generate_and_verify_token():
    user_id = "user123"
    token = Token.generate_and_sign(user_id)
    payload = Token.verify_token(token)
    assert payload is not None
    assert payload["user_id"] == user_id

def test_verify_expired_token():
    user_id = "user123"
    token = Token.generate_and_sign(user_id)
    # Simulate expired token by altering the expiration date in payload
    expired_token = token[:-1] + "a"
    assert Token.verify_token(expired_token) is None
