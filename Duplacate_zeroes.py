def duplicate_zeros(arr: list) -> list:
    duplicates = []
    i, size = 0, len(arr)
    while i < size:
        if arr[i] == 0:
            duplicates.append(0)
            duplicates.append(0)
        else:
            duplicates.append(arr[i])
        i += 1
    arr.clear()
    arr.extend(duplicates[:size])

    return arr


if __name__ == "__main__":
    print("Example:")
    a = [1, 0, 2, 3, 0, 4, 5, 0]
    print(duplicate_zeros(a))
    a = [1, 0, 0, 3, 0, 4, 5, 0]
    print(duplicate_zeros(a))
    a = [0, 0, 0, 3, 0, 4, 5, 0]
    print(duplicate_zeros(a))
    a = [0, 0]
    print(duplicate_zeros(a))
    a = [0]
    print(duplicate_zeros(a))
    a = []
    print(duplicate_zeros(a))
    a = [1]
    print(duplicate_zeros(a))
    # if tmp[i] == 0:
    #     count += 1
    # else:
    #     if arr[i - 1] == 0:
    #         tmp += [0] * (count + count)
    #         count = 0
    #     tmp.append(arr[i])
# tmp += [0] * (count + count)
