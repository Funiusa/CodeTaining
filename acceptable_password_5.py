def is_acceptable_password(password: str) -> bool:
    import re

    if re.search("password", password, re.IGNORECASE):
        return False
    return bool(
        len(password) > 9
        or (
            len(password) > 6
            and (re.findall("\d", password) and re.findall("\D", password))
        )
    )


if __name__ == "__main__":
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    assert is_acceptable_password("password12345") == False
    assert is_acceptable_password("PASSWORD12345") == False
    assert is_acceptable_password("pass1234word") == True
