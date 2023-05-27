def is_acceptable_password(password: str) -> bool:
    import re

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
