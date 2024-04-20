"""
Creation Date: 17 April 2024
DSA Topic: Linked List - Single Linked List

This is based on exercises from book Data Structure and Algorithm: Thinking with Python


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
11. Search: search - Search for value in linked list

"""


# Single Node for Linked List
class Node:

    # Constructor
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


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

    def remove(self, index):
        if index < 0 or index > self.length:
            print(f'Index outside list')
            return None

        if index == 0:
            return self.pop_first()
        elif index == -1 or index == self.length - 1:
            return self.pop()
        else:
            prev_node = self.get(index - 1)
            pop_node = prev_node.next
            prev_node.next = pop_node.next
            pop_node.next = None
            self.length -= 1
            return pop_node

    def get(self, index):
        current_node = self.head
        if index < 0 or index > self.length:
            return None

        for _ in range(index):
            current_node = current_node.next
        return current_node

    def set_value(self, index, value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    def search(self, target):
        current_node = self.head
        index = 0
        while current_node.value:
            if current_node.value == target:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def delete(self):
        self.head = None
        self.tail = None
        self.length = 0


if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.append(30)
    linkedlist.append(10)
    linkedlist.prepend(50)
    linkedlist.insert_at_pos(40, 1)
    linkedlist.insert_at_pos(41, 2)
    linkedlist.insert_at_pos(42, 3)
    linkedlist.insert_at_pos(43, 1)

    print(f'Linked List Before : {linkedlist}')

    linkedlist.pop()
    linkedlist.pop_first()
    linkedlist.remove(3)

    print(f'Linked List After : {linkedlist}')

    print(linkedlist.get(2))
