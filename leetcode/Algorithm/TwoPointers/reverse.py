# Using Slicing
def reverse(s):
    return s[::-1]


# Using two pointers
def reverse1(s):
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    print(reverse1(s))
