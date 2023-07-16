from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority = None
        for num in nums:
            if count == 0:
                majority = num
            count += 1 if num == majority else -1
        return majority


if __name__ == "__main__":
    so = Solution()

    print(so.majorityElement([2, 3, 2]) == 2)
    print(so.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2)
    print(so.majorityElement([2, 3, 2, 4, 2, 2, 6, 2, 2]) == 2)
