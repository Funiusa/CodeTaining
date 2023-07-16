from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = "".join(map(str, digits))
        digit = int(str_digits) + 1
        return list(map(int, str(digit)))


if __name__ == "__main__":
    so = Solution()
    print(so.plusOne([3, 2, 9]))
    print(so.plusOne([3, 2, 1]))
    print(so.plusOne([9]))
