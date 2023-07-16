class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


if __name__ == "__main__":
    so = Solution()
    assert so.multiply("2", "3") == "6"
    assert so.multiply("123", "456") == "56088"
