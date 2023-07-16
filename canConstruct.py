class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        liNote = [i for i in ransomNote]
        for elem in magazine:
            if elem in liNote:
                liNote.remove(elem)
        if len(liNote) == 0:
            return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct("aa", "ba"))