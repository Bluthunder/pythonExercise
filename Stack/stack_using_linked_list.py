class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next


class Stack:

    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return "\n".join(values)

    def is_empty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)

        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        else:
            pop_node = self.LinkedList.head
            self.LinkedList.head = self.LinkedList.head.next
            return pop_node

    def peek(self):
        if self.is_empty():
            return 'Stack is empty'
        else:
            return self.LinkedList.head

    def delete_all(self):
        self.LinkedList.head = None


if __name__ == '__main__':
    customStack = Stack()
    customStack.push(1)
    customStack.push(2)
    customStack.push(3)
    print(customStack)
    print(customStack.pop())
    print(customStack.peek())
