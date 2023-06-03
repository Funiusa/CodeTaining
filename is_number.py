def is_number(val: str) -> bool:
    try:
        return bool(int(val))
    except ValueError:
        return False


if __name__ == "__main__":
    print("Example:")
    print(is_number("34"))

    # These "asserts" are used for self-checking
    assert is_number("34") == True
    assert is_number("df") == False
    assert is_number("") == False
    assert is_number("a5") == False
    assert is_number("ITS A NUMBER") == False
    assert is_number("5a") == False

    print("The mission is done! Click 'Check Solution' to earn rewards!")
