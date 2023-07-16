from typing import List
from itertools import groupby


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums.clear()
        nums.extend(sorted(nums_set))
        return len(nums)

    def print_element_count(self, line: str) -> None:
        if line:
            count = 1
            for i in range(len(line) - 1):
                if line[i] == line[i + 1]:
                    count += 1
                else:
                    print(f"{count}{line[i]}", end="")
                    count = 1
            print(f"{count}{line[-1]}")


if __name__ == "__main__":
    so = Solution()
    nums = [1, 1, 2]
    print(so.removeDuplicates(nums=nums))
    print(nums)

    so.print_element_count("abf")
    so.print_element_count("aaabbbfff")
    so.print_element_count("aewaadfff")
    so.print_element_count("")
    so.print_element_count("a")
