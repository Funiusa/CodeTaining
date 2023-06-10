def how_deep(structure: tuple) -> int:
    deep = 1
    for elem in structure:
        count = 1
        count += how_deep(elem) if isinstance(elem, tuple) else 0
        deep = count if count > deep else deep
    return deep


if __name__ == "__main__":
    print("Example:")
    # These "asserts" are used for self-checking
    assert how_deep((((), (), ()),)) == 3
    assert how_deep((1, 2, 3)) == 1
    assert how_deep((1, 2, (3,))) == 2
    assert how_deep((1, 2, (3, (4,)))) == 3
    assert how_deep(()) == 1
    assert how_deep(((),)) == 2
    assert how_deep((((),),)) == 3
    assert how_deep((1, (2,), (3,))) == 2
    assert how_deep((1, ((),), (3,))) == 3

    print("The mission is done! Click 'Check Solution' to earn rewards!")
