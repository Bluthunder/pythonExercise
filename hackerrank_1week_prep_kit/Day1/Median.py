def median(arr):
    arr = sorted(arr)
    return arr[len(arr) // 2]


if __name__ == '__main__':
    arr = [0, 4, 5, 6, 3, 2, 1]
    print(median(arr))
