'''
If we find the sum of indices of any element in  a N*N matrix,
we will observe that the sum of indices for any element lies between 0 (when i = j = 0) and 2*N – 2 (when i = j = N-1).
So we will follow the following steps:
Declare a vector of vectors of size 2*N – 1 for holding unique sums from sum = 0 to sum = 2*N – 2.
Now we will loop through the vector and pushback the elements of similar sum to same row in that vector of vectors.
'''

def diagonal(A):
    n = len(A)
    N = 2*n-1
    result =[]

    for _ in range(N):
        result.append([])

    # Push each element in the result vector
    for i in range(n):
        for j in range(n):
            result[i+j].append(A[i][j])

    # Print the diagonals
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j], end=" ")

        print()

A = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

diagonal(A)


