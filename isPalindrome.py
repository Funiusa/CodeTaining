class Solution:
    def is_palindrome(self, x: int) -> bool:
        xToStr = str(x)
        middle = len(xToStr) // 2
        print(xToStr[::-1])
        for i in range(middle):
            if xToStr[i] != xToStr[-(i + 1)]:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.is_palindrome(int(input())))