class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin((int(a, 2) + int(b, 2)))[2:]


if __name__ == "__main__":
    so = Solution()
    assert so.addBinary("11", "1") == "100"
    assert so.addBinary("1010", "1011") == "10101"
