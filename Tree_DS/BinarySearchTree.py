"""
Date - 11.06.2024
DSA - Binary Search tree

Binary Search tree has advantage of being more efficient for searching over Binary tree

Worst case complexity - O(logn)

Main Operations on BST
1. Find/ Find Minimum/ Find Maximum Element in bst
2. Inserting Element in bst
3. Deleting Element in bst

Auxiliary Operations on BST
1. Finding kth- smallest element in tree
2. Sorting the elements of binary search tree

This implemtation of BST has
1. Insert - insert() - Insert into BST
2. Traversal -

"""
from Queue_DS.Q import Que as Q


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def find_element(self, root, data):
        current_node = root
        while current_node is not None and data != current_node.data:
            if current_node.data < data:
                current_node = current_node.right
            else:
                current_node = current_node.left

        return current_node.data

    def insert_node(self, root, value):
        new_node = BSTNode(value)
        if root is None:
            root = new_node
        else:
            if value < root.data:
                if root.left is None:
                    root.left = new_node
                else:
                    self.insert_node(root.left, value)
            else:
                if root.right is None:
                    root.right = new_node
                else:
                    self.insert_node(root.right, value)

    def preorderTraversal(self, root, result):
        if not root:
            return None
        result.append(root.data)
        print(root.data)
        self.preorderTraversal(root.left, result)
        self.preorderTraversal(root.right, result)

    def inorderTraversal(self, root, result):
        if not root:
            return None
        self.inorderTraversal(root.left, result)
        result.append(root.data)
        print(root.data)
        self.inorderTraversal(root.right, result)

    def postorderTraversal(self, root, result):
        if not root:
            return None
        self.postorderTraversal(root.left, result)
        self.postorderTraversal(root.right, result)
        result.append(root.data)
        print(root.data)

    def levelorderTraversal(self, root, result):
        if not root:
            return
        customQ = Q()
        customQ.enqueue(root)
        node = None
        while not customQ.is_empty():
            node = customQ.dequeue()
            if node.data is not None:
                result.append(node.data)
                print(node.data)

            if node.left is not None:
                customQ.enqueue(node.left)

            if node.right is not None:
                customQ.enqueue(node.right)

    def find_minimum(self, root):
        current_node = root
        if current_node.left is None:
            return current_node.data
        else:
            return self.find_minimum(current_node.left)

    def find_maximum(self, root):
        current_node = root
        if current_node.right is None:
            return current_node.data
        else:
            return self.find_maximum(current_node.right)

    def successorBST(self, root, node):
        successor_node = None
        while root is not None:
            if node.data >= root.data:
                root = root.right
            else:
                successor_node = root.data
                root = root.left
        return successor_node
    
    def predecessorBST(self, root, node):
        predecessor_node = None
        while root is not None:
            if node.data <= root.data:
                root = root.left
            else:
                predecessor_node = root.data
                root = root.right
        return predecessor_node


    def delete_element(self):
        pass


if __name__ == '__main__':
    newBST = BSTNode(5)
    newBST.insert_node(newBST, 10)
    newBST.insert_node(newBST, 90)
    newBST.insert_node(newBST, 30)
    newBST.insert_node(newBST, 60)
    newBST.insert_node(newBST, 80)
    newBST.insert_node(newBST, 20)
    newBST.insert_node(newBST, 50)
    newBST.insert_node(newBST, 40)

    # newBST.preorderTraversal(newBST, result=[])
    # print('******************************************')
    newBST.inorderTraversal(newBST, result=[])
    # print("******************************************")
    # newBST.postorderTraversal(newBST, result=[])

    # print(f'The -- {newBST.find_element(newBST, 30)}')

    # print(f'Minimum Value is -- >> {newBST.find_minimum(newBST)}')
    # print(f'Maximum Value is -- >> {newBST.find_maximum(newBST)}')

    print(f'Successor -- >  {newBST.successorBST(newBST, BSTNode(50))}')
    print(f'Predecessor --> {newBST.predecessorBST(newBST, BSTNode(50))}')
