#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
"""
Condition for Principal Diagonal:
The row-column condition is row = column.

Condition for Secondary Diagonal:
The row-column condition is row = numberOfRows - column -1.

"""
def diagonalDifference(arr):
    # Write your code here
    prim = 0
    sec = 0

    length = len(arr[0])

    for i in range(length):
        prim += arr[i][i]
        sec += arr[i][(length - i - 1)]

    return abs(prim - sec)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
