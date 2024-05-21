"""
Date - 21.05.2024

DSA - Tree

This is an implementation of Tree traversals (preorder, inorder, postorder) in non-recursive way

"""


class BTNode:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def preOrderNonRecurr(self, root, result):
        if not root:
            return

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            result.append(node.value)
            print(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def inOrderNonRecurr(self, root, result):
        if not root:
            return

        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left

            else:
                node = stack.pop()
                result.append(node.value)
                print(node.value)
                node = node.right


    def postOrderNonRecurr(self, root, result):
        if not root:
            return

        visited = set()
        stack = []
        node = root

        while stack or node:
            if node:
                stack.append(node)
                node = node.left

            else:
                node = stack.pop()
                if node.right and not node.right in visited:
                    stack.append(node)
                    node = node.right
                else:
                    visited.add(node)
                    result.append(node.value)
                    print(node.value)
                    node = None


if __name__ == '__main__':
    bt_node = BTNode(1)
    node_1 = BTNode(2)
    node_2 = BTNode(3)
    node_3 = BTNode(4)
    node_4 = BTNode(5)
    node_5 = BTNode(6)
    node_6 = BTNode(7)

    bt_node.left = node_1
    bt_node.right = node_2

    node_1.left = node_3
    node_1.right = node_4

    node_2.left = node_5
    node_2.right = node_6

    bt_node.postOrderNonRecurr(bt_node, result=[])
