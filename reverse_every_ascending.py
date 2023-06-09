from collections.abc import Iterable


def reverse_ascending(items: list[int]) -> Iterable[int]:
    result = []
    size, j = len(items), 0
    for i in range(1, size + 1):
        if i == size or items[i - 1] >= items[i]:
            result.extend(items[j:i][::-1])
            j = i
    return result


if __name__ == "__main__":
    print("Example:")
    print(list(reverse_ascending([1, 2, 3, 4, 5])))

    # These "asserts" are used for self-checking
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
        10,
        7,
        5,
        4,
        8,
        7,
        2,
        3,
        1,
    ]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]

    print("The mission is done! Click 'Check Solution' to earn rewards!")
