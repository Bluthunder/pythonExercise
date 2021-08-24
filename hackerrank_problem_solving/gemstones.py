def gemstones(arr):
    rocks = [set(arr[_]) for _ in range(len(arr))]
    print(rocks)
    gems = set.intersection(*rocks)
    print(gems)
    return len(gems)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)
    print(result)

# fptr.write(str(result) + '\n')

# fptr.close()
