from collections import Counter


# Method 1
def makeAnagrams1(a, b):
    C1 = Counter(a)
    for c in b:
        C1[c] -= 1
    val = C1.values()
    s = sum(abs(i) for i in val)
    return s


# Method 2
def makeAnagrams2(a, b):
    d1 = Counter(a)
    d2 = Counter(b)
    total = (d1 - d2) + (d2 - d1)
    return sum(total.values())


# Method 3 Without Counter
def makeAnagrams3(a, b):
    counta = [0] * 26
    countb = [0] * 26

    # counting freq of each char in 1st String
    i = 0
    while i < len(a):
        counta[ord(a[i]) - ord('a')] += 1
        i += 1

    # counting freq of each char in 2nd String
    j = 0
    while j < len(b):
        counta[ord(b[j]) - ord('a')] += 1
        j += 1

    # Traverse count arrays to find the number of characters to be deleted
    result = 0
    for i in range(26):
        result = abs(counta[i] - countb[i])

    return result


if __name__ == '__main__':
    a = input()
    b = input()
    res = makeAnagrams3(a, b)
    print(res)
