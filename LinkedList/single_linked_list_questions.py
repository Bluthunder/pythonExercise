class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = " "
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

    def get(self, index):
        current_node = self.head
        if index < 0 or index > self.length:
            return None

        for _ in range(index):
            current_node = current_node.next
        return current_node

    def get_node_from_end(self, index_from_end):
        node_ptr = self.head
        count = 0

        index_from_beg = self.length - index_from_end
        return self.get(index_from_beg)

    # This is approach uses two pointers
    def get_node_from_end_efficient(self, nth_from_end):
        if nth_from_end < 0:
            return None

        temp_ptr, nth_ptr = self.head, self.head
        count = 0

        while count < nth_from_end and temp_ptr is not None:
            temp_ptr = temp_ptr.next
            count += 1

        if count < nth_from_end or temp_ptr is None:
            return None

        while temp_ptr is not None:
            temp_ptr = temp_ptr.next
            nth_ptr = nth_ptr.next

        return nth_ptr


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)
    linked_list.append(50)

    print(linked_list)

    print(linked_list.get_node_from_end_efficient(2))
   # print(linked_list.get_node_from_end(2))
