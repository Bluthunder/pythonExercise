def caesar_cipher(s: str, k: int) -> str:
    res = ""

    for c in s:
        if c.isalpha():
            if c.isupper():
                c = chr((ord(c) - 65 + k) % 26 + 65)
            else:
                c = chr((ord(c) - 97 + k) % 26 + 97)
        res += c
    return res


if __name__ == '__main__':
    s = "middle-Outz"
    k = 2

    print(caesar_cipher(s, k))
