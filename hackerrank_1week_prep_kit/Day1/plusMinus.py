#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    l = len(arr)
    cPos = cNeg = cZero = 0

    for i in range(l):
        if arr[i] > 0:
            cPos += 1
        elif arr[i] < 0:
            cNeg += 1
        else:
            cZero += 1

    print(f'{cPos / l:.6f}')
    print(f'{cNeg / l:.6f}')
    print(f'{cZero / l:.6f}')


if __name__ == '__main__':
    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))
    arr = [-4, 3, -9, 0, 4, 1]

    plusMinus(arr)
