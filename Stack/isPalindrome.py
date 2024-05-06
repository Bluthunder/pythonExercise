"""
This is palindrome checker function using stacks


"""
from Stack.stack_using_array_wol import stack


def isPalindrome(input_str):
    char_stack = stack()

    for char in input_str:
        char_stack.push(char)

    for char in input_str:
        if char != char_stack.pop():
            return False

    return True


if __name__ == '__main__':
    input_string = "madam"
    print(isPalindrome(input_string))
