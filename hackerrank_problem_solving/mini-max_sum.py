def miniMaxSum(arr):
    arr.sort()
    min = sum(arr[:4])
    arr.sort(reverse=True)
    max = sum(arr[:4])
    print(min, max)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
