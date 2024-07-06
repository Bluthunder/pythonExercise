"""
Date - 06.07.2024
Topic - Merge Sort

"""

def mergeSort(A):
    n = len(A)
    if n > 1:
        mid = n//2
        left_half = A[:mid]
        right_half = A[mid:]
        mergeSort(left_half)
        mergeSort(right_half)

        i = j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                A[k] = left_half[i]
                i += 1
            else:
                A[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            A[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            A[k] = right_half[j]
            j += 1
            k += 1
    return A

if __name__ == "__main__":

    arr = [10, 4, 43, 5, 57, 91, 45, 9, 7]

    print(f'Sorted Array using Insertion Sort ===>> {mergeSort(arr)}')

