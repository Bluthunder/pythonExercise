"""
Given a stack of integers, write a function pairWiseConsecutive() that checks whether numbers in the
stack are pairwise consecutive or not. The pairs can be increasing or decreasing, and if the stack
has an odd number of elements, the element at the top is left out of a pair.
The function should retain the original stack content.


Without Using Any Auxiliary Stack:

Follow the steps to implement the approach:

1. Initialize a variable with the top element of the stack and pop it out.
2. Iterate over the remaining elements of the stack and check if the absolute difference between
each pair of consecutive elements is equal to 1. If it is not, return “No”.
3. If the stack has an odd number of elements, discard the top element.
4. If the iteration completes without returning “No”, return “Yes”.


"""


def check_pairwise(s):
    # If there's an odd number of elements, pop the top element and discard it
    if len(s) % 2 != 0:
        s.pop()

    prev = s[-1]
    s.pop()

    while s:
        curr = s[-1]
        s.pop()

        if abs(curr - prev) != 1:
            return "False"

        if s:
            prev = s[-1]
            s.pop()

    return "True"


if __name__ == '__main__':
    s = [4, 5, -2, -3, 11, 10, 5, 6, 20]
    result = check_pairwise(s)
    print(f'Result {result}')
