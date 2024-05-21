"""
Date - 20.05.2024

DSA - Tree

This covers Tree DSA implementation using linked list.

All the traversals (Preorder, Inorder, PostOrder) are implemented using recursion

"""


class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # def __str__(self, level=0):
    #     str_rep = " " * level + str(self.data) + '\n'
    #     for child in

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def insertLeft(self, node):
        if self.left is None:
            self.left = BinaryTreeNode(node)

        else:
            temp = BinaryTreeNode(node)
            temp.left = self.left
            self.left = temp

    def insertRight(self, node):
        if self.right is None:
            self.right = BinaryTreeNode(node)

        else:
            temp = BinaryTreeNode(node)
            temp.right = self.right
            self.right = temp

    def preOrderTraversal(self, root, result):
        if not root:
            return
        result.append(root.data)
        print(root.data)
        self.preOrderTraversal(root.left, result)
        self.preOrderTraversal(root.right, result)

    def inOrderTraversal(self, root, result):
        if not root:
            return

        self.inOrderTraversal(root.left, result)
        result.append(root.data)
        print(root.data)
        self.inOrderTraversal(root.right, result)

    def postOrderTraversal(self, root, result):
        if not root:
            return

        self.postOrderTraversal(root.left, result)
        self.postOrderTraversal(root.right, result)
        result.append(root.data)
        print(root.data)


if __name__ == '__main__':
    r_node = BinaryTreeNode(1)
    ch1_node = BinaryTreeNode(2)
    ch2_node = BinaryTreeNode(3)
    ch3_node = BinaryTreeNode(4)
    ch4_node = BinaryTreeNode(5)
    ch5_node = BinaryTreeNode(6)
    ch6_node = BinaryTreeNode(7)

    r_node.left = ch1_node
    r_node.right = ch2_node

    ch1_node.left = ch3_node
    ch1_node.right = ch4_node

    ch2_node.left = ch5_node
    ch2_node.right = ch6_node

    # r_node.preOrderTraversal(r_node, result=[])
    # r_node.inOrderTraversal(r_node, result=[])
    r_node.postOrderTraversal(r_node, result=[])


