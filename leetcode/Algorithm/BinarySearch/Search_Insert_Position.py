"""
This approach was without using Binary Search
Time Complexity - O(1)
"""


def searchInsertPosition(nums, target):
    nums.append(target)
    nums.sort()
    return nums.index(target)


def searchInsertPositionBS(num, t):




if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    print(searchInsertPosition(nums, target))
