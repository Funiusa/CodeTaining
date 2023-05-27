def is_ascending(items: list[int]) -> bool:
    if items:
        prev = items[0]
        for i in range(1, len(items)):
            cur = items[i]
            if prev < cur:
                prev = cur
            else:
                return False
    return True


if __name__ == "__main__":
    print(is_ascending([-5, 10, 99, 123456]))

    # These "asserts" are used for self-checking
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    assert is_ascending([1, 3, 3, 5]) == False
