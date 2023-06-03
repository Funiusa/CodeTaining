from typing import Any, Iterable


def split_list(items: list[Any]) -> Iterable[list[Any]]:
    size = len(items)
    middle = size // 2 if size % 2 == 0 else size // 2 + 1
    return [items[:middle], items[middle:]]


if __name__ == "__main__":
    print("Example:")
    print(list(split_list([1, 2, 3, 4, 5, 6, 5])))

    assert list(split_list([1, 2, 3, 4, 5, 6])) == [[1, 2, 3], [4, 5, 6]]
    assert list(split_list([1, 2, 3])) == [[1, 2], [3]]
    assert list(split_list(["banana", "apple", "orange", "cherry", "watermelon"])) == [
        ["banana", "apple", "orange"],
        ["cherry", "watermelon"],
    ]
    assert list(split_list([1])) == [[1], []]
    assert list(split_list([])) == [[], []]
