from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count_val = nums.count(val)
        for _ in range(count_val):
            nums.remove(val)
        return len(nums)
        # nums[:] = [x for x in nums if x != val]


if __name__ == "__main__":
    so = Solution()
    print(so.removeElement(nums=[3, 2, 2, 3], val=3))
    print(so.removeElement(nums=[3, 3], val=3))
    print(so.removeElement(nums=[3], val=3))
    print(so.removeElement(nums=[2], val=3))
    print(so.removeElement(nums=[], val=3))
    print(so.removeElement(nums=[1, 2, 4, 5, 6], val=3))
    print(so.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
