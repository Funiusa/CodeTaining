def checkio(expression: str) -> bool:
    opening_brackets = "{[("
    closing_brackets = "}])"
    stack = []

    for bracket in expression:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not stack:
                return False
            top = stack.pop()
            if opening_brackets.index(top) != closing_brackets.index(bracket):
                return False
    return len(stack) == 0


if __name__ == "__main__":
    print("Example:")
    print(checkio("((5+3)*2+1)"))

    assert checkio("((5+3)*2+1)") == True
    assert checkio("{[(3+1)+2]+}") == True
    assert checkio("(3+{1-1)}") == False
    assert checkio("[1+1]+(2*2)-{3/3}") == True
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
    assert checkio("[(3)+(-1)]*{3}") == True
    assert checkio("(((([[[{{{3}}}]]]]))))") == False
    assert checkio("[1+202]*3*({4+3)}") == False
    assert checkio("({[3]})-[4/(3*{1001-1000}*3)/4]") == True
    assert checkio("[[[1+[1+1]]])") == False
    assert checkio("(((1+(1+1))))]") == False
    assert checkio("2+3") == True
