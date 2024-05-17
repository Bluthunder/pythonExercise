"""
Date - 14.05.2024

DSA - Double ended Queue_DS

"""


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, value):
        self.items.append(value)

    def addRear(self, value):
        self.items.insert(0, value)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ---**>> ".join(values)

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    dq = Deque()
    print(f' Check if is empty -- > {dq.isEmpty()}')
    dq.addFront(2)
    dq.addFront(3)
    dq.addFront(4)

    print(f' Double Ended Q --> {dq}')
