"""
Date - 10.05.2024
DSA - Queue

Below is the circular queue implementation based on array with fixed size
Circular Queue ADT has below operations

1. Enqueue - enqueue(): This is used to add elements at the end of the queue
2. Dequeue - dequeue(): This is used to remove elements from the front of the queue
3. Peek - peek(): To get the element in the front without removing it.
4. Delete - delete(): To delete the entire queue
5. IsEmpty - is_empty(): This boolean function returns if the queue is empty
6. IsFull - is_full(): This boolean function returns if the queue is full


"""

class CircularQueue:

    def __init__(self, max_size):
        self.items = max_size * [None]
        self.rear = -1
        self.front = -1
        self.size = 0
        self.max_size = max_size

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def is_full(self):
        if self.rear + 1 == self.front:
            return True
        elif self.front == 0 and self.rear + 1 == self.max_size:
            return True
        else:
            return False
        # return self.size == self.max_size

    def is_empty(self):
        if self.rear == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.is_full():
            print(f'Q is full')

        else:
            if self.rear + 1 == self.max_size:
                self.rear = 0
            else:
                self.rear += 1
                if self.front == -1:
                    self.front = 0
            self.items[self.rear] = value
            print(f'Element inserted at end of q')

    def dequeue(self):
        if self.is_empty():
            print(f' Q is Empty')
        else:
            firstele_ptr = self.items[self.front]
            front = self.front
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            elif self.front + 1 == self.max_size:
                self.front = 0
            else:
                self.front += 1
            self.items[front] = None
            return firstele_ptr

    def peek(self):
        if self.is_empty():
            print('List is empty')

        else:
            return self.items[self.front]

    def delete(self):
        self.items = self.max_size * [None]
        self.front = -1
        self.rear = -1


if __name__ == '__main__':
    cirQ = CircularQueue(10)
    cirQ.enqueue(2)
    cirQ.enqueue(3)
    cirQ.enqueue(4)
    cirQ.enqueue(5)
    cirQ.enqueue(6)
    print(cirQ.dequeue())
