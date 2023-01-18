"""
    Let's continue examining words.
    You are given two strings with words separated by commas.
    Try to find what is common between these strings.
    The words in the same string don't repeat.

    Your function should find all of the words that appear in both strings. The result must be represented as a string of words separated by commas in alphabetic order.

    Input: Two arguments as strings.

    Output: The common words as a string.
"""


def common_words(line1: str, line2: str) -> str:
    return ','.join(sorted(set(line1.split(',')) & set(line2.split(','))))
