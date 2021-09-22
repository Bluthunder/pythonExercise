def minimumSwaps(arr):
    swaps = 0
    for i in range(0, len(arr)):
        while arr[i] != i + 1:
            temp = arr[i] - 1
            arr[i], arr[temp] = arr[temp], arr[i]
            swaps += 1

    return swaps


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    res = minimumSwaps(a)

# fptr.write(str(res) + '\n')

# fptr.close()
