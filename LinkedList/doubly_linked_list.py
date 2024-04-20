"""
Creation Date: 20 April 2024
DSA Topic: Linked List - Double Linked List

This is based on exercises from book
1. Data Structure and Algorithm: Thinking with Python
2. Udemy Course by Elshad Karimov


In a linked list implementation below following method has been implemented

1. Traversal: traversal - For Traversing the list
2. Append: append - For inserting value at the end of the list
3. Prepend: prepend - For inserting value at the start of the list
4. Insert at Position: insert_at_pos - For inserting value at given index
5. Pop First: pop_first - Remove from the beginning of the list
6. Pop: pop - Remove from the end of the list
7. Remove: remove - Remove a node at a given index
8. Get: get - Get the value of node at a given index
9. Set Value: set-value - Insert a value at a given index
10. Delete Linked List: delete - Delete entire linked list
11. Search Linked List: search - Search for target value in linked list and return true

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        # return f'{self.prev}<--{self.value}-->{self.next}'
        return str(self.value)


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' <--> '
            temp_node = temp_node.next

        return result

    def traversal(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def reverse_traverse(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.prev

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

    def prepend(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def insert_at_pos(self, value, index):
        new_node = Node(value)

        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return

        temp_node = self.get(index - 1)

        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node

        self.length += 1

    def search(self, target):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return index
            current_node = current_node.next
            index += 1

        return -1

    def get(self, index):
        '''

        if index < 0 or index > self.length:
            return None
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.value

        '''

        # Optimized Method to get for doubly linked list

        if index < 0 or index >= self.length:
            return None

        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev

        return current_node

    def set(self, value, index):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    def pop_first(self):
        if not self.head:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        if not self.tail:
            return None
        popped_node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index < 0 or index > self.length:
            return None

        if index == 0:
            return self.pop_first()
        elif index == -1 or index == self.length - 1:
            return self.pop()
        else:
            temp_node = self.get(index - 1)
            popped_node = temp_node.next
            temp_node.next = popped_node.next
            popped_node.next.prev = temp_node
            popped_node.next = None
            popped_node.prev = None

        self.length -= 1
        return popped_node


if __name__ == '__main__':
    doublylinkedlist = DoublyLinkedList()
    doublylinkedlist.append(10)
    doublylinkedlist.append(20)
    doublylinkedlist.prepend(5)

    print(doublylinkedlist)

    doublylinkedlist.traversal()
    doublylinkedlist.reverse_traverse()
    print(f'Element is found at index: {doublylinkedlist.search(100)}')
    print(f'Value at given node: {doublylinkedlist.get(2)}')

    doublylinkedlist.set(1, 0)

    print(f'Value Updated: {doublylinkedlist}')

    doublylinkedlist.insert_at_pos(100, 0)
    doublylinkedlist.insert_at_pos(15, 3)
    doublylinkedlist.insert_at_pos(30, 5)

    print(doublylinkedlist)

    print(doublylinkedlist.remove(5))

    print(f'After Pop : {doublylinkedlist}')
