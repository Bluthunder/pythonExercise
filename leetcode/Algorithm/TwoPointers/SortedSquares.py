def sortedSquares(list_nums):
    l = list(map(lambda x: x * x, list_nums))
    return sorted(l)


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    print(sortedSquares(nums))
