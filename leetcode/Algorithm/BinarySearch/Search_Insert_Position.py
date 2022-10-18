"""
This approach was without using Binary Search
Time Complexity - O(1)
"""


def searchInsertPosition(nums, target):
    nums.append(target)
    nums.sort()
    return nums.index(target)


def searchInsertPositionBS(numbers, t):
    start, end = 0, len(numbers) - 1
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    # print(searchInsertPosition(nums, target))
    print(searchInsertPositionBS(nums, target))


