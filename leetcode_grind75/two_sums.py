"""
Date - 8th April 2024
Leetcode Grind 75 Question : 1
DSA Topic: Array
"""
from typing import List


def two_sums(nums: List[int], target: int) -> List[int]:
    a = 0
    for i in range(len(nums)):
        p = target - nums[i]
        if p in nums:
            a = nums.index(p)
            if a == i:
                continue
            break
    return i, a


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    print(two_sums(nums, target))
