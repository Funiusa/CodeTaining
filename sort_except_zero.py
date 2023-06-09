from collections.abc import Iterable
from itertools import takewhile


def zero(num):
    return True if num == 0 else False


def except_zero(items: list[int]) -> Iterable[int]:
    zero_indexes = [i for i, item in enumerate(items) if item == 0]
    items.sort()
    items = items[len(zero_indexes):]
    for index in zero_indexes:
        items.insert(index, 0)
    return items

    # zero_indexes = [i for i, item in enumerate(items) if item == 0]
    #
    # for i in range(items.count(0)):
    #     items.remove(0)
    # items.sort()
    # for index in zero_indexes:
    #     items.insert(index, 0)
    #
    # return items


if __name__ == "__main__":
    print("Example:")
    print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

    # These "asserts" are used for self-checking
    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0,
                                                              7]
    assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    assert list(except_zero([0, 0])) == [0, 0]

    print("The mission is done! Click 'Check Solution' to earn rewards!")
