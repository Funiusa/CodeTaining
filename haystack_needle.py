import re


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1
        # return haystack.find(needle)


if __name__ == "__main__":
    so = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    print(so.strStr(haystack, needle))
    haystack = "leetcode"
    needle = "leeto"
    print(so.strStr(haystack, needle))
    haystack = "butsadbar"
    needle = "sad"
    print(so.strStr(haystack, needle))
