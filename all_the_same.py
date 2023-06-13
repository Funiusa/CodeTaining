from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    from more_itertools import all_equal

    return all_equal(elements)


if __name__ == "__main__":
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same([1, "a", 1]) == False
    assert all_the_same([1, 1, 1, 2]) == False
    assert all_the_same([]) == True
    assert all_the_same([1]) == True

    print("The mission is done! Click 'Check Solution' to earn rewards!")
