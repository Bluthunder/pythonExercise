"""
Creation Date: 17 April 2024
DSA Topic: Linked List

This is based on exercises from book Data Structure and Algorithm: Thinking with Python


In a linked list implementation below following method has been implemented

1. Traversal: traversal - For Traversing the list
2. Append: append - For inserting value at the end of the list
3. Prepend: prepend - For inserting value at the start of the list
4. Insert at Position: insert_at_pos - For inserting value at given index
5. Pop First: pop_first - Remove from the beginning of the list
6. Pop: pop - Remove from the end of the list

"""


# Single Node for Linked List
class Node:

    # Constructor
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' --> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert_at_pos(self, value, index):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return -1
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def traversal(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def pop_first(self):
        pop_node = self.head

        if self.length == 0:
            print(f'Linked List is Empty, no element to remove')
            return None

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            pop_node.next = None

        return pop_node

    def pop(self):
        if self.length == 0:
            print(f'Empty List, no element to remove')
            return None

        pop_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return pop_node


if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.append(30)
    # linkedlist.append(10)
    # linkedlist.prepend(50)
    # linkedlist.insert_at_pos(40, 1)
    # linkedlist.insert_at_pos(41, 2)
    # linkedlist.insert_at_pos(42, 3)
    # linkedlist.insert_at_pos(43, 1)
    #
    # linkedlist.traversal()
    print(f'Linked List : {linkedlist}')

    linkedlist.pop()

    print(f'Linked List : {linkedlist}')
