def rotLeft(a, d):
    d = d % len(a)
    return a[d:] + a[:d]


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    dist = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = rotLeft(arr, dist)
