"""
Date: 12 April 2024
Leetcode Grind 75 Question: 6

Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


isAlphanum function is used to ignore space.
"""


def isPalindrome(string: str) -> bool:
    left, right = 0, len(string) - 1

    while left < right:

        # check if left has not crossed right and ignore special char
        while left < right and not isAlphaNum(string[left]):
            left += 1

        while right > left and not isAlphaNum(string[right]):
            right -= 1

        if string[left].lower() != string[right].lower():
            return False

        left, right = left + 1, right - 1

    return True


def isAlphaNum(c) -> bool:
    return (ord("A") <= ord(c) <= ord("z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9")
            )


# This method uses python in built functions and exta memory
def is_palindrome_inbuilt(string: str) -> bool:
    new_str = ""

    for c in string:
        if c.isalnum():
            new_str += c.lower()

    return new_str == new_str[::-1]


if __name__ == '__main__':
    input_string = "A man, a plan, a canal: Panama"

    invalid_string = ".,"

    print(f'This function uses implementations from scratch to check palindrome, {isPalindrome(input_string)}')

    # print(f'This function uses in built python methods, {is_palindrome_inbuilt(invalid_string)}')
