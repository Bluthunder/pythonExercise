def interpolation_search(array, K):
    n = len(array)
    low = 0
    high = n - 1

    while low <= high and array[low] <= K <= array[high]:
        if low == high:
            if array[low] == K:
                return low
            return -1

        index = low + ((K - array[low]) * (high - low)) // (array[high] - array[low])

        if array[index] < K:
            low = index + 1
        elif array[index] > K:
            high = index - 1
        else:
            # found K
            return index

    return -1


if __name__ == "__main__":
    array = [2, 3, 6, 8, 10, 13, 16, 18]
    K = 13

    res = interpolation_search(array, K)

    if res >= 0:
        print(f"{K} found at index: {res}")
    else:
        print(f"{K} not found")
