from functools import wraps
from time import sleep
from typing import Callable


def long_repeat(line: str) -> int:
    """
    length the longest substring that consists of the same char
    """
    max_len = 0
    sub = ""
    for i in range(len(line) - 1):
        sub += line[i]
        if line[i + 1] != line[i]:
            max_len = max(max_len, len(sub))
            sub = ""

    return max_len


def gen():
    num = 0
    while num < 10:
        yield num
        num += 1


class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        return self.data**2


def decorate(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args)
        if isinstance(result, list):
            return list(map(lambda x: -x, result))

    return wrapper


@decorate
def odd(num: int) -> list:
    max()
    return [elem if num > 0 else -elem for elem in range(abs(num)) if elem % 2 == 0]


# def test_odd():
#     print(odd(-2))
#     assert odd(-8) == [0, 2, 4, 6]
#     assert odd(10) == [0, -2, -4, -6, -8]
#     # assert odd(10) != [1, 2, 3, 4, 5]
#     # assert odd(-8) == [0, -2, -4, -6]


if __name__ == "__main__":
    print("Example:")
    print(odd(10))
    print(odd(-8))

    # test_odd()

    # assert long_repeat('aa') == 2
    # print(long_repeat("sdsffffse"))
    #
    # assert long_repeat("sdsffffse") == 4
    # assert long_repeat("ddvvrwwwrggg") == 3
    #
    # print("The mission is done! Click 'Check Solution' to earn rewards!")
