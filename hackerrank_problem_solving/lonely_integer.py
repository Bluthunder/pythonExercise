# Accepts array of integer as input and returns the elements which occurs only once

# XOR operation with same number gives 0 and XOR with another number gives number itself
from functools import reduce


def lonelyInteger(arr):
    return reduce((lambda x, y: x ^ y), arr)


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = lonelyInteger(a)
    print(result)
