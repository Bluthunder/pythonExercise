"""
Date - 06.07.2024
Topic: Sorting
"""


def findMax(A):
    counter = max_counter = 0
    candidate = A[0]

    for i in range(len(A)):
        counter = 1
        for j in range(i + 1, len(A)):
            if A[i] == A[j]:
                counter += 1

        if counter > max_counter:
            max_counter = counter
            candidate = A[i]

    print(f'candidate {candidate} appeared {max_counter} times')


def checkMax(arr):
    arr.sort()
    counter = max_counter = 0
    candidate = max_candidate = 0

    for i in range(len(arr)):
        if arr[i] == candidate:
            counter += 1
        else:
            counter = 1
            candidate = arr[i]

        if counter > max_counter:
            max_counter = counter
            max_candidate = arr[i]

    print(f'candidate {max_candidate} appeared {max_counter} times')




if __name__ == '__main__':
    arr = [3, 2, 1, 2, 2, 4]
    findMax(arr)
