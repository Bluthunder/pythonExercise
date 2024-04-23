"""
Creation Date: 23 April 2024
DSA Topic: Linked List - Single Circular Linked List

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
10. Delete Linked List: delete_all - Delete entire linked list
11. Search: search - Search for value in linked list

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = " "
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' --> '
        return result

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        self.length += 1

    def insert_at_pos(self, value, index):
        new_node = Node(value)

        if index < 0 or index > self.length:
            raise ValueError(f'Index {index} is less '
                             f'than 0 or more than'
                             f'length of list')

        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
        temp_node = self.get(index - 1)
        new_node.next = temp_node.next
        temp_node.next = new_node

        self.length += 1

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def traversal(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break

    def search(self, target):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return index
            current_node = current_node.next
            index += 1
            if current_node == self.head:
                break
        return -1

    def set(self, value, index):

        target_node = self.get(index)
        while target_node:
            target_node.value = value
            return True
        return False

    def pop_first(self):
        popped_node = self.head

        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = popped_node.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        pop_node = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            temp_node.next = self.head
            self.tail = temp_node
            pop_node.next = None
        self.length -= 1
        return pop_node

    def remove(self, index):
        if index < 0 or index > self.length:
            print(f'Index outside the list')
            return None

        if index == 0:
            return self.pop_first()
        elif index == self.length:
            return self.pop()
        else:
            prev_node = self.get(index - 1)
            pop_node = prev_node.next
            prev_node.next = pop_node.next
            pop_node.next = None
        self.length -= 1
        return pop_node

    def delete_all(self):
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0


if __name__ == '__main__':
    cs_linked_list = CSLinkedList()
    print(cs_linked_list.head)

    cs_linked_list.append(10)
    cs_linked_list.append(20)
    cs_linked_list.append(30)
    cs_linked_list.prepend(5)

    cs_linked_list.insert_at_pos(15, 2)
    cs_linked_list.insert_at_pos(25, 0)

    print(cs_linked_list)

    # print(cs_linked_list.get(3))

    # cs_linked_list.traversal()

    # print(cs_linked_list.search(10))

    cs_linked_list.set(0, 0)

    cs_linked_list.set(15, 2)

    print(f' Value after update {cs_linked_list}')

    print(cs_linked_list.remove(2))
    #
    print(f' List after pop {cs_linked_list}')
