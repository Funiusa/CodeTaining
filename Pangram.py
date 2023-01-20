"""
    A pangram (Greek: παν γράμμα, pan gramma, "every letter")
    or holoalphabetic sentence for a given alphabet is a sentence
    using every letter of the alphabet at least once.
    Perhaps you are familiar with the well known
    pangram "The quick brown fox jumps over the lazy dog".

    For this mission, we will use the latin alphabet (A-Z).
    You are given a text with latin letters and punctuation symbols.
    You need to check if the sentence is a pangram or not.
    Case does not matter.

    Input: A text as a string.

    Output: Whether the sentence is a pangram or not as a boolean.
"""

alphabet = list('abcdefghijklmnopqrstuvwxyz')


def check_pangram(text: str) -> bool:
    text = sorted(set(let.lower() for let in list(text) if let.isalpha()))
    return alphabet == text
