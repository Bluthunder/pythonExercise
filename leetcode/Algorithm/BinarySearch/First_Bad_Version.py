"""
Find first bad version of the API
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

"""


# Sample function which was defined already in Leetcode
def isBadVersion(mid):
    pass


def firstBadVersion(n):
    left, right, result = 1, n, 1

    while left <= right:
        mid = (left + right) // 2
        if not isBadVersion(mid):
            left = mid + 1
        else:
            right = mid - 1
            result = mid
    return result
