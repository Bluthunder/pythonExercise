"""
Date - 06.07.2024

Topic - Sorting

Given an array A[0 ... n-1] of n numbers containing the repetition of some numbers. Give an algorithm for checking
whether there are repeated elements or not.
"""

import time


def checkDuplicatesBruteForce(A):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] == A[j]:
                print(f'Duplicate exists at ---> {A[i]}')
                return

    print(f'No Duplicate exists')


def checkDuplicates(A):
    A.sort()
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] == A[i+1]:
                print(f'Duplications exists at --> {A[i]}')
                return
    print(f'No Duplicate exists')


if __name__ == '__main__':
    arr = [0, 5, 7, 4, 3, 1, 9, 4]
    # checkDuplicatesBruteForce(arr)
    checkDuplicates(arr)