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
        temp = self.head
        result = " "
        while temp:
            result += str(temp.value)
            if temp.next is not None:
                result += ' --> '
            temp = temp.next
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

    def remove_dupes(self):
        """
        remove duplicate nodes from linked list
        """

        if self.head is None:
            return None

        seen = set()
        dummy = Node(-1)
        dummy.next = self.head
        prev_node = dummy
        current_node = self.head

        while current_node:
            if current_node.value in seen:
                prev_node.next = current_node.next
                current_node = current_node.next
            else:
                seen.add(current_node.value)
                prev_node = current_node
                current_node = current_node.next
        return dummy.next

    def remove_elements(self, value):
        dummy = Node(-1)
        dummy.next = self.head

        prev = dummy
        curr = self.head

        while curr is not None:
            if curr.value == value:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next

    def reverse_ll(self):
        prev_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node

    def is_palindrome(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        while prev:
            if self.head.value != prev.value:
                return False
            self.head = self.head.next
            prev = prev.next
        return True


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    print(ll)

    # ll.remove_dupes()
    # print(ll)
    # ll.remove_elements(2)
    # print(ll)
    ll.reverse_ll()
    print(ll)
    # print(ll.is_palindrome())
