from typing import List

"""
Incomplete
"""
def maxProduct(nums: List[int]) -> int:
    maxP = nums[0]
    curP = 1
    if 0 in nums:
        nums.remove(0)

    for i in nums:
        if i < 0:
            curP = 1
        curP *= i
        maxP = max(curP, maxP)

    return maxP


if __name__ == '__main__':
    arr = [0, 2]

    print(maxProduct(arr))