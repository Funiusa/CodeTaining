def changing_direction(elements: list[int]) -> int:
    count, size, direction = 0, len(elements), None
    if size > 1:
        for i in range(size - 1):
            if elements[i] != elements[i + 1] and direction is None:
                direction = True if elements[i] < elements[i + 1] else False
            if not direction and elements[i] < elements[i + 1]:
                count += 1
                direction = True
            elif direction and elements[i] > elements[i + 1]:
                count += 1
                direction = False
    return count


if __name__ == "__main__":
    print("Example:")
    print(changing_direction([1, 2, 3, 4, 5]))
    #
    # # These "asserts" are used for self-checking
    assert changing_direction([1, 2, 3, 4, 5]) == 0
    assert changing_direction([1, 2, 3, 2, 1]) == 1

    assert changing_direction([6, 6, 6, 4, 1, 2, 5, 9, 7, 8, 5, 9, 4, 2, 6]) == 7
    assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
    assert changing_direction([3, 3, 3, 4]) == 0
    assert changing_direction([0]) == 0
