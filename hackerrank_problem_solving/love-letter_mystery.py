def theLoveLetterMystery(s):
    val = [abs(ord(s[i]) - ord(s[-i - 1])) for i in range(len(s) // 2)]
    return sum(val)


if __name__ == '__main__':
    s = "abcdef"
    print(theLoveLetterMystery(s))
