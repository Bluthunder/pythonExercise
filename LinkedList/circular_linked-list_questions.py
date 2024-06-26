class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class Circular_Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = " "
        while temp_node:
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

    def node_count(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
            if temp == self.head:
                break
        return count

    def split_list(self):
        if self.length == 0:
            return None, None

        mid_ptr = (self.length + 1) // 2
        count = 1

        first_list = Circular_Linked_List()
        second_list = Circular_Linked_List()

        current = self.head
        lastNode_first_list = None

        while count <= mid_ptr:
            first_list.append(current.value)
            lastNode_first_list = current
            current = current.next
            count += 1

        if lastNode_first_list:
            first_list.tail = lastNode_first_list
            first_list.tail.next = first_list.head

        while current != self.head:
            second_list.append(current.value)
            current = current.next

        if second_list.length > 0:
            second_list.tail = self.tail
            second_list.tail.next = second_list.head

        return [first_list, second_list]

    def split_list_two_ptr(self):
        fast_ptr = slow_ptr = self.head

        while fast_ptr.next != self.head and fast_ptr.next.next != self.head:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        first_half = Circular_Linked_List()
        second_half = Circular_Linked_List()

        if fast_ptr.next.next == self.head:
            fast_ptr = fast_ptr.next

        first_half.head = self.head

        if self.head.next != self.head:
            second_half.head = slow_ptr.next

        fast_ptr.next = slow_ptr.next

        slow_ptr.next = self.head

        return first_half, second_half

    def delete_node(self, key):
        if self.head.value == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = cur.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.value == key:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(self, step):
        temp = self.head
        while self.node_count() > 1:
            step_count = 1
            while step_count is not step:
                temp = temp.next
                step_count += 1

            print(f'Removed --- {temp.value}')
            self.delete_node(temp.value)
            temp = temp.next
        return f" Last person standing is : {temp.value}"

    def floyd_cycle_detection(self):
        slow_ptr = fast_ptr = self.head

        while slow_ptr is not None and fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                return True
        return False

    def is_sorted(self):
        temp = self.head
        while temp.next is not self.head:
            if temp.value > temp.next.value:
                return False
            temp = temp.next
        return True


#


if __name__ == '__main__':
    csl = Circular_Linked_List()
    csl.append(5)
    csl.append(10)
    csl.append(15)
    csl.append(20)
    csl.append(25)
    csl.append(35)
    csl.append(45)

    print(csl)

    # first, second = csl.split_list_two_ptr()
    # print(first)
    # print(second)
    print(csl.josephus_circle(3))
