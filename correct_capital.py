def correct_capital(line: str) -> bool:
    if all(list(map(lambda x: x.islower(), line))):
        return True
    lower = all(list(map(lambda x: x.islower(), line[1:])))
    upper = all(list(map(lambda x: x.isupper(), line[1:])))
    return line[0].isupper() and any([lower, upper])


if __name__ == "__main__":
    print("Example:")
    print(correct_capital("CheCkio"))
    print(correct_capital("Checkio"))
    print(correct_capital("CHECKIO"))
    assert correct_capital("cHECKIO") == False

    assert correct_capital("checkio") == True
    # These "asserts" are used for self-checking
    assert correct_capital("Checkio") == True
    assert correct_capital("CheCkio") == False
    assert correct_capital("CHECKIO") == True

    print("The mission is done! Click 'Check Solution' to earn rewards!")
