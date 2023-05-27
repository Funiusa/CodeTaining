def is_all_upper(text: str) -> bool:
    print(text.replace(" ", ""), text.isupper())
    print(text.isupper() if len(text) and text.replace(" ", "").isalpha() else True)
    return text.isupper() if len(text) and text.replace(" ", "").isalpha() else True


if __name__ == "__main__":
    # print("Example:")
    # print(is_all_upper("ALL UPPER"))
    #
    # assert is_all_upper("ALL UPPER") == True
    # assert is_all_upper("all lower") == False
    # assert is_all_upper("mixed UPPER and lower") == False
    assert is_all_upper("") == False
