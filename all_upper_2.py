def is_all_upper(text: str) -> bool:
    import re

    text = text.replace(" ", "")
    upper_list = re.findall("\S[A-Z\d]+", text)
    return upper_list == text.split() if text and re.search("\D", text) else False


if __name__ == "__main__":
    assert is_all_upper("ALL UPPER") == True
    assert is_all_upper("all lower") == False
    assert is_all_upper("mixed UPPER and lower") == False
    assert is_all_upper("") == False
    assert is_all_upper("     ") == False
    assert is_all_upper("123") == False
    assert is_all_upper("DIGITS123") == True
