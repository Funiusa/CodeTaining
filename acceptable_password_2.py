def is_acceptable_password(password: str) -> bool:
    import re

    return len(password) > 6 and len(re.findall("\d", password))


if __name__ == "__main__":
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
