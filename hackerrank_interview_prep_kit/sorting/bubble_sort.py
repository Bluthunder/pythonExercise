def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(1, len(arr) - i):
            temp = 0
            if arr[j] < arr[j - 1]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp

    return arr

if __name__ == '__main__':
    arr = [2, 4, 6, 8, 0, 9]
    r = bubbleSort(arr)
    print(r)

