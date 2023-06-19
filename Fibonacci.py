def fi(n):
    tmp = 0
    tmp1 = 1
    out = 0
    while out < n:
        if n == 1:
            return 1
        out = out + tmp
        tmp = tmp1
        tmp1 = out
    return tmp


def fib(n):
    if n == 0:
        return 0
    print(fi(abs(n - 1))), print(fi(abs(n - 2)))
    #print(fi(abs(n - 1)) + fi(abs(n - 2)))


if __name__ == "__main__":
    fib(int(input()))