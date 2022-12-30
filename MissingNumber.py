""" 
    You are given a list of integers, which are elements of arithmetic progression -
    the difference between the consecutive elements is constant.
    But this list is unsorted and one element is missing...good luck!

    Input: List of integers.

    Output: Integer.
"""


def missing_number(items: list[int]) -> int:
    size = len(items)
    if size > 2:
        d = sorted(items, reverse=True)
        for i in range(size - 1):
            first, second = d[i] - d[i + 1], d[i + 1] - d[i + 2]
            if first < second:
                return d[i + 1] - first
            elif first > second:
                return d[i + 1] + second
    return 0
