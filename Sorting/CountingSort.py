"""
Date - 06.07.2024
Topic - Counting Sort
This is counting based sorting.
"""

def coutingSort(A, k):
    B = [0 for el in A]
    C = [0 for el in range(0, k+1)]

    for i in range(0, k+1):
        C[i] = 0

    for j in range(0, len(A)):
        C[A[j]] += 1

    for i in range(1, k+1):
        C[i] += C[i-1]

    


