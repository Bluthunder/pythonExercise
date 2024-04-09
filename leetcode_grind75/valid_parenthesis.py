"""
Date - 9th April 2024
Leetcode Grind 75 Question: 2
DSA Topic: Stack

"""


def valid_parenthesis(s: str) -> bool:

    # Empty stack to hold opening parenthesis
    stack = []

    # Dictionary (hash map) to store parenthesis mapping
    close_to_open_dict = {
                          "}": "{",
                          ")": "(",
                          "]": "["
                          }
    for c in s:
        if c in close_to_open_dict:
            if stack and stack[-1] == close_to_open_dict[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False


if __name__ == '__main__':
    s = "()[]{}"
    print(valid_parenthesis(s))



