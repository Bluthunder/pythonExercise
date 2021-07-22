def repeatedStrings(s, n):
    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")


def repeatedStringsClassic(inpStr, N):
    c = inpStr.count("a")
    d = N // len(inpStr)

    if N % len(inpStr) == 0:
        c = c * d
    else:
        r = N % len(inpStr)
        c = c * d + inpStr[:r].count("a")

    return c


if __name__ == '__main__':
    s = input()
    n = int(input().strip())
    result = repeatedStrings(s, n)
    print(result)
