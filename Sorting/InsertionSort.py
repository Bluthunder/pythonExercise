"""
Date - 05.07.2024
Topic - Inserstion Sort

"""

def insertionSort(arr: list)->list:
    for i in range(1, len(arr)):
        key = arr[i]
        k = i

        while k > 0 and key < arr[k-1]:
            arr[k] = arr[k-1]
            k -= 1
        arr[k] = key

    return arr


if __name__ == '__main__':

    arr = [10, 4, 43, 5, 57, 91, 45, 9, 7]
    print(f'Sorted Array using Insertion Sort ===>> {insertionSort(arr)}')