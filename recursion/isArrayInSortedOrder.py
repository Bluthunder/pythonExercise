"""
Date: 11 April 2024
Check whether array is sorted order with recursion

"""


def is_array_in_sorted_order(A):
    # Base Case

    if len(A) == 1:
        return True

    return A[0] <= A[1] and is_array_in_sorted_order(A[1:])


if __name__ == '__main__':
    A = [200, 127, 220, 246, 321, 454, 534, 565, 933]
    print(is_array_in_sorted_order(A))
