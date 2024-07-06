"""
Date - 06.07.2024
Topic - Quick Sort

"""


def quickSort(A, l, r):
    if l < r:
        partition_point = partition(A, l, r)
        quickSort(A, l, partition_point - 1)
        quickSort(A, partition_point + 1, r)
    return A


def partition(A, low, high):
    pivot = A[low]
    left = low + 1
    right = high
    done = False

    while not done:

        while left <= right and A[left] <= pivot:
            left += 1

        while right >= left and A[right] >= pivot:
            right -= 1

        if right < left:
            done = True
        else:
            A[left], A[right] = A[right], A[left]

    A[low], A[right] = A[right], A[low]

    return right


if __name__ == '__main__':
    arr = [10, 4, 43, 5, 57, 91, 45, 9, 7]
    print(f'Sorted Array using Insertion Sort ===>> {quickSort(arr, 0, len(arr) - 1)}')
