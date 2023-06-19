def runningSum(nums):
    return [index + 1 for index, e in enumerate(nums)]


if __name__ == "__main__":
    nums = [3, 1, 2, 10, 1]
    print(runningSum(nums))
    nums = [1, 1, 1, 1, 1]
    print(runningSum(nums))
