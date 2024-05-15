"""
Date - 06.05.2024
DSA - Stacks

Design a stack such that getminimum should be O(1)

This uses an auxillary stack

"""


class SmartStacK():

    def __init__(self):
        self.stack = []
        self.min = []

    def __str__(self):
        values = self.stack.reverse()
        values = [str(x) for x in self.stack]
        return f"\n".join(values)

    def stackPush(self, x):
        self.stack.append(x)
        if not self.min or x <= self.min[-1]:
            self.min.append(x)
        # else:
        #     self.min.append(self.min[-1])

    def stackPop(self):
        x = self.stack.pop()
        if x == self.min.pop():
            self.min.pop()
        return x

    def stackMin(self):
        return self.min[-1]


if __name__ == '__main__':
    stack = SmartStacK()
    stack.stackPush(2)
    stack.stackPush(6)
    stack.stackPush(4)
    stack.stackPush(1)
    stack.stackPush(5)
    print(stack)

    print(f'Minimum value of the {stack.stackMin()}')
