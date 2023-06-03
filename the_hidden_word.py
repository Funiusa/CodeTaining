def checkio(text, word):
    lines = ["".join(line.split()) for line in text.split("\n")]
    for line in lines:
        print(line)
    return [1, 1, 1, 4]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    checkio(
        """DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""",
        "ten",
    )
