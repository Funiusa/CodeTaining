from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> list:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    tmp = nums1[:m]
    nums1.clear()
    nums1.extend(sorted(tmp + nums2[:n]))

    return nums1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(merge(nums1, m, nums2, n))
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print(merge(nums1, m, nums2, n))
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(merge(nums1, m, nums2, n))
