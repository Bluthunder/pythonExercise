def reverseArray(a):
    n = len(a) // 2
    temp = 0
    for i in range(0, n):
        temp = a[i]
        a[i] = a[len(a) - i - 1]
        a[len(a) - i - 1] = temp

    return a


'''
This uses python slicing
'''


def reverseArray1(a):
    return a[::-1]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    # fptr.write(' '.join(map(str, res)))
    # fptr.write('\n')
    #
    # fptr.close()
