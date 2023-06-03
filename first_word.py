def first_word(text: str) -> str:
    import re

    first = re.match("\w+", text)
    return first.group(0)


if __name__ == "__main__":
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    # assert first_word("") == ""
    print("Coding complete? Click 'Check' to earn cool rewards!")
