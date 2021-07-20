def getMoneySpent(keyboards, drives, b):
    return max([sum([x, y]) for x in keyboards for y in drives if sum([x, y]) <= b] + [-1])


def getMoneySpent_alternateMethod(k, d, s):
    total = -1
    for x in k:
        for y in d:
            z = x + y
            if total < z <= s:
                total = z

    return total


if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #
    moneySpent = getMoneySpent(keyboards, drives, b)
