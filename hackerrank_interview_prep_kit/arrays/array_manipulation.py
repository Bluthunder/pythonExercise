def arrayManipulation(n, queries):
    # init array with zero
    arr = [0] * (n + 2)

    # perform queries operation
    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k

    # find maximum value of the array
    maxNum = temp = 0
    for val in arr:
        temp += val
        maxNum = max(maxNum, temp)

    return maxNum


if __name__ == '__main__':

    #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

#  fptr.write(str(result) + '\n')

#   fptr.close()
