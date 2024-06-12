"""
Date - 11.06.2024
DSA - Binary Search tree

Binary Search tree has advantage of being more efficient for searching over Binary tree

Worst case complexity - O(logn)

This implemtation of BST has
1. Insert - insert() - Insert into BST
2. Traversal -

"""

class BSTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def insert(self, root, value):
        if root.data == None:
            root.data = value

        elif value <= root.data:
            if root.left is None:
                root.left = BSTNode(value)
            else:
                self.insert(root.left, value)

        else:
            if root.right is None:
                root.right = BSTNode(value)
            else:
                self.insert(root.right, value)

        return "Node successfully inserted"




if __name__ == '__main__':
    newBST = BSTNode(None)
    print(newBST.insert(newBST, 70))
    print(newBST.insert(newBST, 60))

    print(newBST.data)
    print(newBST.left.data)