def min(*args, **kwargs):
    key = kwargs.get("key", None)
    print(type(args))
    if len(args) > 1:
        m = args[0]
        for i in range(1, len(*args)):
            if m > args[i]:
                m = args[i]
        return m
    return args


def max(*args, **kwargs):
    tmp = args
    key = kwargs.get("key", None)
    size = 0
    try:
        size = len(*tmp)
    except TypeError:
        size = len(tmp)
    if size > 1:
        if key:
            tmp = tuple(key(arg) for arg in args)
        m = 0
        for i in range(1, size):
            if tmp[m] < tmp[i]:
                m = i
        return args[m]
    return args[0]


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # print(max([2, 1], [3, 4]))
    print(max([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))
    print(max(3.1, 2.5, key=int))
    # print(max())
    # assert max(3, 2) == 3, "Simple case max"
    # assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
