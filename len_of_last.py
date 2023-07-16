class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = s.split()[-1]
        return len(last)


if __name__ == "__main__":
    os = Solution()
    print(os.lengthOfLastWord("Hello world"))
    print(os.lengthOfLastWord("   fly me   to   the moon  "))
    print(os.lengthOfLastWord("luffy is still joyboy"))
