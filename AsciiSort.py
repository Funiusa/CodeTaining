from datetime import datetime


def ascii_sort(uns_list: list) -> list:
    """ Bubbles sorted """
    size, i, j = len(uns_list), 0, 0
    while i + 1 < size:
        j = 0
        while j + 1 < size - i:
            if uns_list[j + 1] < uns_list[j]:
                uns_list[j], uns_list[j + 1] = uns_list[j + 1], uns_list[j]
            j += 1
        i += 1
    return uns_list


def ascii_shake(ushake_l: list) -> list:
    """ Shake sort """
    left, right = 0, len(ushake_l) - 1
    while left <= right:
        i = right
        while i > left:
            if ushake_l[i - 1] > ushake_l[i]:
                ushake_l[i], ushake_l[i - 1] = ushake_l[i - 1], ushake_l[i]
            i -= 1
        left += 1

        i = left
        while i < right:
            if ushake_l[i] > ushake_l[i + 1]:
                ushake_l[i], ushake_l[i + 1] = ushake_l[i + 1], ushake_l[i]
            i += 1
        right -= 1
    return ushake_l


def ascii_insertion_sort(uinsrt_l: list) -> list:
    print(uinsrt_l)
    for i in range(1, len(uinsrt_l)):
        x, j = uinsrt_l[i], i
        while j > 0 and uinsrt_l[j - 1] > x:
            uinsrt_l[j] = uinsrt_l[j - 1]
            j -= 1
        uinsrt_l[j] = x
    return uinsrt_l


def ascii_choice_sort(uch_l: list) -> list:
    b, e = 0, len(uch_l) - 1
    while b != e:
        j = min(uch_l[b], uch_l[e])
        uch_l[b], uch_l[e] = j, uch_l[b]
        b += 1

    return uch_l
