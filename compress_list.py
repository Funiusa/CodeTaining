from collections.abc import Iterable


def compress(items: list[int]) -> Iterable[int]:
    tmp = None
    for item in items:
        if item != tmp:
            yield item
        tmp = item
    # result = [] if not items else [items[0]]
    # result.extend([items[i] for i in range(1, len(items)) if items[i - 1] != items[i]])
    # return result


if __name__ == "__main__":
    print("Example:")
    print(list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])))

    # These "asserts" are used for self-checking
    assert list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])) == [
        5,
        4,
        5,
        6,
        5,
        7,
        8,
        0,
    ]
    assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
    assert list(compress([7, 7])) == [7]
    assert list(compress([])) == []
    assert list(compress([1, 2, 3, 4])) == [1, 2, 3, 4]
    assert list(compress([9, 9, 9, 9, 9, 9, 9])) == [9]
    assert list(compress([9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9])) == [9, 0, 9]

    print("The mission is done! Click 'Check Solution' to earn rewards!")
