class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        temp = self.head
        result = " "
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += ' --> '
            temp = temp.next
        return result

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class Q:

    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return " ->> ".join(values)

    def enqueue(self, value):
        new_node = Node(value)

        if self.linkedlist.head is None:
            self.linkedlist.head = new_node
            self.linkedlist.tail = new_node

        else:
            self.linkedlist.tail.next = new_node
            self.linkedlist.tail = new_node

    def is_empty(self):
        return self.linkedlist.head is None

    def dequeue(self):
        removed_node = self.linkedlist.head

        if self.linkedlist.head == self.linkedlist.tail:
            self.linkedlist.head = None
            self.linkedlist.tail = None

        else:
            self.linkedlist.head = self.linkedlist.head.next

        return removed_node

    def peek(self):
        return self.linkedlist.head

    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None



if __name__ == '__main__':
    qll = Q()

    qll.enqueue(3)
    qll.enqueue(5)
    qll.enqueue(7)
    qll.enqueue(11)
    qll.enqueue(13)
    print(f' Q: {qll}')
    qll.dequeue()
    print(f' Q^: {qll}')
    print(f' Front of the Q: {qll.peek()}')
