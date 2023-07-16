from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        size = len(arr) - 1
        for i in range(size):
            j = size
            while j != i:
                if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]:
                    return True
                j -= 1
        return False


if __name__ == "__main__":
    so = Solution()
    arr = [0, 0]
    print(so.checkIfExist(arr))
    arr = [10, 2, 5, 3]
    print(so.checkIfExist(arr))
    arr = [3, 1, 7, 11]
    print(so.checkIfExist(arr))
    arr = [7, 1, 14, 11]
    print(so.checkIfExist(arr))
    arr = [-2, 0, 10, -19, 4, 6, -8]
    print(so.checkIfExist(arr))
