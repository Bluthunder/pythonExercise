"""
Date - 12 April 2024
LeetCode Grind 75 Question: 7
DSA Topic - HashMap

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""

from collections import Counter


# Using Sorted Method
def anagram_sorted_method(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


# Using Counter
def anagram_counter_method(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


# Using two hashmaps
def anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    """
    This can also be used to build count of chars in hashmap
    """
    # for i in range(len(s)):
    #     count_s[s[i]] = 1 + count_s.get(s[i], 0)
    #     countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in s:
        if c not in countS:
            countS[c] = 1
        else:
            countS[c] += 1

    for b in t:
        if b not in countT:
            countT[b] = 1
        else:
            countT[b] += 1

    # print(f' count of s {count_s}, t {countT}')

    for ch in countS:
        if countS[ch] != countT.get(ch, 0):
            return False

    return True


if __name__ == '__main__':
    string1 = 'anagram'
    string2 = 'nagaram'

    print(anagram(string1, string2))

    print(f'Anagram Counter ---> {anagram_counter_method(string1, string2)}')

    print(f'Anagram Sorted ---> {anagram_sorted_method(string1, string2)}')
