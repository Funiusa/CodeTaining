def duplicate_zeros(donuts: list) -> list:
    retList = []
    count = 0
    size = len(donuts)
    for i in range(size):
        if donuts[i] == 0:
            count += 1
        else:
            if donuts[i - 1] == 0:
                retList += [0] * (count + count)
                count = 0
            retList.append(donuts[i])
    retList += [0] * (count + count)
    return retList


if __name__ == "__main__":
    print("Example:")
    print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))
