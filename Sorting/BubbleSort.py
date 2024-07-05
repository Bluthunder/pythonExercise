"""
Date - 05.06.2024
Topic - Sorting

Bubble Sort, also called sinking sort is simplest sorting algorithm
Time Complexity
Best Case - O(n^2)


"""

def bubble_sort(arr: list) -> list:
    for passnum in range(len(arr) - 1, 0, -1):
        for i in range(passnum):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


"""
This is optimized by using additional flag for swapped. No more swaps indicate the completion 
of sorting, we can use this flag to skip the remaining passes.
"""
# def bubble_sort_optimized(arr: list) -> list:
#     swapped = 1
#     for passnum in range(len(arr)-1, 0, -1):
#         if swapped == 0:
#             return
#         for i in range(passnum):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 swapped = 1



if __name__ == '__main__':
    arr = [10, 4, 43, 5, 57, 91, 45, 9, 7]
    print(f'Sorted array using bubble sort ===>> {bubble_sort(arr)}')

    # print(f'Optimized Bubble Sort ===>> {bubble_sort_optimized(arr)}')
