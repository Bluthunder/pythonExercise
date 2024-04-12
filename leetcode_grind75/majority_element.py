"""
Date - 12 April 2024
LeetCode Grind 75 Question: 8
DSA Topic - Array, Boyer's Moore Algorithm

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

"""


# This uses hashmap with O(n)
def majority_element_HM(nums: list[int]) -> int:
    count = {}
    res, max_count = 0, 0

    for n in nums:
        count[n] = 1 + count.get(n, 0)
        res = n if count[n] > max_count else res
        max_count = max(count[n], max_count)

    return res


# This method uses Boyer's Moore Voting Algorithm
def majority_element_BMV(nums: list[int]) -> int:
    res, count = 0, 0

    for n in nums:
        if count == 0:
            res = n
        count += (1 if n == res else -1)

    return res


"""
This Method uses the fact in any sorted array, majority element would occur > n/2 times, where n is length
of the array. So Majority element would occur at n/2 th index

"""


def majority_element(nums: list[int]) -> int:
    nums = sorted(nums)
    return nums[len(nums) // 2]


if __name__ == '__main__':
    a = [2, 2, 1, 1, 1, 2, 2]
    print(majority_element_HM(a))

    print(majority_element_BMV(a))

    print(majority_element(a))
