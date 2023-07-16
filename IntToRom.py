roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def roman_to_arabian(rom: str) -> int:
    arabian = 0
    prev_value = 0
    for value in reversed(list(rom.upper())):
        value = roman[value]
        if value < prev_value:
            arabian -= value
        else:
            arabian += value
        prev_value = value
    return arabian


if __name__ == "__main__":
    print(roman_to_arabian(input()))
