"""
Date - 05.05.2024
Convert infix expression to postfix expression
DSA - Stack

Algorithm: -

1. Create a stack
2. for each character t in the input stream:
    if t is an operand:
        output t
    else if t is a right parenthesis:
        pop and output tokens until left parenthesis is popped (but not output)
    else t is an operator or left parenthesis:
        pop and output tokens until one of lower priority that t is encountered or left parenthesis is encountered or stack is empty:
        push t
3.  pop and output tokens until the stack is empty

"""
from Stack.stack_using_array_wol import stack


def infix_to_postfix(input_exp: str) -> str:
    prec = {'^': 4,
            '*': 3,
            '/': 3,
            '%': 3,
            '+': 2,
            '-': 2,
            '(': 1
            }

    operation_stack = stack()
    postfix_list = []
    token_list = input_exp.split()

    for token in input_exp:
        if token.isalnum():
            postfix_list.append(token)
        elif token == '(':
            operation_stack.push(token)
        elif token == ')':
            top_token = operation_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = operation_stack.pop()
        else:
            while not operation_stack.is_empty() and prec[operation_stack.peek()] >= prec[token]:
                postfix_list.append(operation_stack.pop())
            operation_stack.push(token)

    while not operation_stack.is_empty():
        postfix_list.append(operation_stack.pop())

    return "".join(postfix_list)


if __name__ == '__main__':
    infix_string = 'A*B-(C+D)+E'
    print(infix_to_postfix(infix_string))



