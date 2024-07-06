"""
Date - 06.07.2024
Topic - Quick Sort

Algorithm

1. Select the first element as a pivot in the list.
2. Start a pointer (the left pointer) at the second item in the list.
3. Start a pointer (the right pointer) at the last of the items
4. While the value at the left pointer in the list is lesser than pivot value, move the left pointer to the right.
   Continue the process until value at the left pointer is greater than pivot value

5. While the value at the right pointer in the list is greater that pivot value, move the right pointer to the left.
   Continue this process until the value at the right pointer is lesser than pivot value.

6. if the left pointer value is greater than or equal to the right pointer value, then swap the value at these location
    in the list
7. if left pointer and right pointer don't meet go to step


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
