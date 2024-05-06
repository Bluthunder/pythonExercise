"""
Date - 06.05.2024
DSA - Stacks

Postfix Evaluation using stacks

Algorithm:

1. Scan the postfix string from left to right
2. Initialize an empty stack
3. Repeat 4 and 5 till all characters are scanned
4. If the scanned characters is an operand, push into stack
5. If the scanned character is an operator, and if operator is a unary operator, then pop an element from stack.
   If the operator is binary, then pop two element from stack. After popping elements from stack, apply the operation
   on the popped elements. Let the result of this operation be retVal on the stack.
6. After all the characters are scanned, we will have only one element in the stack.
7. Return the top of the stack as result

"""
from Stack.stack_using_array_wol import stack


def do_operation(op, operand_1, operand_2):
    if op == "*":
        return operand_1 * operand_2
    elif op == "/":
        return operand_1 / operand_2
    elif op == "+":
        return operand_1 + operand_2
    else:
        return operand_1 - operand_2


def postfix_eval(in_exp: str) -> int:
    op_stack = stack()

    for token in in_exp:
        if token.isnumeric():
            op_stack.push(int(token))
        else:

            operand_2 = op_stack.pop()
            operand_1 = op_stack.pop()
            result = do_operation(token, operand_1, operand_2)
            op_stack.push(result)

    return op_stack.pop()


if __name__ == '__main__':
    postfix_str = '123*+5-'

    print(postfix_eval(postfix_str))
