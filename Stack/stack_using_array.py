"""
Stack Implementation using fixed length array
Date - 01.05.2023

Stack has below operations

1. Push: push() - insert item at the end stack
2. Pop: pop() - remove item from the end of stack and return the item
3. Peek: peek() - check the top of the stack and return item from top without removing
4. Is Empty: is_empty() - check the stack is non empty
5. Size: size() - get the size of the stack
6. Delete: delete_all() - delete entire stack.
"""


class stack(object):

    def __init__(self, limit=10):
        self.stk = []
        self.limit = limit

    def __str__(self):
        values = [str(x) for x in reversed(self.stk)]
        return f'\n'.join(values)

    def is_empty(self):
        if not self.stk:
            return True
        else:
            return False

    def is_full(self):
        if len(self.stk) == self.limit:
            return True
        else:
            return False

    def push(self, value):
        if self.is_full():
            return "The Stack is full !!!"
        else:
            self.stk.append(value)
            return "The Element is inserted successfully"

    def pop(self):
        if self.is_empty():
            return "Stack is Empty !!!"
        else:
            return self.stk.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is Empty !!"
        else:
            return self.stk[len(self.stk) - 1]

    def size(self):
        return len(self.stk)

    def delete_all(self):
        self.stk = None


if __name__ == '__main__':
    Stack = stack()
    Stack.push(12)
    Stack.push(22)
    Stack.push(32)
    Stack.push(52)
    Stack.push(42)
    Stack.push(2)

    # print(Stack)

    print(Stack.pop())

    # print(f'After {Stack}')

    print(Stack.peek())
