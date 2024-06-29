from typing import List


def product_of_array(nums: List) -> List:
    result = [1] * (len(nums))
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    print(product_of_array(a))
