def reveal_num(line: str) -> int | float | None:
    num = ""
    point = zero = negative = False
    for elem in line:
        if elem.isdigit():
            num += elem
        elif elem in ("-", "+") and not num:
            negative = elem == "-"
        elif elem == "." and not point:
            point = True
            if not num:
                zero = True
            num += elem
    if num and num[-1] == ".":
        point = False
        num = num[:-1]
    if zero and num[-1].isdigit():
        num = "0" + num
    if num:
        num = float(num) if point else int(num)
        return -num if negative else num

    return None


if __name__ == "__main__":
    print("Example:")
    assert reveal_num("v-Iu*B&9viteApr=0k}=") == -90
    assert reveal_num("^P!Njz.Tz:GxC}№I.v);y1") == 0.1
    print(reveal_num("-"))
    print(reveal_num("3"))
    print(reveal_num(".a.2..dfg"))
    print(reveal_num("+A%+-1-0..."))

    # These "asserts" are used for self-checking
    assert reveal_num("F0(t}") == 0
    assert reveal_num("Utc&g") == None
    assert reveal_num("-aB%|_-+2ADS.12+3.ADS1.2") == 2.12312
    assert reveal_num("-aB%|_+-2ADS.12+3.ADS1.2") == -2.12312
    assert reveal_num("zV№1}3;o.vEf``C.WqTY0") == 13.0
    assert (
        reveal_num("!3B'j=(}89JQ6aWvN*%5@uy.r)B<?pZ.!545ZD^KF9Sx@gqfa*") == 38965.5459
    )

    print("The mission is done! Click 'Check Solution' to earn rewards!")
