from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                out.append("FizzBuzz")
            elif i % 3 == 0:
                out.append("Fizz")
            elif i % 5 == 0:
                out.append("Buzz")
            else:
                out.append(str(i))
        return out


if __name__ == "__main__":
    sol = Solution()
    print(sol.fizzBuzz(int(input())))
