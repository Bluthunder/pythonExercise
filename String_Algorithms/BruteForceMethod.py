"""
Date - 06.06.2024

DSA Topic - String Algorithms

String Pattern matching - Brute Force Method.

For a given string text of length n, and given pattern of m using brute force method number of comparisons needed
is n-m+1

"""

""" This algorithm searches for the first occurence of a pattern in string"""


def strStrBruteForceMethod(text: str, pattern: str) -> int:
    if not pattern:
        return 0

    for i in range(len(text) - len(pattern) + 1):
        stri = i
        patterni = 0
        while stri < len(text) and patterni < len(pattern) and text[stri] == pattern[patterni]:
            stri += 1
            patterni += 1
        if patterni == len(pattern):
            return i

    return -1


if __name__ == '__main__':
    input_text = "xxxxyzabcdefabc"
    pattern_text = "abc"

    print(f'{pattern_text} appears in {input_text} at position -- {strStrBruteForceMethod(input_text, pattern_text)}')
