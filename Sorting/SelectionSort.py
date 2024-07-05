"""
Date: 05.07.2024
Topic - DSA

Selection sort
Time Complexity - O(n^2)
"""

def selectionSort(arr: list)->list:

    for i in range(len(arr)-1, 0, -1):
        pos_of_largest = 0
        for j in range(1, i+1):
            if arr[j] > arr[pos_of_largest]:
                pos_of_largest = j
            arr[i], arr[pos_of_largest] = arr[pos_of_largest], arr[i]

    return arr


if __name__ == "__main__":

    arr = [10, 4, 43, 5, 57, 91, 45, 9, 7]

    print(f'Sorted Array using selection Sort ===>> {selectionSort(arr)}')