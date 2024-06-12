
def palindrome_index(s: str) -> str:
    n = len(s)

    for i in range(n//2 + 1):
        if s[i] != s[n-1-i]:
            if s[i] == s[n-2-i] and s[i+1] == s[n-3-i]:
                return n-1-i
            else:
                return i
    return -1


if __name__ == '__main__':
    s = "bcbc"

    print(palindrome_index(s))