"""
Date - 06.05.2024
DSA - Stacks

Reverse stack using only push and pop

"""
from stack_using_array_wol import stack


def reverse_stack(in_stack: stack) -> stack:
    new_stack = stack()

    for _ in range(in_stack.get_length()):
        new_stack.push(in_stack.pop())
    # print(f'New stack \n{new_stack}')
    return new_stack


if __name__ == '__main__':
    original_stack = stack()
    original_stack.push(2)
    original_stack.push(3)
    original_stack.push(6)
    original_stack.push(7)
    original_stack.push(8)
    original_stack.push(1)

    print(f'Orginal Stack \n{original_stack}')
    print('**********************************')
    print(f' Reversed Stack \n{reverse_stack(original_stack)}')
