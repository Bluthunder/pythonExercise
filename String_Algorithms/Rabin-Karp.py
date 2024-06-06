"""
Date - 06/06/2024
DSA Topic - String Algorithms

RABIN-KARP algorith is a string matching algorithm, where we will use hashing technique instead of checking for each
possible position on T.
"""


def RabinKarp(text: str, pattern: str):
    if pattern is None and text is None:
        return -1

    if pattern == "" and text == "":
        return -1

    if len(pattern) > len(text):
        return -1

    hashText = Hash(text, len(pattern))
    hashPattern = Hash(pattern, len(pattern))
    hashPattern.update()

    for i in range(len(text) - len(pattern) + 1):
        if hashText.hashedValue() == hashPattern.hashedValue():
            if hashText.text() == pattern:
                return i
        hashText.update()

    return -1


class Hash:

    def __init__(self, text: str, size: int):
        self.str = text
        self.hash = 0

        for i in range(0, size):
            self.hash += ord(self.str[i])

        self.init = 0
        self.end = size

    def update(self):
        if self.end <= len(self.str) - 1:
            self.hash -= ord(self.str[self.init])
            self.hash += ord(self.str[self.end])
            self.init += 1
            self.end += 1

    def hashedValue(self):
        return self.hash

    def text(self):
        return self.str[self.init:self.end]


if __name__ == '__main__':
    print(RabinKarp("3141592653589793", "65"))

    print(RabinKarp("My Name is Kaushik", "ik"))
