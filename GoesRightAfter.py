"""
 In a given word you need to check if one symbol goes only right after another.

Cases you should expect while solving this challenge:

    one of the symbols is not in the given word - your function should return False;
    any symbol appears in a word more than once - use only the first one;
    two symbols are the same - your function should return False;
    the condition is case sensitive, which means 'a' and 'A' are two different symbols.

Input: Three arguments. The first one is a given string, second is a symbol that should go first, and the third is a symbol that should go after the first one.

Output: A bool

"""


def goes_after(word: str, first: str, second: str) -> bool:
    if (first in word) and (second in word) and first != second:
        return word.index(second) - word.index(first) == 1
    return False
