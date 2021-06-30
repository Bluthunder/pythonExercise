import os


def birthday_cake_candles(candles):
    count = 0
    temp = candles[0]
    for i in range(1, len(candles)):
        if candles[i] > temp:
            temp = candles[i]
    print(temp)
    for j in range(0, len(candles)):
        if candles[i] == temp:
            count += 1
    return count


'''
Another pythonic approach
'''


def bcc(arr):
    return arr.count(max(arr))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthday_cake_candles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()
