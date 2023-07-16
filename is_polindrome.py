class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = "".join(list(filter(lambda x: x.isalpha() or x.isdigit(), s.lower())))
        return cs == cs[::-1]
        # clear_s = "".join((let for let in s.lower() if let.isalpha() or let.isdigit()))
        # print(clear_s)
        # return clear_s == clear_s[::-1]


if __name__ == "__main__":
    os = Solution()
    s = "A man, a plan, a canal: Panama"
    print(os.isPalindrome(s))
    print(os.isPalindrome(" "))
    print(os.isPalindrome("0P"))
