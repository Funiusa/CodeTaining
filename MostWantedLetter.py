"""
    You are given a text, which contains different English letters and punctuation symbols.
    You should find the most frequent letter in the text.
    The letter returned must be in lower case.
    While checking for the most wanted letter,
    casing does not matter, so for the purpose of your search,
    "A" == "a". Make sure you do not count punctuation symbols,
    digits and whitespaces, only letters.


    If you have two or more letters with the same frequency,
    then return the letter which comes first in the Latin alphabet.
    For example -- "one" contains "o", "n", "e" only once for each,
    thus we choose "e".

    Input: A text for analysis as a string.

    Output: The most frequent letter in lower case as a string.
"""


# TODO upgrade this it is too slow


def most_wanted_letters(text: str) -> str:
    letters = sorted([let.lower() for let in text if let.isalpha()])
    return sorted(letters, reverse=True, key=lambda l: letters.count(l))[0]
