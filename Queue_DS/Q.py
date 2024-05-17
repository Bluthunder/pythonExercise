"""
Date - 09.05.2024
DSA - QUEUE

This is ADT implementation of queue using python list (arrays) without any size limit

"""


class Que:

    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def is_empty(self):
        if not self.items:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "element is inserted at end"

    def dequeue(self):
        if self.is_empty():
            return " No element in Q"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return "No Element in Q"
        else:
            return self.items[0]

    def delete(self):
        self.items = None

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    customeQ = Que()
    print(customeQ.is_empty())
    customeQ.enqueue(3)
    customeQ.enqueue(2)
    customeQ.enqueue(5)
    customeQ.enqueue(6)
    print(customeQ)
    print(f'Dequeue -- {customeQ.dequeue()}')
    print(customeQ)
    print(customeQ.peek())
