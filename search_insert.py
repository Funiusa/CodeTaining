from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        try:
            index = nums.index(target)
        except ValueError:
            for index, num in enumerate(nums):
                if target < num:
                    break
        return 0 if not nums else len(nums) if nums[-1] < target else index


if __name__ == "__main__":
    so = Solution()
    print(so.searchInsert([1, 2, 5, 6], 5) == 2)
    print(so.searchInsert([1, 3, 5, 6], 2) == 1)
    print(so.searchInsert([1, 3, 5, 6], 7) == 4)
    print(so.searchInsert([6], 7) == 1)
    print(so.searchInsert([], 7) == 0)
