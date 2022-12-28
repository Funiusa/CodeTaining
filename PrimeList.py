from datetime import datetime
from math import sqrt


def prime(base_number):
    count = []
    for num in range(2, base_number):
        flag = True
        for n in range(2, int(sqrt(num)) + 1):
            if num % n == 0:
                flag = False
                break
        if flag:
            count.append(num)
    return len(count)


if __name__ == "__main__":
    base = int(input("Insert number here: "))

    start = datetime.now()
    print(f"{prime(base)} - prime numbers before your {base}")
    end = datetime.now()
    print(f"Speed: {end - start}")
