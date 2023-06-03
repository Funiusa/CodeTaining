def switch_strings(line: str, result: str) -> bool:
    test, count = "", 0
    line_size = len(line)
    if len(result) == line_size and sorted(line) == sorted(result):
        for i in range(line_size):
            if result[i] == line[i]:
                test += line[i]
            elif count < 2:
                test += result[i]
                count += 1
    return test == result


if __name__ == "__main__":
    print("Example:")
    assert switch_strings("bodep", "bopep") == False
    assert switch_strings("abracadabra", "badaboom") == False
    print(switch_strings("btry", "byrt"))

    # These "asserts" are used for self-checking
    assert switch_strings("btry", "byrt") == True
    assert switch_strings("boss", "boss") == True
    assert switch_strings("solid", "disel") == False
    assert switch_strings("false", "flaes") == False
    assert switch_strings("true", "treu") == True

    print("The mission is done! Click 'Check Solution' to earn rewards!")
