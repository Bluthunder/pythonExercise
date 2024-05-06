"""
Date - 06.05.2023
DSA - Stack

3 stack in one array

"""


class Multistack:

    def __init__(self, stacksize):
        self.numberstacks = 3  # number of stack

        # Create a list with all the values as zero of length stacksize * numberofstack
        self.custlist = [0] * (stacksize * self.numberstacks)

        # Create a list of size of stacks initalized to zero
        self.sizes = [0] * self.numberstacks

        self.stacksize = stacksize # initialize stack size

    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False

    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False

    def indexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return f'Stack {stacknum} is FULL !!!'
        else:
            self.sizes[stacknum] += 1
            self.custlist[self.indexOfTop(stacknum)] = item

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return f'Stack {stacknum} is EMPTY !!!'
        else:
            value = self.custlist[self.indexOfTop(stacknum)]
            self.custlist[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
        return value

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return f'Stack {stacknum} is EMPTY !!!'
        else:
            value = self.custlist[self.indexOfTop(stacknum)]
        return value


if __name__ == '__main__':
    custom_stack = Multistack(6)

    print(custom_stack.custlist)
    print(custom_stack.sizes)
    print(custom_stack.stacksize)
    print(custom_stack.isFull(0))
    print(custom_stack.isEmpty(1))

    custom_stack.push(1, 0)
    custom_stack.push(2, 0)
    custom_stack.push(3, 0)
    custom_stack.push(4, 1)

    print(custom_stack.peek(0))

    print(custom_stack.custlist)
