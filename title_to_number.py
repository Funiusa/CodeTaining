class Solution:
    alpha = {}

    def __init__(self):
        self.create_alpha()

    @property
    def alpha_len(self):
        return len(self.alpha)

    def create_alpha(self) -> None:
        self.alpha = {chr(ord("A") + i): i + 1 for i in range(26)}

    def titleToNumber(self, columnTitle: str) -> int:
        size = len(columnTitle) - 1
        number = j = 0
        for i in range(size, -1, -1):
            let = columnTitle[j]
            number += self.alpha[let] * pow(self.alpha_len, i)
            j += 1

        return number


if __name__ == "__main__":
    so = Solution()
    # print(so.titleToNumber("A") == 1)
    # print(so.titleToNumber("Z") == 26)
    print(so.titleToNumber("AZ") == 52)
    print(so.titleToNumber("BA") == 53)
    # print(so.titleToNumber("ZY") == 701)
    # print(so.titleToNumber("YZ") == 676)
    # print(so.titleToNumber("ZA") == 677)
    # print(so.titleToNumber("ZX") == 700)
    # print(so.titleToNumber("ZZ") == 702)
    print(so.titleToNumber("AAA") == 703)
    print(so.titleToNumber("AAZ") == 728)
    print(so.titleToNumber("ABA") == 729)
    print(so.titleToNumber("AA") == 27)
    print(so.titleToNumber("AB") == 28)
