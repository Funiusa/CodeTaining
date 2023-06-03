def caps_lock(text: str) -> str:
    goe_text = ""
    caps = False
    for letter in text:
        if letter == "a":
            pass
        elif caps:
            goe_text += letter.upper()
        else:
            goe_text += letter

    return goe_text


if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
    print("Coding complete? Click 'Check' to earn cool rewards!")
