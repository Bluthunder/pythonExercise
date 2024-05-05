"""

Date: 05.05.2023
Check if the parenthesis is balanced
DSA - Stack

Algorithm

1. Create a stack
2. While(end of input is not reached)
    a. if character read is not a symbol to be balanced, ignore it
    b. if the character is an opening symbol like (,{,[, push it onto the stack
    c. if it is a closing symbol like ),},] then if the stack is empty report an error, else pop the stack
    d. if symbol popped is not corresponding to opening symbol report an error.

3. At the end of input if stack is not empty report error
"""
from Stack.stack_using_array_wol import stack
from Stack.stack_using_linked_list import Stack


def check_symbol(in_str: str) -> bool:
    # Empty stack to hold opening parenthesis
    stack = []

    # Dictionary (hash map) to store parenthesis mapping
    close_to_open_dict = {
        "}": "{",
        ")": "(",
        "]": "["
    }
    for c in in_str:
        if c in close_to_open_dict:
            if stack and stack[-1] == close_to_open_dict[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False


if __name__ == '__main__':
    input_str = "[()()]"
    print(check_symbol(input_str))
