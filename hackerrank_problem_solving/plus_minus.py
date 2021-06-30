def plusMinus(arr):
    pos, neg, zer = 0, 0, 0

    for i in range(len(arr)):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        elif arr[i] == 0:
            zer += 1

    ratio_pos = round(pos / len, 6)
    ratio_neg = round(neg / len, 6)
    ratio_zer = round(zer / len, 6)

    print(ratio_pos)
    print(ratio_neg)
    print(ratio_zer)


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
