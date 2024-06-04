"""
Date - 20.05.2024

DSA - Tree

This covers Tree DSA implementation using linked list.

All the traversals (Preorder, Inorder, PostOrder) are implemented using recursion

"""

from Queue_DS.Q import Que as Q
from Stack.stack_using_array_wol import stack


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

    def levelOrderTraversal(self, root, result):
        if not root:
            return
        q = Q()
        q.enqueue(root)
        node = None

        while not q.is_empty():
            node = q.dequeue()
            if node.data is not None:
                result.append(node.data)
                print(node.data)

            if node.left is not None:
                q.enqueue(node.left)

            if node.right is not None:
                q.enqueue(node.right)

    def searchTree(self, root, node):
        if not root:
            return 0

        if root.data == node:
            return 1
        else:
            temp_ptr = self.searchTree(root.left, node)
            if temp_ptr == 1:
                return temp_ptr
            else:
                return self.searchTree(root.right, node)

    def searchTree_wor(self, root, node):

        if not root:
            return 0

        que = Q()
        que.enqueue(root)
        temp_node = None

        while not que.is_empty():
            temp_node = que.dequeue()
            if node == temp_node.data:
                return 1

            if temp_node.left is not None:
                que.enqueue(temp_node.left)

            if temp_node.right is not None:
                que.enqueue(temp_node.right)
        return 0

    def insert_into_bt(self, root, value):
        new_node = BinaryTreeNode(value)

        if root is None:
            root = new_node

        customQ = Q()
        customQ.enqueue(root)
        while not customQ.is_empty():
            temp_node = customQ.dequeue()
            if value == temp_node.data:
                return root

            if temp_node.left is not None:
                customQ.enqueue(temp_node.left)
            else:
                temp_node.left = new_node
                return root

            if temp_node.right is not None:
                customQ.enqueue(temp_node.right)
            else:
                temp_node.right = new_node
                return root

    def size_of_tree(self, root):
        if not root:
            return 0
        else:
            return self.size_of_tree(root.left) + self.size_of_tree(root.right) + 1

    def size_of_tree_wor(self, root):

        if not root:
            return 0

        q = Q()
        count = 0
        temp_ptr = None
        q.enqueue(root)

        while not q.is_empty():
            temp_ptr = q.dequeue()
            count += 1

            if temp_ptr.left is not None:
                q.enqueue(temp_ptr.left)

            if temp_ptr.right is not None:
                q.enqueue(temp_ptr.right)

        return count

    def reverse_levelOrderTraversal(self, root):
        if not root:
            return 0

        q = Q()
        stk = stack()
        temp_ptr = None
        count = 0
        q.enqueue(root)

        while not q.is_empty():
            temp_ptr = q.dequeue()
            if temp_ptr.left is not None:
                q.enqueue(temp_ptr.left)

            if temp_ptr.right is not None:
                q.enqueue(temp_ptr.right)

            stk.push(temp_ptr)

        while not stk.is_empty():
            print(stk.pop().data)

    def delete_tree(self, root):
        if root is None:
            return
        self.delete_tree(root.left)
        self.delete_tree(root.right)
        print(f'Deleting Node: {root.data}')
        del root

    def deepest_node(self, root):
        if not root:
            return

        que = Q()
        temp_ptr = None
        que.enqueue(root)
        while not que.is_empty():
            temp_ptr = que.dequeue()
            if temp_ptr.left is not None:
                que.enqueue(temp_ptr.left)

            if temp_ptr.right is not None:
                que.enqueue(temp_ptr.right)

        deepest_node = temp_ptr
        return deepest_node.data

    def delete_deepest_node(self, root, d_node):
        if not root:
            return
        else:
            q = Q()
            q.enqueue(root)
            while not q.is_empty():
                temp_ptr = q.dequeue()
                if temp_ptr.data is d_node:
                    temp_ptr.data = None
                    # del temp_ptr.data
                    return
                if temp_ptr.right:
                    if temp_ptr.right.data is d_node:
                        temp_ptr.right.data = None
                        # del temp_ptr.right.data
                        return
                    else:
                        q.enqueue(temp_ptr.right)

                if temp_ptr.left:
                    if temp_ptr.left.data is d_node:
                        temp_ptr.left.data = None
                        # del temp_ptr.left.data
                        return
                    else:
                        q.enqueue(temp_ptr.left)

    def delete_node(self, root, node):
        if not root:
            return
        else:
            customQ = Q()
            customQ.enqueue(root)
            while not customQ.is_empty():
                temp_ptr = customQ.dequeue()
                if temp_ptr.data == node:
                    dNode = self.deepest_node(root)
                    self.delete_deepest_node(root, dNode)
                    temp_ptr.data = dNode
                    # self.delete_deepest_node(root, dNode)

                    return "The Node is deleted Successfully"


                if temp_ptr.left is not None:
                    customQ.enqueue(temp_ptr.left)

                if temp_ptr.right is not None:
                    customQ.enqueue(temp_ptr.right)

            return "Failed to delete"


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
    # r_node.postOrderTraversal(r_node, result=[])

    # r_node.levelOrderTraversal(r_node, result=[])
    #
    # r_node.insert_into_bt(r_node, 11)
    # r_node.levelOrderTraversal(r_node,result=[])
    # print(r_node.size_of_tree_wor(r_node))

    # r_node.reverse_levelOrderTraversal(r_node)

    # dNode = r_node.deepest_node(r_node)
    # print(dNode.data)
    # r_node.delete_deepest_node(r_node, dNode)

    r_node.delete_node(root=r_node, node=4)
    #

    # r_node.delete_tree(r_node)
    # r_node = None

    r_node.levelOrderTraversal(r_node, result=[])
