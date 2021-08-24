import math


def beautifulBinaryString(b):
    return b.count("010")


if __name__ == '__main__':
    n = int(input().strip())
    b = input()
    result = beautifulBinaryString(b)

