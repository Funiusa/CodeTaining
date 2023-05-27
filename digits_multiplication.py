def checkio(number: int) -> int:
    result = 1
    for n in str(number):
        if n != "0":
            result *= int(n)
    return int(result)


if __name__ == "__main__":
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
